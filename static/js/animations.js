(function () {
  'use strict';

  // Scroll fade-in via IntersectionObserver
  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          observer.unobserve(e.target);
        }
      });
    },
    { threshold: 0.12 }
  );

  document.querySelectorAll('.fade-in-up').forEach(function (el) {
    observer.observe(el);
  });

  // Subtle parallax — desktop only, passive scroll listener
  var heroes = document.querySelectorAll('.parallax-hero');
  if (heroes.length && window.innerWidth > 768) {
    window.addEventListener('scroll', function () {
      var y = window.scrollY;
      heroes.forEach(function (h) {
        h.style.backgroundPositionY = 'calc(50% + ' + (y * 0.25) + 'px)';
      });
    }, { passive: true });
  }
})();
