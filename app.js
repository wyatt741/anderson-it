// Mobile menu
const burger = document.querySelector('.burger');
const menu = document.getElementById('mobile-menu');
if (burger) {
  burger.setAttribute('aria-label', 'Menu');
  burger.setAttribute('aria-expanded', 'false');
  const toggle = (open) => {
    document.body.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  };
  burger.addEventListener('click', () => toggle(!document.body.classList.contains('menu-open')));
  menu && menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => toggle(false)));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') toggle(false); });
}

// Scroll reveals
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Contact form: prefill service from ?service= query
const svc = new URLSearchParams(location.search).get('service');
if (svc) {
  const sel = document.getElementById('service');
  if (sel) [...sel.options].forEach(o => { if (o.value.toLowerCase() === svc.toLowerCase()) sel.value = o.value; });
}

// Theme toggle (light default; respects OS on first visit, then persists)
document.querySelectorAll('.theme-toggle').forEach(btn => {
  btn.addEventListener('click', () => {
    const dark = document.documentElement.getAttribute('data-theme') === 'dark';
    const next = dark ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch(e){}
  });
});
