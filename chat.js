/* Anderson Technologies chat widget: AI Q&A + a guided quote-request wizard.
   The wizard is deterministic (no AI, no cost, no invented prices) and packages
   the answers into a lead sent to info@ via the Worker's /lead endpoint. */
(function () {
  // ==========================================================================
  // CONFIG: after you deploy the Cloudflare Worker (see worker/README.md),
  // paste its URL here (no trailing slash), bump chat.js?v= in build.py, rebuild.
  // Until this is set to a real URL, the widget stays hidden.
  var WORKER_URL = "https://anderson-chat.YOURSUBDOMAIN.workers.dev";
  // ==========================================================================

  var root = document.getElementById("cw");
  if (!root || WORKER_URL.indexOf("YOURSUBDOMAIN") !== -1) return; // not configured -> stay hidden

  root.classList.add("cw--ready");
  root.setAttribute("aria-hidden", "false");

  var bubble = document.getElementById("cw-bubble");
  var panel  = document.getElementById("cw-panel");
  var closeB = document.getElementById("cw-close");
  var log    = document.getElementById("cw-log");
  var form   = document.getElementById("cw-form");
  var input  = document.getElementById("cw-input");
  var sendB  = document.getElementById("cw-send");

  var history = [];       // {role, content} for the AI
  var mode = "menu";      // menu | chat | wizard
  var started = false;
  var busy = false;

  var PHONE = "(480) 287-4190";
  var CONTACT = "https://andersontechsupport.com/contact.html";

  // ---------- helpers ----------
  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }
  function scroll() { log.scrollTop = log.scrollHeight; }
  function setInput(enabled, ph) { input.disabled = !enabled; sendB.disabled = !enabled; input.placeholder = ph || "Type your message..."; }

  // safe linkify: URLs -> <a>, "(xxx) xxx-xxxx" -> tel:. Builds text/anchor nodes (no innerHTML).
  function linkify(container, text) {
    var re = /(https?:\/\/[^\s)]+)|(\(\d{3}\)\s?\d{3}-\d{4})/g, last = 0, m;
    while ((m = re.exec(text))) {
      if (m.index > last) container.appendChild(document.createTextNode(text.slice(last, m.index)));
      var a = document.createElement("a");
      if (m[1]) { a.href = m[1]; a.target = "_blank"; a.rel = "noopener"; a.textContent = m[1].replace(/^https?:\/\//, "").replace(/\/$/, ""); }
      else { a.href = "tel:+1" + m[2].replace(/\D/g, ""); a.textContent = m[2]; }
      container.appendChild(a);
      last = m.index + m[0].length;
    }
    if (last < text.length) container.appendChild(document.createTextNode(text.slice(last)));
  }

  function addMsg(role, text) { var d = el("div", "cw-msg cw-" + role); linkify(d, text); log.appendChild(d); scroll(); return d; }
  function typing() { var t = el("div", "cw-msg cw-bot cw-typing"); t.appendChild(el("span")); t.appendChild(el("span")); t.appendChild(el("span")); log.appendChild(t); scroll(); return t; }
  function chips(items) {
    var wrap = el("div", "cw-chips");
    items.forEach(function (it) {
      var b = el("button", "cw-chip" + (it.ghost ? " cw-chip-ghost" : ""), it.label);
      b.type = "button";
      b.addEventListener("click", function () { wrap.remove(); it.act(); });
      wrap.appendChild(b);
    });
    log.appendChild(wrap); scroll(); return wrap;
  }

  // ---------- open / close ----------
  function open() {
    panel.hidden = false; bubble.setAttribute("aria-expanded", "true"); root.classList.add("cw--open");
    if (!started) { started = true; showMenu(); }
    setTimeout(function () { (input.disabled ? bubble : input).focus(); }, 60);
  }
  function close() { panel.hidden = true; bubble.setAttribute("aria-expanded", "false"); root.classList.remove("cw--open"); bubble.focus(); }
  bubble.addEventListener("click", function () { panel.hidden ? open() : close(); });
  closeB.addEventListener("click", close);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !panel.hidden) close(); });

  // ---------- menu ----------
  function showMenu() {
    mode = "menu";
    addMsg("bot", "Hi! I'm the Anderson Technologies assistant. I can answer questions about our services, or help you start a free quote.");
    chips([
      { label: "Ask a question", act: function () { mode = "chat"; setInput(true); addMsg("bot", "Sure, what would you like to know?"); input.focus(); } },
      { label: "Get a quote", act: startWizard },
    ]);
    setInput(true, "Type a message, or pick an option");
  }

  // ---------- AI chat ----------
  function sendChat(text) {
    history.push({ role: "user", content: text });
    busy = true; setInput(false, "..."); var t = typing();
    fetch(WORKER_URL + "/chat", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ messages: history }) })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        t.remove();
        var reply = (d && d.reply) ? d.reply : ("Sorry, I had trouble there. You can reach us at " + PHONE + " or " + CONTACT);
        history.push({ role: "assistant", content: reply });
        addMsg("bot", reply);
      })
      .catch(function () { t.remove(); addMsg("bot", "Sorry, I couldn't connect. Please call " + PHONE + " or use " + CONTACT); })
      .finally(function () { busy = false; setInput(true); input.focus(); });
  }

  // ---------- quote wizard (deterministic, no AI) ----------
  var STEPS = [
    { key: "audience", q: "Let's build your quote. First, is this for a business or your home/office?", opts: ["Business", "Home & Office"] },
    { key: "needs",    q: "What do you need help with?", opts: ["Managed IT", "Repair or setup", "Cybersecurity", "Cloud & Microsoft 365", "AI solutions", "Not sure yet"] },
    { key: "devices",  q: "Roughly how many computers or devices?", opts: ["1-5", "6-20", "21-50", "50+"] },
    { key: "people",   q: "About how many people use them?", opts: ["Just me / 1-2", "3-10", "11-25", "25+"] },
    { key: "details",  q: "Anything specific going on? Type a line or two, or skip.", text: true, optional: true },
    { key: "name",     q: "Great. What's your name?", text: true },
    { key: "email",    q: "And the best email for your quote?", text: true, email: true },
    { key: "phone",    q: "A phone number in case we need it? Optional, type or skip.", text: true, optional: true },
  ];
  var answers = {}, step = 0, skipWrap = null;

  function startWizard() { mode = "wizard"; answers = {}; step = 0; runStep(); }
  function runStep() {
    if (step >= STEPS.length) return submitQuote();
    var s = STEPS[step];
    addMsg("bot", s.q);
    if (s.opts) {
      setInput(false, "Choose an option above");
      chips(s.opts.map(function (opt) { return { label: opt, act: function () { addMsg("user", opt); answers[s.key] = opt; step++; runStep(); } }; }));
    } else {
      setInput(true, s.optional ? "Type, or click Skip" : "Type your answer...");
      skipWrap = s.optional ? chips([{ label: "Skip", ghost: true, act: function () { skipWrap = null; answers[s.key] = ""; step++; runStep(); } }]) : null;
      input.focus();
    }
  }
  function wizardText(text) {
    var s = STEPS[step];
    if (s.email && !/.+@.+\..+/.test(text)) { addMsg("bot", "Hmm, that doesn't look like an email. Mind trying again?"); input.focus(); return; }
    if (skipWrap) { skipWrap.remove(); skipWrap = null; }
    addMsg("user", text); answers[s.key] = text; step++; runStep();
  }
  function submitQuote() {
    setInput(false, "Sending..."); var t = typing();
    fetch(WORKER_URL + "/lead", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(answers) })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        t.remove();
        if (d && d.ok) addMsg("bot", "Perfect, that's everything. We'll put together a quote and get back to you soon. Need it faster? Call " + PHONE + ".");
        else addMsg("bot", "I couldn't send that just now. Please call " + PHONE + " or use " + CONTACT + " and we'll sort your quote.");
      })
      .catch(function () { t.remove(); addMsg("bot", "I couldn't connect to send that. Please call " + PHONE + " or use " + CONTACT); })
      .finally(function () { mode = "chat"; setInput(true, "Ask anything else..."); });
  }

  // ---------- input routes by mode ----------
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var text = input.value.trim();
    if (!text || busy) return;
    input.value = "";
    if (mode === "wizard" && STEPS[step] && STEPS[step].text) { wizardText(text); return; }
    mode = "chat"; addMsg("user", text); sendChat(text);
  });
})();
