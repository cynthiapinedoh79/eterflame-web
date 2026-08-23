/* ============================================================
   works-contact.js
   Dynamic service selector for the Works contact form.
   ============================================================ */
(function () {
  var services = {
    design: ['Brand Identity', 'Art Direction', 'Graphic Design', 'Websites & Digital Experiences', 'Data & Intelligence'],
    media:  ['Photography', 'Video Production', 'Social Media', 'Podcast Production', 'Content Strategy', 'Digital Campaigns'],
    studio: ['Creative Writing', 'Copywriting', 'Ghostwriting', 'Brand Voice', 'Editorial Development', 'Books & Publications'],
    music:  ['Distribution', 'Music Publishing', 'Promotion & Marketing', 'Sync Licensing', 'Artist Development'],
    other:  ['Other']
  };

  function updateServices(division) {
    var wrapper = document.getElementById('service-wrapper');
    var select  = document.getElementById('service');
    if (!wrapper || !select) return;
    select.innerHTML = '<option value="">Select a service...</option>';
    if (!division || division === 'other' || !services[division]) {
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