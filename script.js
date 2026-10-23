'use strict';
(() => {
  const button = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#nav-menu');
  if (!button || !nav) return;
  const closeMenu = () => {
    button.setAttribute('aria-expanded', 'false');
    button.setAttribute('aria-label', '메뉴 열기');
    nav.classList.remove('is-open');
  };
  button.addEventListener('click', () => {
    const next = button.getAttribute('aria-expanded') !== 'true';
    button.setAttribute('aria-expanded', String(next));
    button.setAttribute('aria-label', next ? '메뉴 닫기' : '메뉴 열기');
    nav.classList.toggle('is-open', next);
  });
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });
  window.matchMedia('(min-width: 981px)').addEventListener('change', closeMenu);
})();
