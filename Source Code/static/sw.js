/* ==============================================================================
  - File: sw.js (Service Worker Orchestrator)
  - Author: Amey Thakur
  - Profile: https://github.com/Amey-Thakur
  - Repository: https://github.com/Amey-Thakur/Amey-Thakur.github.io
  - Release Date: December 16, 2025
  - License: MIT License
  - ==============================================================================
  -
  - DESCRIPTION:
  - This script serves as the primary Service Worker for AmeyArc. It handles
  - offline availability and request interception, and it is written so that a
  - reader always receives the version of a page that is currently published.
  -
  - HOW IT WORKS:
  - Pages are fetched from the network first and kept in a cache only as an
  - offline fallback. Fingerprinted assets, whose file name contains a hash of
  - their own contents, are served from the cache. Every other asset is served
  - from the cache and refreshed in the background. Caches from earlier versions
  - are removed during activation.
  -
  - TECH STACK:
  - - Service Worker API
  - - Cache Storage API
  - - Fetch Event Orchestration
  -
  - ============================================================================== */

/*
 * Three rules were learned the hard way and each one is load bearing.
 *
 * 1. A page must never be answered from a cache while the network is available.
 *    The stylesheet is fingerprinted, so its file name changes whenever the
 *    theme changes. A cached page therefore points at a stylesheet that has
 *    been replaced, that request answers 404, and the reader is shown the
 *    article with no styling at all. Only a hard reload cleared it.
 *
 * 2. Asking the network is not the same as asking for the current file. The
 *    site sends `Cache-Control: max-age=600` on HTML, so an ordinary fetch is
 *    free to answer from the browser's own cache for ten minutes. Inside that
 *    window a deploy produces exactly the failure described above. Page
 *    requests are therefore issued with `cache: 'reload'`, which goes past the
 *    browser cache and refreshes it on the way through.
 *
 * 3. Nothing that is not a healthy response may be stored. Writing a 404 or a
 *    504 into the cache turns one bad moment on a train into a permanent
 *    failure, because the next read is a hit and the network is never asked
 *    again.
 *
 * Bump CACHE_VERSION whenever these rules change, so that activation has an
 * old cache to remove and every reader starts from a known state.
 */
const CACHE_VERSION = 'v3';
const PAGE_CACHE = `amey-arc-pages-${CACHE_VERSION}`;
const ASSET_CACHE = `amey-arc-assets-${CACHE_VERSION}`;
const CURRENT = [PAGE_CACHE, ASSET_CACHE];

/* Offline fallbacks. Seeded on install, refreshed on every visit. */
const PAGES_TO_CACHE = [
    '/',
    '/archives/',
    '/search/',
    '/tags/',
    '/connect/'
];

const ASSETS_TO_CACHE = [
    '/pwa_icon_192.png',
    '/pwa_icon_512.png',
    '/favicon_balloon.ico',
    '/site.webmanifest'
];

/*
 * A file name carrying a long hexadecimal hash cannot change without changing
 * its address, so it is safe to serve from the cache forever. Anything else,
 * the search index above all, has a fixed address and new contents on every
 * publication, and must be allowed to refresh itself.
 */
const FINGERPRINTED = /\.[0-9a-f]{20,}\.(css|js)$/i;

/* A response worth keeping: our own origin, complete, and not an error page. */
function storable(response) {
    return response && response.ok && response.type === 'basic';
}

/* Installation: seed both caches, tolerating anything that will not fetch. */
self.addEventListener('install', (event) => {
    event.waitUntil((async () => {
        const [pages, assets] = await Promise.all([
            caches.open(PAGE_CACHE),
            caches.open(ASSET_CACHE)
        ]);
        const seed = async (cache, url) => {
            try {
                const response = await fetch(url, { cache: 'reload' });
                if (storable(response)) await cache.put(url, response);
            } catch (e) {
                /* An asset that will not fetch during install is not fatal. */
            }
        };
        await Promise.all([
            ...PAGES_TO_CACHE.map((u) => seed(pages, u)),
            ...ASSETS_TO_CACHE.map((u) => seed(assets, u))
        ]);
        await self.skipWaiting();
    })());
});

/* Activation: drop every cache this version does not own. */
self.addEventListener('activate', (event) => {
    event.waitUntil((async () => {
        const names = await caches.keys();
        await Promise.all(
            names
                .filter((n) => n.startsWith('amey-arc-') && !CURRENT.includes(n))
                .map((n) => caches.delete(n))
        );
        await self.clients.claim();
    })());
});

/*
 * A navigation cannot be answered with a response that followed a redirect,
 * so the body is repackaged into a plain response of our own. Rebuilding it
 * here is what allows `/connect` to reach `/connect/` through the worker.
 */
function flatten(response) {
    if (!response.redirected) return response;
    return new Response(response.body, {
        status: response.status,
        statusText: response.statusText,
        headers: response.headers
    });
}

/* Pages: the network decides, the cache is only there for when it cannot. */
async function handlePage(request) {
    try {
        const fresh = await fetch(new Request(request.url, {
            cache: 'reload',
            credentials: 'same-origin',
            redirect: 'follow'
        }));
        if (storable(fresh)) {
            const cache = await caches.open(PAGE_CACHE);
            cache.put(request.url, fresh.clone());
        }
        return flatten(fresh);
    } catch (e) {
        const cached = await caches.match(request.url, { cacheName: PAGE_CACHE });
        return cached ||
            (await caches.match('/', { cacheName: PAGE_CACHE })) ||
            new Response(
                '<!doctype html><meta charset="utf-8"><title>Offline</title>' +
                '<p style="font:16px/1.6 system-ui;margin:3rem auto;max-width:32rem">' +
                'This page is not available offline. It will load again once you ' +
                'have a connection.</p>',
                { status: 503, headers: { 'Content-Type': 'text/html; charset=utf-8' } }
            );
    }
}

/* Assets: instant from the cache, and quietly brought up to date behind it. */
async function handleAsset(request, immutable) {
    const cache = await caches.open(ASSET_CACHE);
    const cached = await cache.match(request);

    /* Its address contains its own hash, so a hit can never be out of date. */
    if (cached && immutable) return cached;

    const update = fetch(request).then((fresh) => {
        if (storable(fresh)) cache.put(request, fresh.clone());
        return fresh;
    });

    if (cached) {
        update.catch(() => {});
        return cached;
    }
    return update;
}

self.addEventListener('fetch', (event) => {
    const request = event.request;
    if (request.method !== 'GET') return;

    let url;
    try {
        url = new URL(request.url);
    } catch (e) {
        return;
    }
    if (url.origin !== self.location.origin) return;

    const isPage = request.mode === 'navigate' ||
        (request.headers.get('accept') || '').includes('text/html');

    event.respondWith(
        isPage
            ? handlePage(request)
            : handleAsset(request, FINGERPRINTED.test(url.pathname))
    );
});
