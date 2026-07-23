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
  if (form) try { form.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch (e) {}
})();

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
        show('Those photos total ' + mb + ' MB, over the 10 MB limit. Remove or compress a few and try again, or email them to Info@AndersonTechSupport.com.', true);
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
        show('Thanks. Your message is on its way. Prefer to talk now? Call (480) 287-4190.', false);
        form.reset();
      } else {
        show('Something went wrong sending that. Please email Info@AndersonTechSupport.com or call (480) 287-4190.', true);
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
