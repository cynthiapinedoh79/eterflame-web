/* ============================================================
   account-login.js
   Restyles the social login buttons (icon + label layout).
   ============================================================ */
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.socialaccount_providers li a').forEach(function (btn) {
      var img = btn.querySelector('img');
      var text = btn.textContent.trim()
        .replace('Continue with ', '')
        .replace('continue with ', '');
      btn.innerHTML = '';
      if (img) btn.appendChild(img);
      var span = document.createElement('span');
      span.textContent = text;
      btn.appendChild(span);
    });
  });
})();
