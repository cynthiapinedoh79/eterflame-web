/* ── EF TOAST SYSTEM — auto-dismiss + manual close + programmatic API ──
 * 1. Auto-reads server-rendered toasts from base.html (Django messages)
 * 2. Auto-dismisses each after 6s
 * 3. Allows manual close via the × button
 * 4. Exposes window.efToast(message, type) for AJAX-driven toasts
 *
 * Types: 'success' | 'error' | 'warning' | 'info'
 *
 * Usage:
 *   window.efToast('Subscribed!', 'success');
 *   window.efToast('Network error', 'error');
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

  function ensureStack() {
    let stack = document.querySelector('.ef-toast-stack');
    if (!stack) {
      stack = document.createElement('div');
      stack.className = 'ef-toast-stack';
      stack.setAttribute('role', 'status');
      stack.setAttribute('aria-live', 'polite');
      document.body.appendChild(stack);
    }
    return stack;
  }

  function createToast(message, type) {
    const validTypes = ['success', 'error', 'warning', 'info'];
    const safeType = validTypes.includes(type) ? type : 'success';
    const icon = safeType === 'error' ? '✕' : '✓';

    const toast = document.createElement('div');
    toast.className = 'ef-toast ef-toast--' + safeType;
    toast.setAttribute('data-toast', '');

    toast.innerHTML =
      '<span class="ef-toast__icon" aria-hidden="true">' + icon + '</span>' +
      '<span class="ef-toast__msg"></span>' +
      '<button type="button" class="ef-toast__close" aria-label="Close">&times;</button>' +
      '<div class="ef-toast__progress" aria-hidden="true"></div>';

    // textContent prevents XSS
    toast.querySelector('.ef-toast__msg').textContent = message;

    return toast;
  }

  /**
   * Show a toast programmatically (for AJAX-driven forms).
   */
  window.efToast = function (message, type) {
    if (!message) return;
    const stack = ensureStack();
    const toast = createToast(message, type);
    stack.appendChild(toast);
    initToast(toast);
  };

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