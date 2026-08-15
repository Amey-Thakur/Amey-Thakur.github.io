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
  - persistent offline caching, resource synchronization, and intercepting 
  - network requests to ensure site availability in low-connectivity environments.
  -
  - HOW IT WORKS:
  - The orchestrator utilizes the Cache API to store critical site assets during 
  - the installation phase. It performs cache-first fetch strategies and 
  - identifies/purges legacy cache versions during activation to maintain 
  - architectural efficiency and resource integrity.
  -
  - TECH STACK:
  - - Service Worker API
  - - Cache Storage API
  - - Fetch Event Orchestration
  -
  - ============================================================================== */

/*
 * Two caches, because the two kinds of request want opposite strategies.
 *
 *   pages   Navigations and the shell. These change every time something is
 *           published, so they are network-first and fall back to the cache
 *           only when offline. The previous worker was cache-first for
 *           everything, which meant a reader who had visited once kept the
 *           page they saw that day and never received a correction or a new
 *           version of an article.
 *
 *   assets  Icons and the manifest. Effectively immutable, so cache-first,
 *           which is what keeps the site usable with no connection.
 *
 * CACHE_VERSION must be changed whenever the caching contract itself changes.
 * The name of the old cache is not enough on its own: the previous worker kept
 * one fixed name, so its activate step never had an old cache to delete.
 */
const CACHE_VERSION = 'v2';
const PAGE_CACHE = `amey-arc-pages-${CACHE_VERSION}`;
const ASSET_CACHE = `amey-arc-assets-${CACHE_VERSION}`;
const CURRENT = [PAGE_CACHE, ASSET_CACHE];

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

/* Installation: seed both caches, tolerating anything that will not fetch. */
self.addEventListener('install', (event) => {
    event.waitUntil((async () => {
        const pages = await caches.open(PAGE_CACHE);
        const assets = await caches.open(ASSET_CACHE);
        await Promise.all([
            ...PAGES_TO_CACHE.map((u) => pages.add(u).catch(() => {})),
            ...ASSETS_TO_CACHE.map((u) => assets.add(u).catch(() => {}))
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

/* Fetch: network-first for pages, cache-first for assets. */
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

    if (isPage) {
        event.respondWith((async () => {
            try {
                const fresh = await fetch(request);
                const cache = await caches.open(PAGE_CACHE);
                cache.put(request, fresh.clone());
                return fresh;
            } catch (e) {
                return (await caches.match(request)) || (await caches.match('/'));
            }
        })());
        return;
    }

    event.respondWith((async () => {
        const cached = await caches.match(request);
        if (cached) return cached;
        const fresh = await fetch(request);
        const cache = await caches.open(ASSET_CACHE);
        cache.put(request, fresh.clone());
        return fresh;
    })());
});
