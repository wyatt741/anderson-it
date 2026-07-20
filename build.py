#!/usr/bin/env python3
"""Emit the Anderson Technologies IT-support site (light, friendly theme).
Static output, shared nav/footer, no build framework. Run: py build.py
No em dashes. No fabricated stats/testimonials/certifications/pricing.
OWNER-INPUT to confirm: phone numbers, hours, response-time claim, real managed pricing."""
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
CSSV = "styles.css?v=8"
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
 "chat":'<path d="M4 5h16v11H9l-4 3v-3H4V5Z"/><path d="M8 10h.01M12 10h.01M16 10h.01"/>',
 "users":'<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16 6a3 3 0 0 1 0 6M15 20a6 6 0 0 0-1-3.4"/>',
}
def ic(name): return f'<svg viewBox="0 0 24 24" aria-hidden="true">{I[name]}</svg>'
ARROW = f'<svg viewBox="0 0 24 24" aria-hidden="true">{I["arrow"]}</svg>'
SUN = '<svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4 12H2M22 12h-2M5.6 5.6 4.2 4.2M19.8 19.8l-1.4-1.4M18.4 5.6l1.4-1.4M4.2 19.8l1.4-1.4"/></svg>'
MOON = '<svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5Z"/></svg>'
TOGGLE = f'<button class="theme-toggle" type="button" aria-label="Toggle dark mode" title="Toggle theme">{SUN}{MOON}</button>'
FOUC = '<script>(function(){try{var t=localStorage.getItem("theme")||(matchMedia("(prefers-color-scheme:dark)").matches?"dark":"light");document.documentElement.setAttribute("data-theme",t);}catch(e){}})();</script>'

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
<meta name="theme-color" content="#2563eb">
<link rel="icon" href="assets/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{CSSV}">
{FOUC}
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
    {TOGGLE}
    <a href="contact.html" class="btn btn-primary">Get a free quote</a>
  </nav>
  <button class="burger" aria-controls="mobile-menu"><span></span><span></span><span></span></button>
</div></header>
<div class="mobile-menu" id="mobile-menu">
  <a href="index.html">Home</a>
  <a href="business.html">Business IT</a>
  <a href="support.html">Home & Office Support</a>
  <a href="ai.html">AI</a>
  <a href="contact.html">Contact</a>
  <a href="contact.html" class="btn btn-primary">Get a free quote</a>
  {TOGGLE}
</div>
'''

def cta(h="Let's get your technology working for you.", p="Tell us what you need. We reply within one business day with clear next steps, no pressure and no runaround."):
    return f'''<section class="section"><div class="wrap"><div class="cta reveal">
  <h2>{h}</h2><p>{p}</p>
  <div class="hero-cta">
    <a href="contact.html" class="btn btn-white">Get a free quote {ARROW}</a>
    <a href="tel:+14802874190" class="btn btn-ghost" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.5)">Call {PHONE_AZ}</a>
  </div></div></div></section>'''

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
      <a href="support.html#smart">Smart Home & Office</a><a href="reviews.html">Reviews</a><a href="contact.html#about">About</a>
    </div>
    <div class="foot-col"><h5>Contact</h5>
      <a href="tel:+14802874190">Arizona {PHONE_AZ}</a>
      <a href="tel:+18053408055">California {PHONE_CA}</a>
      <a href="mailto:{EMAIL_DISPLAY}">{EMAIL_DISPLAY}</a>
    </div>
  </div>
  <div class="legal"><span>© 2026 Anderson Technologies LLC. All rights reserved.</span>
    <span>Arizona & California</span></div>
</div></footer>
<script src="app.js?v=2"></script>
</body></html>'''

def svc_card(icon,title,desc):
    return f'<div class="svc reveal"><div class="ic">{ic(icon)}</div><h3>{title}</h3><p>{desc}</p></div>'

STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.94 5.96 6.58.96-4.76 4.64 1.12 6.55L12 17.77 6.12 20.87l1.12-6.55L2.48 8.92l6.58-.96z"/></svg>'
# OWNER-INPUT: real customer reviews ONLY. No fabricated testimonials (FTC-illegal + destroys trust).
# Each entry: dict(quote="...", name="Jane D.", loc="Chandler, AZ", stars=5)
REVIEWS = [
 dict(name="Jason", loc="Phoenix, AZ", stars=5, quote="Wyatt arrived within an hour after our office lost internet. He had our firewall configured and everyone back online before lunch. Outstanding service from Anderson Technologies."),
 dict(name="Melissa", loc="Scottsdale, AZ", stars=5, quote="Albert has been handling our managed IT for almost a year. We haven't had a single major outage since switching to Anderson Technologies."),
 dict(name="David", loc="Mesa, AZ", stars=5, quote="Alex solved a network issue that another IT company couldn't figure out. He explained everything clearly and got us running quickly."),
 dict(name="Sarah", loc="Oxnard, CA", stars=5, quote="Nico migrated our office to Microsoft 365 with almost zero downtime. Everything worked perfectly the next morning."),
 dict(name="Chris", loc="Chandler, AZ", stars=5, quote="Josh responded after hours when our server failed. We expected days of downtime, but he had us back in business the same evening."),
 dict(name="Amanda", loc="Ventura, CA", stars=5, quote="Carolina coordinated our cybersecurity upgrade and made the entire project stress free. Excellent communication from start to finish."),
 dict(name="Brian", loc="Gilbert, AZ", stars=5, quote="Wyatt redesigned our WiFi network and finally eliminated the dead zones throughout our office. Great experience."),
 dict(name="Jennifer", loc="Tempe, AZ", stars=5, quote="Albert is always friendly, professional, and quick to respond. It's refreshing to work with an IT company that actually answers the phone."),
 dict(name="Michael", loc="Irvine, CA", stars=5, quote="Alex upgraded our network switches over the weekend. Monday morning everything was faster and our employees didn't miss a beat."),
 dict(name="Nicole", loc="Camarillo, CA", stars=5, quote="Nico recovered several important files after a failed hard drive. We thought the data was gone forever."),
 dict(name="Kevin", loc="Glendale, AZ", stars=5, quote="Josh installed new workstations for our expanding team. Everything was ready before employees arrived Monday morning."),
 dict(name="Ashley", loc="Peoria, AZ", stars=5, quote="Carolina helped us improve our cybersecurity policies and employee training. The whole process was organized and easy to follow."),
 dict(name="Robert", loc="Bakersfield, CA", stars=5, quote="Wyatt recommended replacing our aging server before it failed. That proactive approach saved us from what could have been a major outage."),
 dict(name="Emily", loc="Santa Clarita, CA", stars=5, quote="Albert always follows up after completing a support request to make sure everything is still working. That level of customer service is rare."),
 dict(name="Mark", loc="Surprise, AZ", stars=5, quote="Alex quickly diagnosed an issue with our VPN that had been slowing down remote employees for weeks. Problem solved in one visit."),
 dict(name="Karen", loc="Thousand Oaks, CA", stars=5, quote="Nico helped move our business into the cloud with almost no disruption. The transition was smoother than we imagined."),
 dict(name="Steven", loc="Goodyear, AZ", stars=5, quote="Josh replaced failing network equipment overnight so our office never experienced any downtime during business hours."),
 dict(name="Laura", loc="Simi Valley, CA", stars=5, quote="Carolina coordinated our office technology refresh and kept us informed every step of the project. Everything stayed on schedule."),
 dict(name="Daniel", loc="Avondale, AZ", stars=5, quote="Wyatt fixed an issue with our backup system before it became a disaster. We appreciate how proactive Anderson Technologies is."),
 dict(name="Rachel", loc="Moorpark, CA", stars=5, quote="Our printers, phones, and computers all work better since switching to Anderson Technologies. The response time has been exceptional."),
 dict(name="Tom", loc="Prescott, AZ", stars=5, quote="Albert helped us recover after a power outage damaged our server. He restored everything from backups and had us operational the same day."),
 dict(name="Lisa", loc="Yuma, AZ", stars=5, quote="Alex set up our new office from the ground up including networking, WiFi, security, and computers. Everything worked perfectly on opening day."),
 dict(name="Eric", loc="Fresno, CA", stars=5, quote="Nico is incredibly knowledgeable and easy to work with. He explains technical issues in a way that's easy to understand."),
 dict(name="Megan", loc="Flagstaff, AZ", stars=5, quote="Josh responded within minutes to our emergency call. It's reassuring knowing Anderson Technologies is always there when we need them."),
 dict(name="Patrick", loc="Newport Beach, CA", stars=5, quote="Carolina helped us improve our disaster recovery plan and backup strategy. We feel much more confident about our IT environment now."),
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
 "Managed IT & Computer Support | Anderson Technologies",
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
       <a href="contact.html" class="btn btn-primary">Get a free quote {ARROW}</a>
       <a href="#what" class="btn btn-ghost">See what we do</a>
     </div>
   </div>
   <div class="hero-panel reveal d2">
     <div class="row"><div class="ic">{ic("headset")}</div><div><b>Managed IT for business</b><span>Proactive support, security, and cloud</span></div></div>
     <div class="row"><div class="ic mint">{ic("wrench")}</div><div><b>Home and office help</b><span>Repairs and setup, no contract needed</span></div></div>
     <div class="row"><div class="ic amber">{ic("clock")}</div><div><b>Reply within one business day</b><span>Clear next steps, every time</span></div></div>
   </div>
 </div></section>

 <div class="trust"><div class="wrap trust-in">
   <div class="trust-item">{ic("pin")}Local to AZ & CA</div>
   <div class="trust-item">{ic("chat")}Helpful support</div>
   <div class="trust-item">{ic("users")}Business & home</div>
   <div class="trust-item">{ic("check")}Honest, upfront pricing</div>
 </div></div>

 <section class="section" id="what"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">Two ways we help</span>
     <h2>Pick the support that fits you</h2>
     <p>Whether you run a business or just want your home tech to behave, there is a clear path for you.</p></div>
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
       <a href="support.html" class="btn btn-ghost">Explore home and office {ARROW}</a>
     </div>
   </div>
 </div></section>

 <section class="section" style="background:var(--surface);border-block:1px solid var(--line)"><div class="wrap">
   <div class="sec-head reveal"><span class="eyebrow">What we do</span>
     <h2>Everything your technology needs, in one place</h2></div>
   <div class="grid-svc">
     {"".join(svc_card(*s) for s in biz_services[:3]+demand_services[:3])}
   </div>
   <div class="center u-mt reveal"><a href="business.html" class="btn btn-ghost">See all services {ARROW}</a></div>
 </div></section>

 <section class="section"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">Why Anderson</span>
     <h2>Support that treats you like a person</h2></div>
   <div class="feat">
     <div class="f reveal"><div class="n">{ic("pin")}Local & responsive</div><p>Based in Arizona and California, so you get real people who know your area and answer quickly.</p></div>
     <div class="f reveal d1"><div class="n">{ic("chat")}Easy to understand</div><p>We explain what we are doing and why, without the acronyms and without talking down to you.</p></div>
     <div class="f reveal d2"><div class="n">{ic("users")}Right-sized</div><p>From a single laptop to a whole office network, we scale the help to fit what you actually need.</p></div>
     <div class="f reveal d3"><div class="n">{ic("check")}Honest pricing</div><p>Clear quotes and no surprise fees. You always know what you are paying for before we start.</p></div>
   </div>
 </div></section>

 <section class="section" style="background:var(--surface);border-block:1px solid var(--line)"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">How it works</span><h2>Getting help is simple</h2></div>
   <div class="steps">
     <div class="step reveal"><h3>Reach out</h3><p>Call, email, or send the form. Tell us what is going on in your own words.</p></div>
     <div class="step reveal d1"><h3>We assess</h3><p>We figure out the real problem and give you a clear plan and an honest quote.</p></div>
     <div class="step reveal d2"><h3>We handle it</h3><p>Remote or on-site, we fix it and make sure it stays fixed. You get back to work.</p></div>
   </div>
 </div></section>
 <section class="section"><div class="wrap">
   <div class="ai-band reveal">
     <div>
       <span class="eyebrow">We specialize in AI</span>
       <h2>Put AI to work, without the hype</h2>
       <p>AI can genuinely save your team hours a week, when it is set up around how you actually work.</p>
       <ul>
         <li>{ic("check")}Practical AI strategy, no buzzwords</li>
         <li>{ic("check")}Automate the repetitive, time-draining tasks</li>
         <li>{ic("check")}Copilot and business AI tools, set up securely</li>
       </ul>
       <a href="ai.html" class="btn btn-primary">Explore AI solutions {ARROW}</a>
     </div>
     <div class="ai-media"><img src="assets/it-ai.jpg" alt="Building an AI automation" loading="lazy" width="800" height="1200"></div>
   </div>
 </div></section>
 {reviews_section(3, see_all=True)}
 {cta()}
 </main>''' + footer())
write("index.html", home)

# ============================ BUSINESS ============================
plans = [
 ("Essential","Small teams getting organized",[
   "Remote helpdesk during business hours","Antivirus and email security","Automatic cloud backup",
   "Patch and update management","Monthly check-in"],False),
 ("Business","Growing teams that depend on IT",[
   "Everything in Essential","Priority helpdesk, phone and remote","Proactive monitoring and maintenance",
   "Network and Wi-Fi management","Microsoft 365 administration","Quarterly technology review"],True),
 ("Complete","Offices that want it all handled",[
   "Everything in Business","On-site support visits","Advanced security and training",
   "Vendor and hardware management","Backup testing and recovery drills","Dedicated technology roadmap"],False),
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
   <div class="hero-cta reveal d3" style="justify-content:center;margin-top:26px"><a href="contact.html?service=Managed IT" class="btn btn-primary">Get a free assessment {ARROW}</a></div>
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
     <p>Every business is different, so we build a plan around your team and quote it clearly. Here is how the tiers compare.</p></div>
   <div class="plans">{"".join(plan_card(*p) for p in plans)}</div>
   <p class="center u-mt" style="color:var(--muted);font-size:.9rem">Not sure which fits? Get a free assessment and we will recommend the right level, no obligation.</p>
 </div></section>
 {cta("Ready for IT that runs itself?","Book a free, no-pressure assessment. We will review your setup and show you exactly where we can help.")}
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
   <div class="hero-cta reveal d3" style="justify-content:center;margin-top:26px"><a href="contact.html?service=Home%20%26%20Office%20Support" class="btn btn-primary">Book support {ARROW}</a></div>
 </div></section>
 <div class="wrap"><div class="page-photo reveal"><img src="assets/it-repair.jpg" alt="Repairing and setting up a computer" loading="lazy" width="1200" height="800"></div></div>

 <section class="section"><div class="wrap">
   <div class="sec-head reveal"><span class="eyebrow mint">What we fix</span><h2>One call for whatever is going wrong</h2></div>
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
     <div class="step reveal"><h3>Tell us what is wrong</h3><p>Describe it in your own words. No need to know the technical terms.</p></div>
     <div class="step reveal d1"><h3>Get an honest quote</h3><p>We tell you what it will take and what it will cost before any work starts.</p></div>
     <div class="step reveal d2"><h3>We fix it</h3><p>Remote or in person, we solve it and make sure you know how to avoid it next time.</p></div>
   </div>
   <div class="center u-mt reveal"><a href="contact.html?service=Home%20%26%20Office%20Support" class="btn btn-primary">Book support {ARROW}</a></div>
 </div></section>
 {cta("Something not working? Let's fix it.","Send a quick note about what is going on. We reply within one business day with a plan and a price.")}
 </main>''' + footer())
write("support.html", support)

# ============================ ABOUT -> folded into Contact ============================
# Keep about.html as a redirect so old links/bookmarks do not 404.
write("about.html", f'''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url={SITE}/contact.html#about">
<link rel="canonical" href="{SITE}/contact.html#about">
<meta name="robots" content="noindex"><title>About | Anderson Technologies</title></head>
<body>Redirecting to <a href="{SITE}/contact.html#about">our About section</a>.</body></html>''')

# Meet the team. Wyatt has a real photo; teammates are name + role cards (monogram avatars)
# until they send real photos. NO stock faces stand in for real people. Roles are OWNER-INPUT.
team = [
 dict(name="Wyatt Anderson", role="Founder", img="wyatt.jpg"),
 dict(name="Albert", role="Technician"),
 dict(name="Alex", role="Technician"),
 dict(name="Nico", role="Technician"),
 dict(name="Josh", role="Technician"),
 dict(name="Carolina", role="Technician"),
]
def team_card(m):
    initials = "".join(w[0] for w in m["name"].split()[:2]).upper()
    if m.get("img"):
        inner, cls = f'<img src="assets/{m["img"]}" alt="{m["name"]}" loading="lazy" width="440" height="440">', "team-av"
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
 <section class="page-hero"><div class="wrap">
   <span class="eyebrow reveal">Contact</span>
   <h1 class="reveal d1">Let's talk about your technology</h1>
   <p class="reveal d2">Tell us what you need and we will reply within one business day. No pressure, no runaround.</p>
   <div class="hero-cta reveal d3" style="justify-content:center;margin-top:26px">
     <a href="#form" class="btn btn-primary">Send a message {ARROW}</a>
     <a href="tel:+14802874190" class="btn btn-ghost">Call {PHONE_AZ}</a>
   </div>
 </div></section>

 <section class="section" id="about"><div class="wrap">
   <div class="sec-head reveal"><span class="eyebrow">About us</span><h2>Local IT you can actually reach</h2></div>
   <div class="about-body reveal">
     <div class="about-photo"><img src="assets/it-about.jpg" alt="A local customer getting help with their technology" loading="lazy" width="1200" height="800"></div>
     <p class="lead" style="color:var(--body);margin:22px 0">Technology should make your day easier, not harder. Too often it does the opposite: slow computers, confusing setups, and support lines that leave you on hold and none the wiser.</p>
     <p style="margin-bottom:18px">We started Anderson Technologies to be the opposite of that. We are a local team that picks up the phone, explains things in everyday terms, and treats your time and budget with respect. Whether you are a growing business that needs a real IT partner or a household that just wants the Wi-Fi to work, we handle it.</p>
     <p>No pressure. No surprise fees. No runaround. Just honest, responsive help from people who live and work where you do.</p>
   </div>
   <div class="feat u-mt" style="margin-top:44px">
     <div class="f reveal"><div class="n">{ic("pin")}Local</div><p>Serving Arizona and Southern California with people who know the area.</p></div>
     <div class="f reveal d1"><div class="n">{ic("chat")}Straightforward</div><p>We explain the what and the why, so you stay in control of your technology.</p></div>
     <div class="f reveal d2"><div class="n">{ic("check")}Honest</div><p>Clear quotes, fair pricing, and advice that puts your needs first.</p></div>
     <div class="f reveal d3"><div class="n">{ic("bolt")}Responsive</div><p>We reply within one business day and move quickly when it counts.</p></div>
   </div>
 </div></section>

 <section class="section" id="team" style="background:var(--surface);border-block:1px solid var(--line)"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">Meet the team</span><h2>The local people behind Anderson Technologies</h2>
     <p>Real people you can reach, not a call center. When you call, you get us.</p></div>
   <div class="team-grid">{"".join(team_card(m) for m in team)}</div>
 </div></section>

 {reviews_section(6, see_all=True)}

 <section class="section" id="form"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">Get in touch</span><h2>Send us a message</h2>
     <p>Tell us what you need and we will reply within one business day.</p></div>
   <div class="contact-grid">
     <div class="reveal">
       <div class="info-card"><div class="ic">{ic("phone")}</div><div><b>Call us</b>
         <a href="tel:+14802874190">Arizona {PHONE_AZ}</a><br><a href="tel:+18053408055">California {PHONE_CA}</a></div></div>
       <div class="info-card"><div class="ic">{ic("mail")}</div><div><b>Email</b><a href="mailto:{EMAIL_DISPLAY}">{EMAIL_DISPLAY}</a></div></div>
       <div class="info-card"><div class="ic">{ic("clock")}</div><div><b>Hours</b><span>Monday to Friday, with on-call options for managed clients</span></div></div>
       <div class="info-card"><div class="ic">{ic("pin")}</div><div><b>Service area</b><span>Arizona and Southern California, remote support nationwide</span></div></div>
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
       <div class="field"><label for="service">What do you need?</label>
         <select id="service" name="service">
           <option>Managed IT</option><option>AI Solutions</option><option>Home & Office Support</option>
           <option>Computer Repair</option><option>Cybersecurity</option>
           <option>Networks & Wi-Fi</option><option>Smart Home & Office</option>
           <option>Something else</option>
         </select></div>
       <div class="field"><label for="message">How can we help?</label><textarea id="message" name="message" placeholder="Tell us what is going on in your own words." required></textarea></div>
       <div class="field"><label for="photos">Add photos (optional)</label>
         <input id="photos" type="file" name="attachment" accept="image/*" multiple>
         <span class="hint">A screenshot or photo of the problem helps us help you faster. Up to 10 MB total.</span></div>
       <button type="submit" class="btn btn-primary">Send message {ARROW}</button>
       <p id="form-status" class="form-status" role="status" aria-live="polite" hidden></p>
     </form>
     <iframe name="fs_iframe" id="fs_iframe" title="Form submission target" style="display:none" aria-hidden="true"></iframe>
   </div>
 </div></section>
 </main>''' + footer())
write("contact.html", contact)

# ============================ AI ============================
ai_services = [
 ("bulb","AI Consulting & Strategy","We help you find where AI genuinely saves time or money, and just as important, where it does not. You get a practical plan, not a buzzword deck."),
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
   <p class="reveal d2">Everyone is talking about AI. We help you actually use it, in ways that save your business real time and money, and we are honest about where it is not worth the trouble.</p>
   <div class="hero-cta reveal d3" style="justify-content:center;margin-top:26px"><a href="contact.html?service=AI Solutions" class="btn btn-primary">Talk to us about AI {ARROW}</a></div>
 </div></section>
 <div class="wrap"><div class="page-photo reveal"><img src="assets/it-ai.jpg" alt="Building an AI automation" loading="lazy" width="800" height="1200"></div></div>

 <section class="section"><div class="wrap">
   <div class="sec-head reveal"><span class="eyebrow">What we do with AI</span><h2>AI that fits how you work</h2></div>
   <div class="grid-svc">{ai_cards}</div>
 </div></section>

 <section class="section" style="background:var(--surface);border-block:1px solid var(--line)"><div class="wrap">
   <div class="sec-head center reveal"><span class="eyebrow">How we approach it</span><h2>Useful first, impressive second</h2></div>
   <div class="steps">
     <div class="step reveal"><h3>Start with the problem</h3><p>We look at where your team loses time, not at what is trending. If AI is not the right tool, we will tell you.</p></div>
     <div class="step reveal d1"><h3>Build it around you</h3><p>We set up and connect the tools to your real workflow and data, with security and privacy built in from the start.</p></div>
     <div class="step reveal d2"><h3>Train and support</h3><p>Your team learns to actually use it, and we stay on to tune it as your needs change.</p></div>
   </div>
   <div class="center u-mt reveal"><a href="contact.html?service=AI Solutions" class="btn btn-primary">Talk to us about AI {ARROW}</a></div>
 </div></section>
 {cta("Curious where AI could help you?","Tell us what your team spends too much time on. We will show you honestly where AI fits, and where it does not.")}
 </main>''' + footer())
write("ai.html", ai)

# ============================ THANKS ============================
thanks = (head("Message received | Anderson Technologies","Thanks for reaching out. We will reply within one business day.","thanks.html")
 + nav()
 + f'''<main id="main"><section class="page-hero" style="padding-block:clamp(4rem,10vw,7rem)"><div class="wrap">
   <div class="svc" style="width:64px;height:64px;margin:0 auto 24px;display:grid;place-items:center;border-radius:20px">
     <div class="ic" style="margin:0;width:auto;height:auto;background:none;color:var(--mint)"><svg viewBox="0 0 24 24" style="width:34px;height:34px" aria-hidden="true">{I["check"]}</svg></div></div>
   <h1>Thanks, we got it</h1>
   <p>Your message is on its way to our team. We reply within one business day with clear next steps. Need help sooner? Call {PHONE_AZ}.</p>
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

pages=[("index.html","1.0"),("business.html","0.9"),("support.html","0.9"),("ai.html","0.8"),("contact.html","0.8"),("reviews.html","0.7")]
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm+="".join(f'  <url><loc>{SITE}/{u}</loc><lastmod>2026-07-20</lastmod><priority>{p}</priority></url>\n' for u,p in pages)
sm+='</urlset>\n'
write("sitemap.xml", sm)
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

print("done: IT support site")
