/* ─────────────────────────────────────────────────────
 * EF POEM LIKES — public engagement metric
 * 
 * Behavior:
 *   - Anonymous users can like a poem (no login required)
 *   - One like per browser (tracked via localStorage)
 *   - Counter shows only when >= 2 likes (server decides)
 *   - Uses window.efToast for feedback
 *
 * Server response shape:
 *   { ok: true, likes: <int>, show_count: <bool> }
 * ─────────────────────────────────────────────────── */
(function () {
  'use strict';

  const buttons = document.querySelectorAll('[data-poem-like]');
  if (!buttons.length) return;

  function getCsrfToken() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  function markAsLiked(btn) {
    btn.classList.add('is-liked');
    btn.disabled = true;
    btn.setAttribute('aria-label', 'You already liked this poem');
  }

  function updateCounter(btn, likes, showCount) {
    const display = btn.querySelector('[data-likes-display]');
    if (!display) return;
    display.textContent = likes;
    if (showCount) {
      display.removeAttribute('hidden');
    } else {
      display.setAttribute('hidden', '');
    }
  }

  buttons.forEach(function (btn) {
    const slug = btn.dataset.poemSlug;
    const url = btn.dataset.likesUrl;
    const likedKey = 'poem_liked_' + slug;

    // If already liked in this browser, disable from the start.
    if (localStorage.getItem(likedKey)) {
      markAsLiked(btn);
      return;
    }

    btn.addEventListener('click', async function (e) {
      e.preventDefault();
      btn.disabled = true;

      try {
        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCsrfToken(),
          },
          credentials: 'same-origin',
        });

        if (!response.ok) throw new Error('HTTP ' + response.status);

        const data = await response.json();
        if (!data.ok) throw new Error('Server rejected like');

        localStorage.setItem(likedKey, '1');
        markAsLiked(btn);
        updateCounter(btn, data.likes, data.show_count);

        if (window.efToast) {
          window.efToast('Thanks for the like!', 'success');
        }
      } catch (err) {
        btn.disabled = false;
        if (window.efToast) {
          window.efToast('Could not register your like. Try again?', 'error');
        }
      }
    });
  });
})();
