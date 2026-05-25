/* ============================================================
   base-init.js
   Initialization scripts shared across all pages (base.html).
   Moved out of inline <script> tags so the Content-Security-Policy
   can drop 'unsafe-inline' (B2 / Fase 4).
   ============================================================ */

/* --- Sticky navbar: toggle 'scrolled' class on scroll --- */
(function () {
  var nav = document.querySelector('.ef-navbar-sticky');
  if (!nav) return;
  window.addEventListener('scroll', function () {
    nav.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });
})();

/* --- Back to top: visibility toggle on scroll --- */
(function () {
  var btn = document.querySelector('[data-back-to-top]');
  if (!btn) return;
  var SCROLL_THRESHOLD = 400;
  function toggleVisibility() {
    btn.classList.toggle('is-visible', window.scrollY > SCROLL_THRESHOLD);
  }
  window.addEventListener('scroll', toggleVisibility, { passive: true });
  toggleVisibility();
})();

/* --- GA4 custom event tracking --- */
(function () {
  if (typeof gtag !== 'function') return;

  // 1. Contact form submit
  var contactForm = document.querySelector('form[action*="contact"]');
  if (contactForm) {
    contactForm.addEventListener('submit', function () {
      gtag('event', 'contact_form_submit', {
        event_category: 'conversion',
        event_label: 'Contact Form'
      });
    });
  }

  // 2. Start a Project CTA clicks
  document.querySelectorAll('a[href*="contact"]').forEach(function (el) {
    el.addEventListener('click', function () {
      gtag('event', 'cta_start_project_click', {
        event_category: 'engagement',
        event_label: el.textContent.trim().substring(0, 50)
      });
    });
  });

  // 3. Service card clicks
  document.querySelectorAll('.wh-div-card, .ed-card, .ef-pw-card').forEach(function (el) {
    el.addEventListener('click', function () {
      gtag('event', 'service_card_click', {
        event_category: 'engagement',
        event_label: el.querySelector('h2,h3,h4')?.textContent.trim().substring(0, 50) || 'unknown'
      });
    });
  });

  // 4. Song play clicks
  document.querySelectorAll('audio, .song-play, [class*="play"]').forEach(function (el) {
    el.addEventListener('click', function () {
      gtag('event', 'song_play_click', {
        event_category: 'media',
        event_label: document.title
      });
    });
  });

  // 5. Shop product clicks
  document.querySelectorAll('.shop-product, [href*="shop"], [class*="product"]').forEach(function (el) {
    el.addEventListener('click', function () {
      gtag('event', 'shop_product_click', {
        event_category: 'ecommerce',
        event_label: el.textContent.trim().substring(0, 50)
      });
    });
  });

  // 6. Favorite poem clicks
  document.querySelectorAll('.poem-favorite, [class*="favorite"], [class*="like"]').forEach(function (el) {
    el.addEventListener('click', function () {
      gtag('event', 'favorite_poem_click', {
        event_category: 'engagement',
        event_label: document.title
      });
    });
  });

  // 7. Lead magnet form submit (blog)
  var leadForm = document.querySelector('.ef-lead-form');
  if (leadForm) {
    leadForm.addEventListener('submit', function () {
      gtag('event', 'lead_magnet_submit', {
        event_category: 'conversion',
        event_label: 'Branding Guide 2026'
      });
    });
  }

  // 8. Portfolio card clicks
  document.querySelectorAll('.ef-pw-card').forEach(function (el) {
    el.addEventListener('click', function () {
      gtag('event', 'portfolio_card_click', {
        event_category: 'engagement',
        event_label: el.querySelector('.ef-pw-title')?.textContent.trim() || 'unknown'
      });
    });
  });

  // 9. FAQ accordion opens
  document.querySelectorAll('.ef-faq__item').forEach(function (el) {
    el.addEventListener('toggle', function () {
      if (el.open) {
        gtag('event', 'faq_question_open', {
          event_category: 'engagement',
          event_label: el.querySelector('.ef-faq__question')?.textContent.trim().substring(0, 80) || 'unknown'
        });
      }
    });
  });
})();

