/* ============================================================
   account-signup.js
   Client-side password match validation on the signup form.
   ============================================================ */
(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('signup_form');
    var pw1  = document.getElementById('id_password1');
    var pw2  = document.getElementById('id_password2');

    if (!form || !pw1 || !pw2) return;

    function validatePasswords() {
      pw2.setCustomValidity('');
      if (pw1.value && pw2.value && pw1.value !== pw2.value) {
        pw2.setCustomValidity('Passwords do not match.');
      }
    }

    pw1.addEventListener('input', validatePasswords);
    pw2.addEventListener('input', validatePasswords);

    form.addEventListener('submit', function (e) {
      validatePasswords();
      if (!form.checkValidity()) {
        e.preventDefault();
        pw2.reportValidity();
      }
    });
  });
})();