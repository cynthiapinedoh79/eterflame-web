/* ============================================================
   works-contact.js
   Dynamic service selector for the Works contact form.
   ============================================================ */
(function () {
  var services = {
    design: ['Web Development', 'UI/UX Design', 'Branding', 'E-commerce', 'Data Visualization', 'API Integration'],
    media:  ['Photography', 'Video Production', 'Podcast Production', 'Content Strategy'],
    studio: ['Copywriting', 'Ghostwriting', 'Brand Voice', 'Creative Writing'],
    other:  ['Other']
  };

  function updateServices(division) {
    var wrapper = document.getElementById('service-wrapper');
    var select  = document.getElementById('service');
    if (!wrapper || !select) return;
    select.innerHTML = '<option value="">Select a service...</option>';
    if (!division || division === 'other') {
      wrapper.style.display = 'none';
      return;
    }
    services[division].forEach(function (s) {
      var opt = document.createElement('option');
      opt.value = division.toUpperCase() + ' — ' + s;
      opt.textContent = s;
      select.appendChild(opt);
    });
    wrapper.style.display = 'block';
  }

  document.addEventListener('DOMContentLoaded', function () {
    var divisionSelect = document.getElementById('division');
    if (!divisionSelect) return;
    divisionSelect.addEventListener('change', function () {
      updateServices(this.value);
    });
  });
})();