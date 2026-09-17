/* form-guard.js — lightweight spam screening for the Zoho lead forms (consult form + offer popup).
   Runs in the capture phase, before each form's own submit handler.
   - Honeypot filled  -> pretend success, send nothing.
   - Suspicious text (links, Cyrillic, SEO/marketing pitches, vendor solicitations) or a
     submit faster than a human could type -> still delivered, but tagged "Junk Lead" and
     prefixed so the front desk can skip it. Nothing real is ever silently dropped. */
(function () {
  var T0 = Date.now();
  var PITCH = /(seo\b|search engine|online (visibility|presence|performance)|rank(ing)? (higher|on google)|website (audit|design|redesign)|improv\w* (the |your )?(site|website)|backlink|guest post|web ?developer|digital marketing|lead generation|bookkeeping|virtual assistant|merchant (services|cash)|business (loan|funding)|crypto|casino|free spins|wagering|jackpot|interested in (purchasing|buying) (your|a|the) )/i;
  function suspicious(text, elapsed) {
    if (/[Ѐ-ӿ]/.test(text)) return "non-English script";
    if (/https?:\/\/|www\.|\.(workers\.dev|ru|xyz|top)\b/i.test(text)) return "link in message";
    if (PITCH.test(text)) return "sales/marketing pitch";
    if (elapsed < 3000) return "submitted too fast";
    return "";
  }
  function setHidden(f, name, val) {
    var i = f.querySelector('[name="' + name + '"]');
    if (!i) { i = document.createElement("input"); i.type = "hidden"; i.name = name; f.appendChild(i); }
    i.value = val;
  }
  document.addEventListener("submit", function (e) {
    var f = e.target;
    if (!f || !(f.id === "zf-consult" || (f.classList && f.classList.contains("np-zf")))) return;
    var hp = f.querySelector('[name="aG9uZXlwb3Q"]');
    if (hp && hp.value.trim()) {
      e.preventDefault(); e.stopImmediatePropagation();
      if (f.id === "zf-consult") { f.hidden = true; var d = document.getElementById("zf-done"); if (d) d.hidden = false; }
      else { f.outerHTML = '<div class="np-ok">&#10003; Thank you!</div>'; }
      return;
    }
    var desc = f.querySelector('[name="Description"]');
    var text = [desc && desc.tagName === "TEXTAREA" ? desc.value : "",
                (f.querySelector('[name="First Name"]') || {}).value || "",
                (f.querySelector('[name="Last Name"]') || {}).value || ""].join(" ");
    var why = suspicious(text, Date.now() - T0);
    if (why) {
      setHidden(f, "Lead Status", "Junk Lead");
      if (desc) desc.value = "[Auto-flagged: " + why + "] " + desc.value;
    }
  }, true);
})();
