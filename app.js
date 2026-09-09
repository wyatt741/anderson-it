const reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const scrollBehavior = reduceMotion ? 'auto' : 'smooth';

// Mobile menu
const burger = document.querySelector('.burger');
const menu = document.getElementById('mobile-menu');
if (burger && menu) {
  burger.setAttribute('aria-label', 'Menu');
  burger.setAttribute('aria-expanded', 'false');
  menu.setAttribute('aria-hidden', 'true');
  const pageRegions = [...document.querySelectorAll('main, footer, .cw')];
  const focusable = () => [...menu.querySelectorAll('a[href], button:not([disabled])')];
  const toggle = (open) => {
    const wasOpen = document.body.classList.contains('menu-open');
    document.body.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Menu');
    menu.setAttribute('aria-hidden', open ? 'false' : 'true');
    pageRegions.forEach(el => { el.inert = open; });
    if (open) requestAnimationFrame(() => { const first = focusable()[0]; if (first) first.focus(); });
    else if (wasOpen) burger.focus();
  };
  burger.addEventListener('click', () => toggle(!document.body.classList.contains('menu-open')));
  menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => toggle(false)));
  document.addEventListener('keydown', e => {
    if (!document.body.classList.contains('menu-open')) return;
    if (e.key === 'Escape') { e.preventDefault(); toggle(false); return; }
    if (e.key !== 'Tab') return;
    const items = focusable();
    if (!items.length) return;
    const first = items[0], last = items[items.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });
  window.matchMedia('(min-width: 601px)').addEventListener('change', e => { if (e.matches) toggle(false); });
}

// Scroll reveals
const reveals = document.querySelectorAll('.reveal');
if (reduceMotion || !('IntersectionObserver' in window)) reveals.forEach(el => el.classList.add('in'));
else {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
  reveals.forEach(el => io.observe(el));
}

// Contact form: prefill service from ?service= query
const svc = new URLSearchParams(location.search).get('service');
if (svc) {
  const sel = document.getElementById('service');
  if (sel) [...sel.options].forEach(o => { if (o.value.toLowerCase() === svc.toLowerCase()) sel.value = o.value; });
}

// Careers: salary-table rows link through to the contact form
document.querySelectorAll('.sal tbody tr[data-href]').forEach(tr => {
  tr.addEventListener('click', e => { if (!e.target.closest('a')) location.href = tr.getAttribute('data-href'); });
});

// Contact form: prefill when arriving from a job listing (?job=Role)
(function () {
  const job = new URLSearchParams(location.search).get('job');
  if (!job) return;
  const msg = document.getElementById('message');
  if (msg && !msg.value.trim()) msg.value = "I'd like to apply for the " + job + " position. Here's a bit about me:\n\n";
  const sel = document.getElementById('service');
  if (sel) { const o = document.createElement('option'); o.value = "Careers: " + job; o.textContent = "Careers: " + job; o.selected = true; sel.appendChild(o); }
  const form = document.getElementById('contact-form');
  if (form) try { form.scrollIntoView({ behavior: scrollBehavior, block: 'start' }); } catch (e) {}
})();

// Theme toggle. Dark is the default; a visitor's choice persists.
const themeButtons = document.querySelectorAll('.theme-toggle');
function syncThemeButtons() {
  const dark = document.documentElement.getAttribute('data-theme') === 'dark';
  themeButtons.forEach(btn => {
    const label = dark ? 'Switch to light mode' : 'Switch to dark mode';
    btn.setAttribute('aria-label', label);
    btn.setAttribute('aria-pressed', dark ? 'true' : 'false');
    btn.title = label;
  });
}
themeButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const dark = document.documentElement.getAttribute('data-theme') === 'dark';
    const next = dark ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch(e){}
    syncThemeButtons();
  });
});
syncThemeButtons();

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
  var confirmationTimer = null;
  var submitButton = form.querySelector('[type="submit"]');

  function show(msg, isErr){
    statusEl.hidden = false;
    statusEl.textContent = msg;
    statusEl.classList.toggle('err', !!isErr);
    try { statusEl.scrollIntoView({behavior:scrollBehavior, block:'center'}); } catch(e){}
  }

  function setPending(pending){
    submitting = pending;
    if (submitButton) submitButton.disabled = pending;
  }

  function finishSuccess(){
    clearTimeout(confirmationTimer);
    setPending(false);
    show('Thanks. Your message was sent. Need help now? Call or text Arizona at (480) 287-4190 or California at (805) 340-8055.', false);
    form.reset();
  }

  form.addEventListener('submit', function(e){
    if (fileInput && fileInput.files && fileInput.files.length){
      var total = 0;
      for (var i=0;i<fileInput.files.length;i++) total += fileInput.files[i].size;
      if (total > MAX - MARGIN){
        e.preventDefault();
        var mb = (total/1048576).toFixed(1);
        show('Those photos total ' + mb + ' MB, over the 10 MB limit. Remove or compress a few and try again, or email them to Info@AndersonTechSupport.com.', true);
        return;
      }
    }
    setPending(true);
    show('Sending your message...', false);
    clearTimeout(confirmationTimer);
    confirmationTimer = setTimeout(function(){
      if (!submitting) return;
      setPending(false);
      show("We couldn't confirm delivery. Your message is still here, so you can try again or call or text Arizona at (480) 287-4190 or California at (805) 340-8055.", true);
    }, 20000);
  });

  if (iframe){
    iframe.addEventListener('load', function(){
      if (!submitting) return;            // ignore the initial (empty) iframe load
      try {
        var loc = iframe.contentWindow.location;
        if (loc.origin === window.location.origin && /\/thanks\.html$/i.test(loc.pathname)) finishSuccess();
      } catch (err) {
        // FormSubmit is still cross-origin. Wait for the configured same-origin thanks page.
      }
    });
  }
})();

// mailto links: copy the address + show a toast (many desktops have no mail handler, so a click does nothing otherwise)
(function(){
  function toast(msg){
    var t=document.getElementById('toast');
    if(!t){t=document.createElement('div');t.id='toast';t.className='toast';document.body.appendChild(t);}
    t.textContent=msg; t.classList.add('show');
    clearTimeout(t._h); t._h=setTimeout(function(){t.classList.remove('show');},1900);
  }
  document.querySelectorAll('a[href^="mailto:"]').forEach(function(a){
    a.addEventListener('click',function(){
      var addr=a.getAttribute('href').replace(/^mailto:/,'');
      if(navigator.clipboard&&navigator.clipboard.writeText){
        navigator.clipboard.writeText(addr).then(function(){toast('Email copied: '+addr);}).catch(function(){});
      }
    });
  });
})();
