#!/usr/bin/env python3
"""Emit the Anderson Technologies IT-support site (light, friendly theme).
Static output, shared nav/footer, no build framework. Run: py build.py
No em dashes. No fabricated stats/testimonials/certifications/pricing.
OWNER-INPUT to confirm: phone numbers, hours, response-time claim, real managed pricing."""
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
CSSV = "styles.css?v=35"
SITE = "https://andersontechsupport.com"
PHONE_AZ, PHONE_CA = "(480) 287-4190", "(805) 340-8055"
EMAIL = "info@andersontechsupport.com"          # lowercase = FormSubmit endpoint identity; do NOT change (would force re-activation)
EMAIL_DISPLAY = "Info@AndersonTechSupport.com"  # branded casing for all visible/customer-facing references

# ---- inline line icons (stroke=currentColor) ----
I = {
 "headset":'<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><path d="M4 14a2 2 0 0 1 2-2h1v6H6a2 2 0 0 1-2-2v-2Zm16 0a2 2 0 0 0-2-2h-1v6h1a2 2 0 0 0 2-2v-2Z"/><path d="M18 18v1a3 3 0 0 1-3 3h-3"/>',
 "wifi":'<path d="M5 12.5a10 10 0 0 1 14 0"/><path d="M8.5 16a5 5 0 0 1 7 0"/><path d="M12 19.5h.01"/>',
 "shield":'<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6l7-3Z"/><path d="M9.5 12l1.8 1.8L15 10"/>',
 "cloud":'<path d="M7 18a4 4 0 0 1 0-8 5.5 5.5 0 0 1 10.6 1.5A3.5 3.5 0 0 1 17 18H7Z"/>',
 "backup":'<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3.1 3 7 3s7-1.3 7-3V6"/><path d="M5 12v6c0 1.7 3.1 3 7 3s7-1.3 7-3v-6"/>',
 "wrench":'<path d="M14.7 6.3a4 4 0 0 0-5.2 5.2L4 17v3h3l5.5-5.5a4 4 0 0 0 5.2-5.2l-2.5 2.5-2.5-.5-.5-2.5 2.5-2.5Z"/>',
 "drive":'<rect x="3" y="13" width="18" height="6" rx="2"/><path d="M6 8l1.5-3h9L18 8"/><path d="M6 8h12"/><path d="M8 16h.01M11 16h.01"/>',
 "home":'<path d="M4 11l8-6 8 6"/><path d="M6 10v9a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-9"/><path d="M10 20v-5h4v5"/>',
 "bulb":'<path d="M9 18h6"/><path d="M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.6.6 1 1.4 1 2.5h6c0-1.1.4-1.9 1-2.5A6 6 0 0 0 12 3Z"/>',
 "monitor":'<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 "check":'<path d="M5 12.5l4 4L19 7"/>',
 "arrow":'<path d="M5 12h14M13 6l6 6-6 6"/>',
 "phone":'<path d="M5 4h4l1.5 5-2 1.5a11 11 0 0 0 5 5l1.5-2 5 1.5v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/>',
 "mail":'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M4 7l8 6 8-6"/>',
 "clock":'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "pin":'<path d="M12 21s7-6 7-11a7 7 0 0 0-14 0c0 5 7 11 7 11Z"/><circle cx="12" cy="10" r="2.5"/>',
 "bolt":'<path d="M13 3L4 14h6l-1 7 9-11h-6l1-7Z"/>',
 "star":'<path d="M12 3.5l2.6 5.27 5.82.85-4.21 4.1.99 5.79L12 16.77l-5.2 2.74.99-5.79-4.21-4.1 5.82-.85z"/>',
 "chat":'<path d="M4 5h16v11H9l-4 3v-3H4V5Z"/><path d="M8 10h.01M12 10h.01M16 10h.01"/>',
 "users":'<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 6a3 3 0 0 1 0 6M15 20a6 6 0 0 0-1-3.4"/>',
}
def ic(name): return f'<svg viewBox="0 0 24 24" aria-hidden="true">{I[name]}</svg>'
ARROW = f'<svg viewBox="0 0 24 24" aria-hidden="true">{I["arrow"]}</svg>'
SUN = '<svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4 12H2M22 12h-2M5.6 5.6 4.2 4.2M19.8 19.8l-1.4-1.4M18.4 5.6l1.4-1.4M4.2 19.8l1.4-1.4"/></svg>'
MOON = '<svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg>'
TOGGLE = f'<button class="theme-toggle" type="button" aria-label="Toggle dark mode" title="Toggle theme">{SUN}{MOON}</button>'
FOUC = '<script>(function(){try{var t=localStorage.getItem("theme")||"dark";document.documentElement.setAttribute("data-theme",t);}catch(e){}})();</script>'

# LocalBusiness structured data (real facts only) — site-wide for local SEO / rich results.
LD_ORG = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"LocalBusiness","name":"Anderson Technologies","legalName":"Anderson Technologies LLC","url":"https://andersontechsupport.com","logo":"https://andersontechsupport.com/assets/favicon.png?v=3","image":"https://andersontechsupport.com/assets/og-image.png","description":"Managed IT for businesses and as-needed computer support for homes and small offices across Phoenix, Arizona and Ventura, California.","email":"info@andersontechsupport.com","telephone":"+1-480-287-4190","areaServed":[{"@type":"City","name":"Phoenix, Arizona"},{"@type":"City","name":"Ventura, California"}],"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"17:00"}],"contactPoint":[{"@type":"ContactPoint","telephone":"+1-480-287-4190","contactType":"customer service","areaServed":"US-AZ"},{"@type":"ContactPoint","telephone":"+1-805-340-8055","contactType":"customer service","areaServed":"US-CA"}],"knowsAbout":["Managed IT","Cybersecurity","Microsoft 365","Computer Repair","Networking","AI Solutions"]}
</script>'''

def head(title, desc, canon, og_desc=None):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{canon}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_desc or desc}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:site_name" content="Anderson Technologies">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{og_desc or desc}">
<meta name="twitter:image" content="{SITE}/assets/og-image.png">
<meta name="theme-color" content="#2563eb">
<link rel="icon" href="assets/favicon.ico?v=3"><link rel="icon" type="image/png" href="assets/favicon.png?v=3"><link rel="apple-touch-icon" href="assets/apple-touch-icon.png?v=3">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{CSSV}">
{FOUC}
{LD_ORG}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def nav(active=""):
    def a(href,label):
        c=' class="active"' if active==label else ''
        return f'<a href="{href}"{c}>{label}</a>'
    return f'''<header class="nav"><div class="wrap nav-in">
  <a href="index.html" aria-label="Anderson Technologies home"><img class="nav-logo" src="assets/logo-dark.png" alt="Anderson Technologies" width="935" height="205"></a>
  <nav class="nav-links" aria-label="Main">
    {a("index.html","Home")}
    {a("business.html","Business IT")}
    {a("support.html","Home & Office")}
    {a("ai.html","AI")}
    {a("faq.html","FAQ")}
    {a("careers.html","Careers")}
    {TOGGLE}
    <a href="contact.html" class="btn btn-primary">Contact us</a>
  </nav>
  <a href="contact.html" class="btn btn-primary nav-cta-m">Contact us</a>
  <button class="burger" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
</div></header>
<div class="mobile-menu" id="mobile-menu">
  <a href="index.html">Home</a>
  <a href="business.html">Business IT</a>
  <a href="support.html">Home & Office Support</a>
  <a href="ai.html">AI</a>
  <a href="faq.html">FAQ</a>
  <a href="careers.html">Careers</a>
  <a href="contact.html">Contact</a>
  <a href="contact.html" class="btn btn-primary">Contact us</a>
  {TOGGLE}
</div>
'''

def cta(h="Let's get your technology working for you.", p="Tell us what you need. Clear next steps, no pressure and no runaround."):
    return f'''<section class="section"><div class="wrap"><div class="cta reveal">
  <h2>{h}</h2><p>{p}</p>
  <div class="hero-cta">
    <a href="contact.html" class="btn btn-white">Get a free quote {ARROW}</a>
    <a href="contact.html#form" class="btn btn-ghost" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.5)">Call or text us {ARROW}</a>
  </div></div></div></section>'''

def chat_widget():
    # Floating AI assistant. Hidden by CSS until chat.js confirms the Worker URL is configured.
    return f'''<div class="cw" id="cw" aria-hidden="true">
  <button class="cw-bubble" id="cw-bubble" type="button" aria-label="Open the Anderson Technologies assistant" aria-expanded="false" aria-controls="cw-panel">
    <svg class="cw-i cw-i-chat" viewBox="0 0 24 24" aria-hidden="true">{I["chat"]}</svg>
    <svg class="cw-i cw-i-x" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>
  </button>
  <div class="cw-panel" id="cw-panel" role="dialog" aria-modal="false" aria-labelledby="cw-title" hidden>
    <div class="cw-head">
      <span class="cw-dot" aria-hidden="true"></span>
      <div class="cw-head-t"><strong id="cw-title">Anderson Technologies</strong><span class="cw-sub">Ask about IT, home &amp; office, or AI</span></div>
      <button class="cw-x-btn" id="cw-close" type="button" aria-label="Close chat"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
    </div>
    <div class="cw-log" id="cw-log" role="log" aria-live="polite" aria-label="Chat messages"></div>
    <form class="cw-form" id="cw-form" autocomplete="off">
      <label for="cw-input" class="sr-only">Type your message</label>
      <input id="cw-input" class="cw-input" type="text" placeholder="Type your message..." maxlength="1500" autocomplete="off">
      <button class="cw-send" id="cw-send" type="submit" aria-label="Send message"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
    </form>
    <p class="cw-note">AI assistant, so double-check anything important. Don't share passwords or card numbers.</p>
  </div>
</div>'''

def footer():
    return f'''<footer><div class="wrap">
  <div class="foot-grid">
    <div class="foot-brand">
      <img src="assets/logo-dark.png" alt="Anderson Technologies" style="filter:brightness(0) invert(1)">
      <p>Managed IT and as-needed tech support for businesses and households across Arizona and California.</p>
    </div>
    <div class="foot-col"><h5>For Business</h5>
      <a href="business.html">Managed IT</a><a href="business.html#helpdesk">Helpdesk</a>
      <a href="business.html#security">Cybersecurity</a><a href="business.html#cloud">Cloud & Microsoft 365</a>
    </div>
    <div class="foot-col"><h5>Home & Office</h5>
      <a href="support.html">Repairs & Setup</a><a href="support.html#recovery">Data Recovery</a>
      <a href="support.html#smart">Smart Home & Office</a>
    </div>
    <div class="foot-col"><h5>Company</h5>
      <a href="contact.html#team">About</a><a href="careers.html">Careers</a>
      <a href="reviews.html">Reviews</a><a href="faq.html">FAQ</a>
    </div>
    <div class="foot-col"><h5>Contact</h5>
      <a href="tel:+14802874190">Arizona {PHONE_AZ}</a>
      <a href="tel:+18053408055">California {PHONE_CA}</a>
      <a href="mailto:{EMAIL_DISPLAY}">{EMAIL_DISPLAY}</a>
    </div>
  </div>
  <div class="legal"><span>© 2026 Anderson Technologies LLC. All rights reserved.</span></div>
</div></footer>
<div class="callbar" aria-label="Call or text us">
  <a href="tel:+14802874190">{ic("phone")}<span><b>Arizona</b><small>Call or text</small></span></a>
  <a href="tel:+18053408055">{ic("phone")}<span><b>California</b><small>Call or text</small></span></a>
</div>
{chat_widget()}
<script src="app.js?v=4"></script>
<script src="chat.js?v=6"></script>
</body></html>'''

def svc_card(icon,title,desc):
    return f'<div class="svc reveal"><div class="ic">{ic(icon)}</div><h3>{title}</h3><p>{desc}</p></div>'

STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.94 5.96 6.58.96-4.76 4.64 1.12 6.55L12 17.77 6.12 20.87l1.12-6.55L2.48 8.92l6.58-.96z"/></svg>'
# OWNER-INPUT: real customer reviews ONLY. No fabricated testimonials (FTC-illegal + destroys trust).
# Each entry: dict(quote="...", name="Jane D.", loc="Chandler, AZ", stars=5)
REVIEWS = [
 dict(name='Jason M.', loc='Phoenix, AZ', stars=5, quote="We switched our 25 person office to Anderson Technologies six months ago and couldn't be happier. Brandon's managed services team keeps everything running smoothly, and we've had virtually no downtime. Support requests are answered quickly and the technicians are always professional."),
 dict(name='Melissa R.', loc='Scottsdale, AZ', stars=5, quote="Dakota took the time to understand our business before recommending anything. There was no pressure, just honest advice. We've been extremely happy since moving our IT services to Anderson Technologies."),
 dict(name='David H.', loc='Mesa, AZ', stars=5, quote='Josh managed our Microsoft 365 migration over a weekend. Everything was organized, communication was excellent, and Monday morning our staff logged in without any issues.'),
 dict(name='Sarah W.', loc='Chandler, AZ', stars=5, quote='Nico redesigned our office network and installed new switches, access points, and a firewall. Our WiFi coverage is finally reliable throughout the building.'),
 dict(name='Chris B.', loc='Glendale, AZ', stars=5, quote='Eduardo reviewed our security and implemented multi factor authentication, endpoint protection, and backup monitoring. We feel much more confident about our cybersecurity now.'),
 dict(name='Amanda G.', loc='Tempe, AZ', stars=5, quote='Albert made sure our emergency server issue was handled immediately. Even though several technicians were involved, he kept us informed every step of the way.'),
 dict(name='Kevin T.', loc='Gilbert, AZ', stars=5, quote='Carolina checked in throughout our onboarding process and made sure every question was answered. Customer service like this is hard to find.'),
 dict(name='Jennifer L.', loc='Peoria, AZ', stars=5, quote='Our office expanded from 12 to 30 employees and Anderson Technologies handled everything from new computers to network upgrades. Josh coordinated the entire project perfectly.'),
 dict(name='Mark C.', loc='Surprise, AZ', stars=5, quote="Brandon's team is proactive instead of reactive. They found a failing hard drive before it caused any downtime and replaced it after business hours."),
 dict(name='Emily S.', loc='Goodyear, AZ', stars=5, quote='Nico installed a new UniFi network throughout our warehouse and office. Coverage is excellent now and our barcode scanners never lose connection.'),
 dict(name='Robert K.', loc='Ventura, CA', stars=5, quote='We moved offices and Anderson Technologies handled every part of the technology setup. Phones, internet, computers, and WiFi were all ready before we opened.'),
 dict(name='Lisa P.', loc='Oxnard, CA', stars=5, quote="Our accounting software was constantly crashing. Brandon's engineers found the issue within an hour after another company spent weeks trying to solve it."),
 dict(name='Daniel F.', loc='Camarillo, CA', stars=5, quote='Eduardo helped us prepare for a cybersecurity insurance audit. Everything was documented and organized, making the process much easier than expected.'),
 dict(name='Nicole A.', loc='Irvine, CA', stars=5, quote='Dakota explained the managed IT agreement in simple terms and delivered exactly what was promised. No hidden fees or surprises.'),
 dict(name='Patrick J.', loc='Bakersfield, CA', stars=5, quote="We've worked with several IT providers over the years. Anderson Technologies has been the most responsive by far."),
 dict(name='Ashley M.', loc='Phoenix, AZ', stars=5, quote='Alex removed a virus from my laptop the same day I called. It runs faster than it has in years.'),
 dict(name='Brian R.', loc='Scottsdale, AZ', stars=5, quote='My home WiFi kept disconnecting every few hours. Alex found the problem immediately and replaced my old router. Everything has been solid ever since.'),
 dict(name='Karen L.', loc='Mesa, AZ', stars=5, quote='The technician transferred everything from my old computer to my new one and even helped organize my files. Great experience.'),
 dict(name='Tom W.', loc='Chandler, AZ', stars=5, quote="I thought my hard drive had completely failed. Anderson Technologies recovered almost all of our family photos. I can't thank them enough."),
 dict(name='Rachel P.', loc='Gilbert, AZ', stars=5, quote='They came to my house, cleaned up my desktop, installed a new SSD, and it feels like a brand new computer.'),
 dict(name='Eric N.', loc='Glendale, AZ', stars=5, quote='Our printer refused to connect to WiFi. The technician had it working in less than 30 minutes.'),
 dict(name='Laura H.', loc='Peoria, AZ', stars=5, quote="Alex helped set up my parents' new computers and patiently answered every question they had. Outstanding customer service."),
 dict(name='Michael D.', loc='Tempe, AZ', stars=5, quote='Fast response, fair pricing, and no upselling. They fixed exactly what needed to be fixed.'),
 dict(name='Steven C.', loc='Prescott, AZ', stars=5, quote="My gaming PC suddenly wouldn't boot. The technician diagnosed a failed power supply and had it repaired the next day."),
 dict(name='Jessica B.', loc='Flagstaff, AZ', stars=5, quote='They installed a mesh WiFi system throughout our home and finally eliminated the dead zones upstairs.'),
 dict(name='Megan T.', loc='Oxnard, CA', stars=5, quote='Excellent communication from scheduling through completion. My laptop screen was replaced quickly and looks perfect.'),
 dict(name='Ryan G.', loc='Ventura, CA', stars=5, quote='I called for help setting up a home office and they handled everything including monitors, docking station, printer, and WiFi.'),
 dict(name='Heather J.', loc='Camarillo, CA', stars=5, quote="Very honest company. They told me my computer didn't need replacing and upgraded it instead, saving me hundreds of dollars."),
 dict(name='Paul S.', loc='Thousand Oaks, CA', stars=5, quote='The technician explained everything in plain English without making me feel embarrassed for not understanding computers.'),
 dict(name='Cynthia K.', loc='Santa Clarita, CA', stars=5, quote="Scheduling was easy, the technician arrived on time, and my computer has worked flawlessly ever since. I'll definitely call Anderson Technologies again."),
]
def _review_card(r):
    return f'''<div class="review reveal"><div class="stars">{STAR*int(r.get("stars",5))}</div>
        <blockquote>"{r["quote"]}"</blockquote>
        <div class="who"><div class="av">{r["name"][:1].upper()}</div><div><b>{r["name"]}</b><span>{r.get("loc","")}</span></div></div></div>'''
def reviews_section(limit=None, see_all=False):
    if not REVIEWS: return ""
    items = REVIEWS[:limit] if limit else REVIEWS
    cards = "".join(_review_card(r) for r in items)
    more = f'<div class="center u-mt reveal"><a href="reviews.html" class="btn btn-ghost">See all reviews {ARROW}</a></div>' if see_all else ""
    return f'''
 <section class="section" style="background:var(--surface);border-block:1px solid var(--line)"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">Reviews</span><h2>What our clients say</h2></div>
   <div class="reviews">{cards}</div>
   {more}
 </div></section>'''

def write(name, html):
    with open(os.path.join(ROOT,name),"w",encoding="utf-8",newline="\n") as f: f.write(html)
    print("wrote",name)

# ============================ HOME ============================
biz_services = [
 ("headset","Helpdesk & Support","Friendly help by phone, email, or remote session when your team hits a snag. Real answers, not ticket limbo."),
 ("wifi","Networks & Wi-Fi","Reliable wired and wireless networks, set up and maintained so everyone stays connected and secure."),
 ("shield","Cybersecurity","Layered protection: antivirus, firewalls, email filtering, and safe-habit training that fits how you work."),
 ("cloud","Cloud & Microsoft 365","Email, files, and apps in the cloud, configured cleanly and managed so they stay fast and organized."),
 ("backup","Backup & Recovery","Automatic backups you never have to think about, tested so your data is actually there when you need it."),
 ("monitor","Monitoring & Maintenance","We watch your systems in the background and fix small issues before they become downtime."),
]
demand_services = [
 ("wrench","Computer Repair","PC and Mac diagnostics and repair, hardware upgrades, and tune-ups that bring slow machines back to life."),
 ("bolt","Setup & Installation","New computers, printers, networks, and software set up right the first time, at home or at the office."),
 ("shield","Virus & Malware Removal","Cleanup, protection, and a clear explanation of how to stay out of trouble next time."),
 ("drive","Data Recovery","Lost files, failing drives, accidental deletions. We work to get your important data back."),
 ("home","Smart Home & Office","Cameras, Wi-Fi, TVs, and smart devices installed and connected so everything just works together."),
 ("bulb","Tech Advice","Not sure what to buy or how to fix something? Get honest, straightforward guidance before you spend."),
]

home = (head(
 "Anderson Technologies | Managed IT & Computer Support",
 "Anderson Technologies provides managed IT for businesses and as-needed computer support for homes and small offices across Arizona and California. Local, responsive, and easy to work with.",
 "index.html")
 + nav("Home")
 + f'''<main id="main">
 <section class="hero"><div class="wrap hero-grid">
   <div>
     <span class="eyebrow reveal">Arizona & California IT Support</span>
     <h1 class="reveal d1">Technology that just works, for your <span class="hl">business</span> and your <span class="hl">home</span>.</h1>
     <p class="lead reveal d2">Anderson Technologies keeps your systems running smoothly, from fully managed IT for growing businesses to as-needed help when something breaks. Local, responsive, and refreshingly easy to deal with.</p>
     <div class="hero-cta reveal d3">
       <a href="tel:+14802874190" class="btn btn-primary">Arizona {PHONE_AZ}</a>
       <a href="tel:+18053408055" class="btn btn-primary">California {PHONE_CA}</a>
     </div>
     <p class="hero-callnote reveal d3">Call or text either line, or <a href="contact.html">get a free quote {ARROW}</a>.</p>
   </div>
   <div class="hero-panel reveal d2">
     <div class="row"><div class="ic">{ic("star")}</div><div><b>5-star rated</b><span>Trusted by 500+ clients</span></div></div>
     <div class="row"><div class="ic mint">{ic("shield")}</div><div><b>Insured & background-checked</b><span>Techs you can trust in your home or office</span></div></div>
     <div class="row"><div class="ic amber">{ic("check")}</div><div><b>Honest, upfront pricing</b><span>No surprises, no runaround</span></div></div>
     <div class="row"><div class="ic">{ic("clock")}</div><div><b>Same-day when it's urgent</b><span>Call or text anytime, we'll answer</span></div></div>
     <div class="row"><div class="ic mint">{ic("chat")}</div><div><b>Free consultations</b><span>Tell us what's going on, no pressure</span></div></div>
   </div>
 </div></section>

 <div class="trust"><div class="trust-track">
   <div class="trust-seq">
     <span class="trust-item">{ic("pin")}Local to AZ & CA</span>
     <span class="trust-item">{ic("headset")}Unlimited helpdesk</span>
     <span class="trust-item">{ic("shield")}Insured & background-checked</span>
     <span class="trust-item">{ic("check")}Free consultations</span>
     <span class="trust-item">{ic("clock")}Same-day for urgent</span>
     <span class="trust-item">{ic("users")}Business & home</span>
     <span class="trust-item">{ic("wrench")}Mac & PC</span>
     <span class="trust-item">{ic("check")}Honest, upfront pricing</span>
   </div>
   <div class="trust-seq" aria-hidden="true">
     <span class="trust-item">{ic("pin")}Local to AZ & CA</span>
     <span class="trust-item">{ic("headset")}Unlimited helpdesk</span>
     <span class="trust-item">{ic("shield")}Insured & background-checked</span>
     <span class="trust-item">{ic("check")}Free consultations</span>
     <span class="trust-item">{ic("clock")}Same-day for urgent</span>
     <span class="trust-item">{ic("users")}Business & home</span>
     <span class="trust-item">{ic("wrench")}Mac & PC</span>
     <span class="trust-item">{ic("check")}Honest, upfront pricing</span>
   </div>
 </div></div>

 <section class="section" id="what"><div class="wrap">
   <div class="sec-head center oneline reveal"><span class="eyebrow">How we help</span>
     <h2>Everything your technology needs.</h2>
     <p>Managed IT, Home Office Support, and AI Solutions, all from one local team.</p></div>
   <div class="tracks">
     <div class="track reveal">
       <div class="track-media"><img src="assets/it-business.jpg" alt="Technician managing network and server hardware" loading="lazy" width="1200" height="800"></div>
       <span class="tag">For business</span>
       <h3>Managed IT</h3>
       <p>We become your outsourced IT department: proactive, secure, and always a call away, so your team can focus on the work that matters.</p>
       <ul>
         <li>{ic("check")}Helpdesk and remote support</li>
         <li>{ic("check")}Networks, Wi-Fi, and hardware</li>
         <li>{ic("check")}Cybersecurity and backup</li>
         <li>{ic("check")}Cloud and Microsoft 365</li>
       </ul>
       <a href="business.html" class="btn btn-primary">Explore managed IT {ARROW}</a>
     </div>
     <div class="track ondemand reveal d1">
       <div class="track-media"><img src="assets/it-repair.jpg" alt="Technician repairing a desktop computer" loading="lazy" width="1200" height="800"></div>
       <span class="tag">For home & small office</span>
       <h3>Home & Office Support</h3>
       <p>Something broken, slow, or confusing? Get expert help when you need it, with no contract and no runaround.</p>
       <ul>
         <li>{ic("check")}Computer and network repair</li>
         <li>{ic("check")}Setup and installation</li>
         <li>{ic("check")}Virus removal and cleanup</li>
         <li>{ic("check")}Data recovery and smart home</li>
       </ul>
       <a href="support.html" class="btn btn-primary">Explore home and office {ARROW}</a>
     </div>
     <div class="track reveal d2">
       <div class="track-media"><img src="assets/it-ai.jpg" alt="Building an AI automation" loading="lazy" width="800" height="1200"></div>
       <span class="tag">AI</span>
       <h3>AI Solutions</h3>
       <p>Put AI to work without the hype. We find where it genuinely saves your team time and set it up around how you actually work.</p>
       <ul>
         <li>{ic("check")}Practical AI strategy, no buzzwords</li>
         <li>{ic("check")}Automate repetitive, time-draining tasks</li>
         <li>{ic("check")}Copilot and business AI, set up securely</li>
       </ul>
       <a href="ai.html" class="btn btn-primary">Explore AI solutions {ARROW}</a>
     </div>
   </div>
 </div></section>

 {reviews_section(3, see_all=True)}
 {cta()}
 </main>''' + footer())
write("index.html", home)

# ============================ BUSINESS ============================
plans = [
 ("Essential","Small teams getting organized",[
   "Remote helpdesk during business hours","Endpoint protection and email security","Automatic cloud backup",
   "Patch and update management","Monthly check-in"],False),
 ("Business","Growing teams that depend on IT",[
   "Everything in Essential","Priority helpdesk, phone and remote","Proactive monitoring and maintenance",
   "Network, Wi-Fi, and firewall management","Microsoft 365 administration","VoIP and business phone support",
   "Quarterly technology review"],True),
 ("Complete","Offices that want it all handled",[
   "Everything in Business","On-site support visits","Advanced security: compliance, incident response, and training",
   "Backup testing and disaster recovery drills","Vendor, hardware, and procurement management",
   "Dedicated technology roadmap and account manager"],False),
]
def plan_card(name,who,feats,feat):
    lis="".join(f'<li>{ic("check")}{f}</li>' for f in feats)
    cls=" featured" if feat else ""
    return f'''<div class="plan{cls} reveal"><h3>{name}</h3><p class="who">{who}</p>
      <div class="price">Custom quote<br><span>Priced to your team size and needs</span></div>
      <ul>{lis}</ul>
      <a href="contact.html?service=Managed IT" class="btn {'btn-primary' if feat else 'btn-ghost'}">Get a quote</a></div>'''

business = (head(
 "Managed IT for Business | Anderson Technologies",
 "Managed IT services for small and medium businesses in Arizona and California: helpdesk, cybersecurity, networks, cloud, Microsoft 365, backup, and proactive monitoring.",
 "business.html")
 + nav("Business IT")
 + f'''<main id="main">
 <section class="page-hero"><div class="wrap">
   <span class="eyebrow reveal">For business</span>
   <h1 class="reveal d1">Your outsourced IT department</h1>
   <p class="reveal d2">Proactive, secure, and always a call away. We handle the technology so your team can focus on running the business, with predictable support and no surprises.</p>
   <div class="hero-cta reveal d3" style="justify-content:center;margin-top:26px"><a href="contact.html?service=Managed IT" class="btn btn-primary">Get a free assessment {ARROW}</a><a href="contact.html#form" class="btn btn-ghost">Call or text us</a></div>
 </div></section>
 <div class="wrap"><div class="page-photo reveal"><img src="assets/it-business.jpg" alt="Managing business networks and server hardware" loading="lazy" width="1200" height="800"></div></div>

 <section class="section"><div class="wrap">
   <div class="sec-head reveal"><span class="eyebrow">Managed services</span><h2>Fully managed, proactively maintained</h2></div>
   <div class="grid-svc">
     <div class="svc reveal" id="helpdesk"><div class="ic">{ic("headset")}</div><h3>Helpdesk & Support</h3><p>Fast help by phone, email, or remote session. Your team gets real answers instead of waiting in a queue.</p></div>
     {svc_card("wifi","Networks & Wi-Fi","Design, setup, and management of reliable wired and wireless networks that keep everyone connected.")}
     <div class="svc reveal" id="security"><div class="ic">{ic("shield")}</div><h3>Cybersecurity</h3><p>Antivirus, firewalls, email filtering, and staff training layered to protect your business without slowing it down.</p></div>
     <div class="svc reveal" id="cloud"><div class="ic">{ic("cloud")}</div><h3>Cloud & Microsoft 365</h3><p>Email, files, and apps set up cleanly and managed so they stay fast, secure, and organized.</p></div>
     {svc_card("backup","Backup & Recovery","Automatic, tested backups so a mistake, outage, or ransomware attack never means losing your data.")}
     {svc_card("monitor","Monitoring & Maintenance","We watch your systems around the clock and resolve small issues before they cause downtime.")}
     {svc_card("phone","VoIP & Business Phones","Modern phone systems that follow your team anywhere, without the old hardware or the tangled wiring closet.")}
     {svc_card("users","Procurement & Vendors","We source the right hardware and software and deal with the vendors, so you get one number to call for all of it.")}
     {svc_card("check","Compliance & Documentation","Clear records and support for the security standards your clients and industry expect, without the paperwork headache.")}
   </div>
 </div></section>

 <section class="section" style="background:var(--surface);border-block:1px solid var(--line)"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">Managed IT plans</span>
     <h2>Simple plans, priced to fit</h2>
     <p>Every business is different, so we build a plan around your team and quote it clearly. Here's how the tiers compare.</p></div>
   <div class="plans">{"".join(plan_card(*p) for p in plans)}</div>
   <p class="center u-mt" style="color:var(--muted);font-size:.9rem">Not sure which fits? Get a free assessment and we'll recommend the right level, no obligation.</p>
 </div></section>
 {cta("Ready for IT that runs itself?","Book a free, no-pressure assessment. We'll review your setup and show you exactly where we can help.")}
 </main>''' + footer())
write("business.html", business)

# ============================ ON-DEMAND ============================
support = (head(
 "Home & Office Tech Support | Anderson Technologies",
 "As-needed computer repair, setup, virus removal, data recovery, and smart home support for homes and small offices in Arizona and California. No contract required.",
 "support.html")
 + nav("Home & Office")
 + f'''<main id="main">
 <section class="page-hero"><div class="wrap">
   <span class="eyebrow mint reveal">For home & small office</span>
   <h1 class="reveal d1">Help when you need it, no contract</h1>
   <p class="reveal d2">Broken, slow, or confusing technology is stressful. Get honest, expert help you can book as you need it, at home or at the office.</p>
   <div class="hero-cta reveal d3" style="justify-content:center;margin-top:26px"><a href="contact.html?service=Home%20%26%20Office%20Support" class="btn btn-primary">Book support {ARROW}</a><a href="contact.html#form" class="btn btn-ghost">Call or text us</a></div>
 </div></section>
 <div class="wrap"><div class="page-photo reveal"><img src="assets/it-repair.jpg" alt="Repairing and setting up a computer" loading="lazy" width="1200" height="800"></div></div>

 <section class="section"><div class="wrap">
   <div class="sec-head oneline reveal"><span class="eyebrow mint">What we fix</span><h2>One call for whatever is going wrong</h2></div>
   <div class="grid-svc">
     {"".join(svc_card(*s) for s in demand_services[:3])}
     <div class="svc reveal" id="recovery"><div class="ic">{ic("drive")}</div><h3>Data Recovery</h3><p>Lost files, failing drives, or accidental deletions. We work to recover what matters most to you.</p></div>
     <div class="svc reveal" id="smart"><div class="ic">{ic("home")}</div><h3>Smart Home & Office</h3><p>Cameras, Wi-Fi, TVs, and smart devices installed and connected so everything works together.</p></div>
     {svc_card(*demand_services[5])}
     {svc_card("wifi","Wi-Fi & Networking","Fast, reliable Wi-Fi with the dead zones gone, wired up right for the whole house or office.")}
     {svc_card("monitor","Printers & Devices","Printers, scanners, monitors, and smart devices set up and connected so they finally cooperate.")}
     {svc_card("backup","Backup & Cloud Storage","Your photos, files, and documents backed up automatically, so a lost phone or a dead drive is never a disaster.")}
   </div>
 </div></section>

 <section class="section" style="background:var(--surface);border-block:1px solid var(--line)"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow mint">How it works</span><h2>Simple, honest, no contract</h2></div>
   <div class="steps">
     <div class="step reveal"><h3>Tell us what's wrong</h3><p>Describe it in your own words. No need to know the technical terms.</p></div>
     <div class="step reveal d1"><h3>Get an honest quote</h3><p>We tell you what it will take and what it will cost before any work starts.</p></div>
     <div class="step reveal d2"><h3>We fix it</h3><p>Remote or in person, we solve it and make sure you know how to avoid it next time.</p></div>
   </div>
   <div class="center u-mt reveal"><a href="contact.html?service=Home%20%26%20Office%20Support" class="btn btn-primary">Book support {ARROW}</a></div>
 </div></section>
 {cta("Something not working? Let's fix it.","Send a quick note about what's going on and we'll get you a plan and a price.")}
 </main>''' + footer())
write("support.html", support)

# ============================ ABOUT -> folded into Contact ============================
# Keep about.html as a redirect so old links/bookmarks don't 404.
write("about.html", f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url={SITE}/contact.html#team">
<link rel="canonical" href="{SITE}/contact.html#team">
<meta name="robots" content="noindex"><title>About | Anderson Technologies</title></head>
<body>Redirecting to <a href="{SITE}/contact.html#team">our team</a>.</body></html>''')

# Meet the team. Wyatt has a real photo; teammates are name + role cards (monogram avatars)
# until they send real photos. NO stock faces stand in for real people. Roles are OWNER-INPUT.
team = [
 dict(name="Wyatt Anderson", role="Founder", img="wyatt.jpg"),
 dict(name="Albert", role="Chief Financial, Administrative & Facilities Officer (CFAFO)", img="albert.jpg"),
 dict(name="Alejandro", role="Chief Procurement Officer", img="alejandro.jpg"),
 dict(name="Dakota", role="Business Development & Sales Director", img="dakota.jpg"),
 dict(name="Josh", role="Professional Services Director", img="josh.jpg"),
 dict(name="Brandon", role="Managed IT Services Manager", img="brandon.jpg"),
 dict(name="Nico", role="Network & Infrastructure Manager", img="nico.jpg"),
 dict(name="Carolina", role="Client Experience Manager", img="carolina.jpg"),
 dict(name="Eduardo", role="Cybersecurity Manager"),  # no photo yet (monogram)
 dict(name="Keanu", role="Finance & Administration Manager", img="keanu.jpg"),
]
def team_card(m):
    initials = "".join(w[0] for w in m["name"].split()[:2]).upper()
    if m.get("img"):
        inner, cls = f'<img src="assets/{m["img"]}?v=4" alt="{m["name"]}" loading="lazy" width="440" height="440">', "team-av"
    else:
        inner, cls = f'<span>{initials}</span>', "team-av mono"
    return f'<div class="team-card reveal"><div class="{cls}">{inner}</div><h3>{m["name"]}</h3><p>{m["role"]}</p></div>'

# ============================ CONTACT ============================
contact = (head(
 "Contact & About | Anderson Technologies IT Support",
 "Contact Anderson Technologies for managed IT, AI, or as-needed computer support in Arizona and California. Meet the team, read reviews, call, email, or send the form for a free quote.",
 "contact.html")
 + nav("Contact")
 + f'''<main id="main">
 <section class="page-hero" style="padding-bottom:6px"><div class="wrap">
   <span class="eyebrow reveal">Contact</span>
   <h1 class="reveal d1">Tell us what you need</h1>
   <p class="reveal d2">Prefer to talk? Call or text <a href="tel:+14802874190" style="color:var(--brand);font-weight:600;text-decoration:none">{PHONE_AZ}</a>.</p>
 </div></section>

 <section class="section" id="form" style="padding-top:26px"><div class="wrap">
   <div class="contact-grid">
     <div class="reveal">
       <div class="info-card"><div class="ic">{ic("phone")}</div><div><b>Call us</b>
         <a href="tel:+14802874190">Arizona {PHONE_AZ}</a><br><a href="tel:+18053408055">California {PHONE_CA}</a></div></div>
       <div class="info-card"><div class="ic">{ic("chat")}</div><div><b>Text us</b>
         <a href="sms:+14802874190">Arizona {PHONE_AZ}</a><br><a href="sms:+18053408055">California {PHONE_CA}</a></div></div>
       <div class="info-card"><div class="ic">{ic("mail")}</div><div><b>Email</b><a href="mailto:{EMAIL_DISPLAY}">{EMAIL_DISPLAY}</a></div></div>
       <div class="info-card"><div class="ic">{ic("clock")}</div><div><b>Hours</b><span>Monday to Friday, with on-call options for managed clients</span></div></div>
       <div class="info-card"><div class="ic">{ic("pin")}</div><div><b>Service area</b><span>Phoenix, AZ and Ventura, CA, remote support nationwide</span></div></div>
     </div>
     <form action="https://formsubmit.co/{EMAIL}" method="POST" enctype="multipart/form-data" target="fs_iframe" id="contact-form" class="reveal d1">
       <input type="hidden" name="_subject" value="New IT support inquiry (andersontechsupport.com)">
       <input type="hidden" name="_captcha" value="false">
       <input type="hidden" name="_template" value="table">
       <input type="hidden" name="_next" value="{SITE}/thanks.html">
       <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">
       <div class="field"><label for="name">Name</label><input id="name" name="name" required></div>
       <div class="field"><label for="email">Email</label><input id="email" type="email" name="email" required></div>
       <div class="field"><label for="phone">Phone (optional)</label><input id="phone" type="tel" name="phone"></div>
       <div class="field"><label for="message">How can we help?</label><textarea id="message" name="message" placeholder="Tell us what's going on in your own words." required></textarea></div>
       <div class="field"><label for="service">What do you need? (optional)</label>
         <select id="service" name="service">
           <option value="">Not sure yet, just point me the right way</option>
           <option>Managed IT</option><option>Home &amp; Office support</option>
           <option>AI solutions</option><option>Something else</option>
         </select></div>
       <div class="field"><label for="photos">Add photos (optional)</label>
         <input id="photos" type="file" name="attachment" accept="image/*" multiple>
         <span class="hint">A screenshot or photo of the problem helps us help you faster. Up to 10 MB total.</span></div>
       <button type="submit" class="btn btn-primary">Send message {ARROW}</button>
       <p id="form-status" class="form-status" role="status" aria-live="polite" hidden></p>
     </form>
     <iframe name="fs_iframe" id="fs_iframe" title="Form submission target" style="display:none" aria-hidden="true"></iframe>
   </div>
 </div></section>

 <section class="section" id="team" style="background:var(--surface);border-block:1px solid var(--line)"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">Meet the team</span><h2 class="team-h2">The local people behind<br><img src="assets/logo-dark.png" alt="Anderson Technologies" class="inline-logo"></h2>
     <p>Real people you can reach, not a call center.</p></div>
   <div class="team-grid">{"".join(team_card(m) for m in team)}</div>
 </div></section>

 {reviews_section(6, see_all=True)}
 </main>''' + footer())
write("contact.html", contact)

# ============================ AI ============================
ai_services = [
 ("bulb","AI Consulting & Strategy","We help you find where AI genuinely saves time or money, and just as important, where it doesn't. You get a practical plan, not a buzzword deck."),
 ("bolt","Workflow Automation","Automate the repetitive, error-prone work, data entry, scheduling, quotes, document handling, so your team spends its time on what actually matters."),
 ("chat","Copilot & AI Assistants","Roll out tools like Microsoft Copilot and business AI chat the right way: configured, secured, and with training your team will actually use."),
 ("cloud","Custom AI Integrations","Connect AI to the systems you already run, email, CRM, files, so it fits your workflow instead of becoming one more app to check."),
 ("shield","Secure & Responsible AI","Guardrails and clear policies so your team gets the benefit of AI without leaking sensitive company or customer data to public models."),
 ("monitor","AI-Assisted Support","We use AI in our own toolkit too: faster diagnostics, smarter monitoring, and quicker fixes, so your problems get solved sooner."),
]
ai_cards = "".join(svc_card(*s) for s in ai_services)
ai = (head(
 "AI Solutions for Business | Anderson Technologies",
 "Practical AI for businesses in Arizona and California: AI strategy, workflow automation, Microsoft Copilot setup, custom integrations, and secure, responsible AI adoption.",
 "ai.html")
 + nav("AI")
 + f'''<main id="main">
 <section class="page-hero"><div class="wrap">
   <span class="eyebrow reveal">AI Solutions</span>
   <h1 class="reveal d1">Put AI to work, without the hype</h1>
   <p class="reveal d2">Everyone is talking about AI. We help you actually use it, in ways that save your business real time and money, and we're honest about where it isn't worth the trouble.</p>
   <div class="hero-cta reveal d3" style="justify-content:center;margin-top:26px"><a href="contact.html?service=AI Solutions" class="btn btn-primary">Talk to us about AI {ARROW}</a><a href="contact.html#form" class="btn btn-ghost">Call or text us</a></div>
 </div></section>
 <div class="wrap"><div class="page-photo reveal"><img src="assets/it-ai.jpg" alt="Building an AI automation" loading="lazy" width="800" height="1200"></div></div>

 <section class="section"><div class="wrap">
   <div class="sec-head reveal"><span class="eyebrow">What we do with AI</span><h2>AI that fits how you work</h2></div>
   <div class="grid-svc">{ai_cards}</div>
 </div></section>

 <section class="section" style="background:var(--surface);border-block:1px solid var(--line)"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">How we approach it</span><h2>Useful first, impressive second</h2></div>
   <div class="steps">
     <div class="step reveal"><h3>Start with the problem</h3><p>We look at where your team loses time, not at what's trending. If AI isn't the right tool, we'll tell you.</p></div>
     <div class="step reveal d1"><h3>Build it around you</h3><p>We set up and connect the tools to your real workflow and data, with security and privacy built in from the start.</p></div>
     <div class="step reveal d2"><h3>Train and support</h3><p>Your team learns to actually use it, and we stay on to tune it as your needs change.</p></div>
   </div>
   <div class="center u-mt reveal"><a href="contact.html?service=AI Solutions" class="btn btn-primary">Talk to us about AI {ARROW}</a></div>
 </div></section>
 {cta("Curious where AI could help you?","Tell us what your team spends too much time on.<br>We'll show you honestly where AI fits, and where it doesn't.")}
 </main>''' + footer())
write("ai.html", ai)

# ============================ THANKS ============================
thanks = (head("Message received | Anderson Technologies","Thanks for reaching out. We'll be in touch soon.","thanks.html")
 + nav()
 + f'''<main id="main"><section class="page-hero" style="padding-block:clamp(4rem,10vw,7rem)"><div class="wrap">
   <div class="svc" style="width:64px;height:64px;margin:0 auto 24px;display:grid;place-items:center;border-radius:20px">
     <div class="ic" style="margin:0;width:auto;height:auto;background:none;color:var(--mint)"><svg viewBox="0 0 24 24" style="width:34px;height:34px" aria-hidden="true">{I["check"]}</svg></div></div>
   <h1>Thanks, we got it</h1>
   <p>Your message is on its way to our team. We'll be in touch with clear next steps. Need help sooner? Call {PHONE_AZ}.</p>
   <div class="hero-cta" style="justify-content:center;margin-top:26px"><a href="index.html" class="btn btn-primary">Back to home {ARROW}</a></div>
 </div></section></main>''' + footer())
write("thanks.html", thanks)

# ============================ 404 ============================
nf = (head("Page not found | Anderson Technologies","That page could not be found.","404.html")
 + nav()
 + f'''<main id="main"><section class="page-hero" style="padding-block:clamp(4rem,10vw,7rem)"><div class="wrap">
   <h1 style="font-size:var(--step-4)">404</h1><p>That page could not be found. It may have moved.</p>
   <div class="hero-cta" style="justify-content:center;margin-top:26px"><a href="index.html" class="btn btn-primary">Back to home {ARROW}</a></div>
 </div></section></main>''' + footer())
write("404.html", nf)

# ============================ sitemap + robots ============================
reviews_page = (head("Reviews | Anderson Technologies IT Support",
 "Reviews from Anderson Technologies managed IT and tech-support customers across Arizona and California.",
 "reviews.html")
 + nav() + f'''<main id="main">
 <section class="page-hero"><div class="wrap">
   <span class="eyebrow reveal">Reviews</span>
   <h1 class="reveal d1">What our clients say</h1>
   <p class="reveal d2">Feedback from the businesses and households we support across Arizona and California.</p>
 </div></section>
 <section class="section" style="padding-top:0"><div class="wrap">
   <div class="reviews">{"".join(_review_card(r) for r in REVIEWS)}</div>
 </div></section>
 {cta()}
 </main>''' + footer())
write("reviews.html", reviews_page)

# ============================ FAQ page ============================
import json
faq = [
 ("Pricing & plans", [
   ("How much does managed IT cost?", "Our managed IT is priced per user, per month, and custom-quoted to your team and needs, so there's no one-size flat rate. Tell us about your setup and we'll put together a free quote."),
   ("Is there a contract?", "You can go month-to-month, or save with an annual agreement. Whatever fits how you like to work."),
   ("Is there a minimum company size?", "No minimum. We help everyone from a single person to a larger team."),
   ("Is helpdesk support unlimited?", "Yes. Our managed helpdesk is unlimited, with no per-ticket charges."),
   ("Can we keep our current IT company and just use you for projects?", "Absolutely. We do project-only and co-managed work right alongside your existing provider."),
   ("Do you offer free consultations and estimates?", "Yes. Consultations and quotes are always free."),
 ]),
 ("Business IT & security", [
   ("Can you protect us from ransomware?", "Yes. We layer antivirus and endpoint protection, firewalls, email filtering, multi-factor authentication, security training, and tested backups, plus incident response if something ever gets through."),
   ("Do you set up multi-factor authentication (MFA)?", "Yes, MFA is a standard part of how we secure your accounts and systems."),
   ("Can you migrate us to Microsoft 365?", "Yes, including migrations from Google Workspace. We handle email, Teams, SharePoint, and day-to-day management."),
   ("Do you support HIPAA or PCI compliance?", "Yes. We help you meet security and compliance requirements, including HIPAA, PCI, and cyber-insurance requirements."),
   ("What's your response time, and can I get help after hours?", "Urgent issues get same-day attention, and managed clients have on-call support. For anything urgent, just call and we'll jump on it."),
   ("Do you provide on-site and remote support?", "Both. We can remote in for many issues, and we come on-site too, with on-site visits included on our Complete plan."),
   ("Can you handle servers, firewalls, cabling, and networks?", "Yes. Servers, firewall replacement, VLANs, structured cabling, network racks, Wi-Fi, and conference-room AV are all in our wheelhouse."),
 ]),
 ("Home & office support", [
   ("My computer is slow, crashing, or has a virus. Can you help?", "Yes. We do PC and Mac diagnostics, repair, tune-ups, and virus and malware removal to get things running right again."),
   ("Can you recover my files or photos?", "Yes. We handle data recovery for lost files, deleted photos, and failing or dead drives."),
   ("Can you fix my Wi-Fi or install mesh?", "Yes. We set up and improve home Wi-Fi, including mesh systems, so you get solid coverage everywhere."),
   ("Can you set up a new computer and move my files over?", "Yes. New-computer setup, file transfer, Office install, and monitor setup are all part of what we do."),
   ("Can you build a custom or gaming PC?", "Yes, we build custom and gaming PCs to fit what you need."),
   ("Can you set up smart home devices?", "Yes. Cameras, doorbells, thermostats, TVs, Alexa, and other smart devices, installed and connected."),
   ("Can you help with my email (Gmail or Outlook)?", "Yes. We help set up, transfer, and troubleshoot personal email."),
 ]),
 ("The basics", [
   ("What areas do you serve?", "Arizona and California, with remote support available for many issues."),
   ("Do you support both Mac and Windows?", "Yes, we work on PC, Mac, and Windows."),
   ("Are you insured, and are your technicians background-checked?", "Yes to both. We're insured and our technicians are background-checked."),
   ("Do you sell computers and hardware?", "Yes. We sell and supply computers and hardware, and we'll recommend the right gear for the job."),
   ("Can I text you? What are your numbers?", "Yes, text or call us anytime. Arizona is (480) 287-4190 and California is (805) 340-8055."),
   ("How do I schedule or get a quote?", "Call or text us, or fill out the contact form, and we'll get you set up with a free quote."),
 ]),
]
def _faq_items(group):
    return "".join(f'<details class="faq-item reveal"><summary class="faq-q">{q}</summary><div class="faq-a"><p>{a}</p></div></details>' for q,a in group)
faq_body = "".join(f'<div class="faq-group reveal"><h2>{t}</h2>{_faq_items(items)}</div>' for t,items in faq)
faq_ld = json.dumps({"@context":"https://schema.org","@type":"FAQPage",
  "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for _,items in faq for q,a in items]}, ensure_ascii=False)
faq_page = (head("FAQ | Anderson Technologies IT Support",
 "Answers to common questions about Anderson Technologies managed IT, home and office tech support, pricing, security, and service areas across Arizona and California.",
 "faq.html")
 + nav("FAQ") + f'''<main id="main">
 <section class="page-hero"><div class="wrap">
   <span class="eyebrow reveal">FAQ</span>
   <h1 class="reveal d1">Frequently asked questions</h1>
   <p class="reveal d2">Quick answers about our services, pricing, and how we work.<br>Still have a question? We're a call or message away.</p>
 </div></section>
 <section class="section" style="padding-top:0"><div class="wrap faq-wrap">
   {faq_body}
 </div></section>
 {cta()}
 </main>
 <script type="application/ld+json">{faq_ld}</script>''' + footer())
write("faq.html", faq_page)

# ============================ Careers page ============================
# location: "az" / "ca" (on-site in that state), "both" (on-site across AZ + CA), "remote" (desk/knowledge work).
# Field/on-site roles are state-bound; engineering, security, and back-office roles are remote.
careers_roles = [
 ("Technical", [
   ("IT Apprentice","$40,000 to $55,000","az"),("Bench Repair Technician","$42,000 to $58,000","az"),
   ("Residential IT Technician","$45,000 to $65,000","ca"),("Field Service Technician I","$50,000 to $70,000","az"),
   ("Field Service Technician II","$60,000 to $80,000","ca"),("Senior Field Technician","$75,000 to $95,000","both"),
   ("Help Desk Technician I","$45,000 to $60,000","az"),("Help Desk Technician II","$55,000 to $75,000","remote"),
   ("Help Desk Technician III","$70,000 to $90,000","remote"),("Systems Administrator","$75,000 to $105,000","remote"),
   ("Systems Engineer","$90,000 to $130,000","remote"),("Senior Systems Engineer","$120,000 to $160,000","remote"),
   ("Network Engineer","$90,000 to $130,000","both"),("Senior Network Engineer","$120,000 to $165,000","remote"),
   ("Cloud Engineer","$105,000 to $145,000","remote"),("Azure Engineer","$110,000 to $155,000","remote"),
   ("Microsoft 365 Engineer","$85,000 to $125,000","remote"),("Cybersecurity Analyst","$80,000 to $120,000","remote"),
   ("Security Engineer","$110,000 to $160,000","remote"),("SOC Analyst","$75,000 to $115,000","remote"),
   ("Compliance Specialist","$80,000 to $120,000","remote"),("Project Engineer","$90,000 to $130,000","both"),
   ("Project Manager","$90,000 to $140,000","remote"),("Cabling Technician","$45,000 to $70,000","ca"),
   ("Low Voltage Installer","$50,000 to $75,000","az"),
 ]),
 ("Leadership", [
   ("Service Manager","$90,000 to $130,000","az"),("Operations Manager","$95,000 to $140,000","az"),
   ("IT Director","$130,000 to $180,000","both"),("Cybersecurity Manager","$120,000 to $170,000","remote"),
   ("Engineering Manager","$125,000 to $175,000","remote"),("Client Success Manager","$80,000 to $120,000","ca"),
   ("Dispatch Manager","$60,000 to $90,000","az"),
 ]),
 ("Sales & customer service", [
   ("Customer Service Representative","$40,000 to $55,000","remote"),("Dispatcher","$45,000 to $65,000","az"),
   ("Account Manager","$65,000 to $100,000 plus commission","both"),("Business Development Representative","$55,000 to $75,000 plus commission","remote"),
   ("Sales Executive","$70,000 to $110,000 plus commission","ca"),("Sales Director","$120,000 to $200,000 plus bonuses","both"),
 ]),
 ("Administration", [
   ("Office Administrator","$45,000 to $65,000","az"),("HR Coordinator","$55,000 to $75,000","remote"),
   ("Payroll & Billing Specialist","$50,000 to $70,000","remote"),("Bookkeeper","$55,000 to $80,000","remote"),
   ("Purchasing & Inventory Coordinator","$50,000 to $75,000","az"),
 ]),
]
careers_ladders = [
 ("Technical path", ["IT Apprentice","Help Desk I","Help Desk II","Help Desk III","Systems Administrator","Systems Engineer","Senior Systems Engineer","Engineering Manager","IT Director"]),
 ("Field services path", ["Residential Technician","Field Technician I","Field Technician II","Senior Field Technician","Field Supervisor","Service Manager","Operations Manager"]),
 ("Sales path", ["Sales Development Rep","Account Executive","Senior Account Executive","Sales Manager","Sales Director"]),
]
careers_certs = [
 ("CompTIA","A+, Network+, Security+, Server+"),
 ("Microsoft","Microsoft 365 Certified, Azure Administrator (AZ-104), Azure Solutions Architect (AZ-305)"),
 ("Cisco","CCNA, CCNP"),
 ("Fortinet","NSE / Fortinet Certified Professional"),
 ("Ubiquiti","UniFi training and certifications"),
 ("VMware","VCP"),("Veeam","VMCE"),
 ("Apple","Apple Certified Mac Technician (ACMT)"),
 ("AWS","Cloud Practitioner, Solutions Architect (SAA)"),
 ("More","ITIL Foundation, Certified Ethical Hacker (CEH), CISSP for senior security roles"),
]
import re
_LOC = {"az":"AZ","ca":"CA","both":"AZ + CA","remote":"Remote"}
def _loc(l): return f'<span class="loc loc-{l}">{_LOC[l]}</span>'
def _salkey(s):
    m=re.search(r'\$([\d,]+)', s)
    return int(m.group(1).replace(',','')) if m else 0
import urllib.parse
def _sal_table(cat, rows):
    rows=sorted(rows, key=lambda r:_salkey(r[1]))   # sort low to high by starting salary
    def _row(p,s,loc):
        u="contact.html?job="+urllib.parse.quote(p)   # clicking the row -> contact form prefilled with this role
        return f'<tr class="job-row" data-href="{u}"><td><a class="job-link" href="{u}">{p}</a></td><td>{_loc(loc)}</td><td class="sal-pay">{s}</td></tr>'
    trs="".join(_row(p,s,loc) for p,s,loc in rows)
    return f'<div class="sal-group reveal"><h3>{cat}</h3><div class="sal-wrap"><table class="sal"><thead><tr><th>Position</th><th>Loc</th><th>Typical salary</th></tr></thead><tbody>{trs}</tbody></table></div></div>'
def _ladder(name, steps):
    return f'<div class="ladder reveal"><h4>{name}</h4><ol class="rungs">{"".join(f"<li>{s}</li>" for s in steps)}</ol></div>'
careers = (head("Careers | Anderson Technologies",
 "Join Anderson Technologies, a growing IT and tech-support team across Arizona and California. Roles, salary ranges, career paths, and how to apply.",
 "careers.html")
 + nav("Careers")
 + f'''<main id="main">
 <section class="page-hero"><div class="wrap">
   <span class="eyebrow reveal">Careers</span>
   <h1 class="reveal d1">Grow with Anderson Technologies</h1>
   <p class="lead reveal d2">A growing IT team across Arizona and California. Real career paths, honest pay.</p>
 </div></section>

 <section class="section" style="background:var(--surface);border-block:1px solid var(--line)"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">Career Opportunities</span>
     <h2>Roles & typical pay</h2>
     <p><span class="loc loc-az">AZ</span> <span class="loc loc-ca">CA</span> <span class="loc loc-both">AZ + CA</span> <span class="loc loc-remote">Remote</span></p></div>
   <div class="sal-layout">
     <div>{_sal_table(*careers_roles[0])}</div>
     <div class="sal-right">{"".join(_sal_table(c,rows) for c,rows in careers_roles[1:])}</div>
   </div>
 </div></section>

 <section class="section"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">Career progression</span>
     <h2>Career paths</h2></div>
   <div class="ladders">{"".join(_ladder(n,s) for n,s in careers_ladders)}</div>
 </div></section>

 <section class="section" style="background:var(--surface);border-block:1px solid var(--line)"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">Certifications</span>
     <h2>Certifications we value</h2></div>
   <div class="cert-grid">{"".join(f'<div class="cert reveal"><strong>{v}</strong><span>{c}</span></div>' for v,c in careers_certs)}</div>
 </div></section>

 <section class="section"><div class="wrap"><div class="reveal" style="max-width:680px;margin-inline:auto;text-align:center">
   <span class="eyebrow">How to apply</span>
   <h2 style="margin:14px 0 12px">Apply</h2>
   <p class="lead" style="text-wrap:balance">Email your resume to <a href="mailto:{EMAIL_DISPLAY}?subject=Careers%20Application" style="color:var(--brand);font-weight:600;text-decoration:none">{EMAIL_DISPLAY}</a>, or use the contact&nbsp;form.</p>
   <div class="hero-cta" style="justify-content:center;margin-top:1.8rem">
     <a href="contact.html" class="btn btn-primary">Get in touch {ARROW}</a>
     <a href="mailto:{EMAIL_DISPLAY}?subject=Careers%20Application" class="btn btn-ghost">Email your resume</a>
   </div>
 </div></div></section>
 </main>''' + footer())
write("careers.html", careers)

pages=[("index.html","1.0"),("business.html","0.9"),("support.html","0.9"),("ai.html","0.8"),("faq.html","0.8"),("careers.html","0.7"),("contact.html","0.8"),("reviews.html","0.7")]
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm+="".join(f'  <url><loc>{SITE}/{u}</loc><lastmod>2026-07-20</lastmod><priority>{p}</priority></url>\n' for u,p in pages)
sm+='</urlset>\n'
write("sitemap.xml", sm)
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

print("done: IT support site")
