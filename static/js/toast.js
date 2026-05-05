/* ── EF TOAST SYSTEM — auto-dismiss + manual close ──
 * Reads server-rendered toasts from base.html and:
 *   1. Auto-dismisses each after 6s
 *   2. Allows manual close via the × button
 *   3. Animates out smoothly before removing from DOM
 * No dependencies. Runs once on DOMContentLoaded.
 */
(function () {
  'use strict';

  const AUTO_DISMISS_MS = 6000;
  const ANIMATION_OUT_MS = 260;

  function dismiss(toast, timer) {
    if (timer) clearTimeout(timer);
    toast.classList.add('is-leaving');
    setTimeout(function () {
      if (toast.parentNode) toast.parentNode.removeChild(toast);
      // Si el stack queda vacío, ocultarlo (cleaner DOM)
      const stack = document.querySelector('.ef-toast-stack');
      if (stack && stack.children.length === 0) {
        stack.parentNode.removeChild(stack);
      }
    }, ANIMATION_OUT_MS);
  }

  function initToast(toast) {
    const closeBtn = toast.querySelector('.ef-toast__close');
    const timer = setTimeout(function () {
      dismiss(toast, null);
    }, AUTO_DISMISS_MS);

    if (closeBtn) {
      closeBtn.addEventListener('click', function () {
        dismiss(toast, timer);
      });
    }
  }

  function init() {
    const toasts = document.querySelectorAll('.ef-toast[data-toast]');
    toasts.forEach(initToast);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
