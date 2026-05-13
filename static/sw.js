/**
 * Eterflame Works — Service Worker
 * Strategy: network-first with cache fallback.
 * Caches static assets and visited pages for offline use.
 */

const CACHE_NAME = 'eterflame-v1';
const STATIC_ASSETS = [
  '/',
  '/static/css/works.css',
  '/static/css/design.css',
  '/static/images/ef_logo.webp',
  '/static/images/icon-192.png',
  '/static/images/icon-512.png',
];

// Install: pre-cache static assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS).catch((err) => {
        console.warn('[SW] Some assets failed to pre-cache:', err);
      });
    })
  );
  self.skipWaiting();
});

// Activate: clean old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((names) =>
      Promise.all(
        names.filter((n) => n !== CACHE_NAME).map((n) => caches.delete(n))
      )
    )
  );
  self.clients.claim();
});

// Fetch: network-first, cache fallback
self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;
  
  // Skip non-http(s) requests (extensions, etc.)
  if (!event.request.url.startsWith('http')) return;
  
  // Skip admin pages — always fresh
  if (event.request.url.includes('/admin/')) return;

  event.respondWith(
    fetch(event.request)
      .then((response) => {
        // Cache successful GET responses
        if (response.ok) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return response;
      })
      .catch(() => {
        // Network failed — try cache
        return caches.match(event.request).then((cached) => {
          if (cached) return cached;
          // No cache match — return basic offline message for navigation
          if (event.request.mode === 'navigate') {
            return new Response(
              '<h1>Offline</h1><p>This page is not available offline yet. Please reconnect.</p>',
              { headers: { 'Content-Type': 'text/html' }, status: 503 }
            );
          }
        });
      })
  );
});
