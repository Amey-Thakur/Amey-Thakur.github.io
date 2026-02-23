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

const CACHE_NAME = 'amey-arc-cache-v1';
const ASSETS_TO_CACHE = [
    '/',
    '/archives/',
    '/search/',
    '/tags/',
    '/connect/',
    '/favicon_balloon.ico',
    '/site.webmanifest'
];

/* Installation Event: Lifecycle initialization and primary asset caching. */
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(ASSETS_TO_CACHE);
        })
    );
});

/* Activation Event: Cache purge the technical debt of legacy versions. */
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((cacheName) => {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});

/* Fetch Orchestration: Intercepting network requests for offline resilience. */
self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});
