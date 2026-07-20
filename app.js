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

// Contact form: attach photos, stay on page (hidden-iframe target), size guard, inline status
(function(){
  var form = document.getElementById('contact-form');
  if (!form) return;
  var iframe = document.getElementById('fs_iframe');
  var statusEl = document.getElementById('form-status');
  var fileInput = document.getElementById('photos');
  var MAX = 10 * 1024 * 1024;      // FormSubmit hard cap: 10MB total
  var MARGIN = 400 * 1024;         // leave room for the text fields + encoding
  var submitting = false;

  function show(msg, isErr){
    statusEl.hidden = false;
    statusEl.textContent = msg;
    statusEl.classList.toggle('err', !!isErr);
    try { statusEl.scrollIntoView({behavior:'smooth', block:'center'}); } catch(e){}
  }

  form.addEventListener('submit', function(e){
    if (fileInput && fileInput.files && fileInput.files.length){
      var total = 0;
      for (var i=0;i<fileInput.files.length;i++) total += fileInput.files[i].size;
      if (total > MAX - MARGIN){
        e.preventDefault();
        var mb = (total/1048576).toFixed(1);
        show('Those photos total ' + mb + ' MB, over the 10 MB limit. Remove or compress a few and try again, or email them to info@andersontechsupport.com.', true);
        return;
      }
    }
    submitting = true;
    show('Sending your message...', false);
  });

  if (iframe){
    iframe.addEventListener('load', function(){
      if (!submitting) return;            // ignore the initial (empty) iframe load
      submitting = false;
      var ok = true;
      try { ok = /thanks/i.test(iframe.contentWindow.location.pathname); }
      catch (err) { ok = true; }          // cross-origin = FormSubmit queued it (pre-activation or its own thanks page)
      if (ok){
        show('Thanks. Your message is on its way and we reply within one business day. Prefer to talk now? Call (480) 287-4190.', false);
        form.reset();
      } else {
        show('Something went wrong sending that. Please email info@andersontechsupport.com or call (480) 287-4190.', true);
      }
    });
  }
})();
