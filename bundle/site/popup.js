/* Serene Med Spa — New Client offer popup (self-contained, brand-styled)
   Captures leads into the existing HubSpot form, then hands off to Mangomint booking. */
(function () {
  "use strict";

  // Last calendar day of the current month, e.g. "August 31, 2026" — auto-updates, no manual edits.
  function endOfMonth() {
    var n = new Date(), last = new Date(n.getFullYear(), n.getMonth() + 1, 0);
    return last.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric" });
  }

  var CFG = {
    book: "https://booking.mangomint.com/serenemedspa?serviceId=321",
    hs: { region: "na2", portal: "242695075", form: "16625e0e-6a46-4664-98c6-2cbf264da060" },
    image: "/img/lobby.jpg",
    dismissDays: 7,      // don't re-show for this many days after close
    delayMs: 7000,       // show after this long on the page...
    storageKey: "serene_np_v1"
  };

  // ---- gate: respect prior dismissal (unless forced via #offer) ----
  var forced = location.hash === "#offer";
  function dismissedRecently() {
    try {
      var t = parseInt(localStorage.getItem(CFG.storageKey) || "0", 10);
      return t && (Date.now() - t) < CFG.dismissDays * 864e5;
    } catch (e) { return false; }
  }
  function remember() {
    try { localStorage.setItem(CFG.storageKey, String(Date.now())); } catch (e) {}
  }

  var shown = false;

  function injectStyles() {
    if (document.getElementById("serene-np-css")) return;
    var css = document.createElement("style");
    css.id = "serene-np-css";
    css.textContent = [
      ".np-ov{position:fixed;inset:0;background:rgba(63,43,61,.55);backdrop-filter:blur(3px);z-index:9998;display:flex;align-items:center;justify-content:center;padding:20px;opacity:0;transition:opacity .28s ease}",
      ".np-ov.in{opacity:1}",
      ".np-card{position:relative;display:flex;width:100%;max-width:860px;max-height:92vh;overflow:hidden;background:#fff4f1;border-radius:22px;box-shadow:0 30px 80px rgba(63,43,61,.35);transform:translateY(14px);transition:transform .3s ease;font-family:'Jost',system-ui,sans-serif}",
      ".np-ov.in .np-card{transform:none}",
      ".np-pic{flex:0 0 42%;background:#e7d9e6 center/cover no-repeat;min-height:320px}",
      ".np-body{flex:1;padding:38px 34px;overflow-y:auto;text-align:center}",
      ".np-x{position:absolute;top:12px;right:14px;z-index:2;border:0;background:rgba(255,255,255,.7);width:34px;height:34px;border-radius:50%;font-size:20px;line-height:1;color:#3f2b3d;cursor:pointer}",
      ".np-x:hover{background:#fff}",
      ".np-ey{font-size:.74rem;letter-spacing:.18em;text-transform:uppercase;color:#c94f74;font-weight:600}",
      ".np-h{font-family:'Cormorant Garamond',serif;font-size:2rem;line-height:1.12;color:#3f2b3d;margin:8px 0 6px}",
      ".np-h b{color:#9988d2}",
      ".np-sub{color:#8a7b84;font-size:.96rem;margin:0 0 14px}",
      ".np-exp{display:inline-block;background:#3f2b3d;color:#fff;font-size:.78rem;letter-spacing:.04em;padding:7px 16px;border-radius:999px;margin-bottom:18px}",
      ".np-form{min-height:60px;margin:6px 0 4px;text-align:left}",
      ".np-btn{display:block;width:100%;box-sizing:border-box;background:linear-gradient(120deg,#f7a072,#e0698a 55%,#c94f74);color:#fff;border:0;border-radius:999px;padding:15px 20px;font-family:'Jost',sans-serif;font-size:1rem;font-weight:600;letter-spacing:.03em;cursor:pointer;text-decoration:none;text-align:center;margin-top:6px}",
      ".np-btn:hover{filter:brightness(1.04)}",
      ".np-exist{display:block;margin-top:14px;font-size:.9rem;color:#3f2b3d}",
      ".np-exist a{color:#c94f74;font-weight:600}",
      ".np-consent{font-size:.72rem;color:#8a7b84;line-height:1.5;margin:12px 0 0}",
      ".np-stars{margin-top:16px;color:#e0b25c;letter-spacing:3px;font-size:1.05rem}",
      ".np-rev{font-size:.76rem;letter-spacing:.14em;text-transform:uppercase;color:#8a7b84;margin-top:4px}",
      "@media(max-width:640px){.np-pic{display:none}.np-body{padding:30px 22px}.np-h{font-size:1.7rem}}"
    ].join("");
    document.head.appendChild(css);
  }

  function loadHubSpot() {
    if (document.getElementById("serene-hs-embed")) return;
    var s = document.createElement("script");
    s.id = "serene-hs-embed";
    s.src = "https://js-" + CFG.hs.region + ".hsforms.net/forms/embed/" + CFG.hs.portal + ".js";
    s.defer = true;
    document.body.appendChild(s);
  }

  function close(ov) {
    ov.classList.remove("in");
    remember();
    setTimeout(function () { if (ov && ov.parentNode) ov.parentNode.removeChild(ov); }, 300);
  }

  function build() {
    if (shown) return;
    shown = true;
    injectStyles();

    var ov = document.createElement("div");
    ov.className = "np-ov";
    ov.setAttribute("role", "dialog");
    ov.setAttribute("aria-modal", "true");
    ov.setAttribute("aria-label", "New client special");

    ov.innerHTML =
      '<div class="np-card">' +
        '<button class="np-x" aria-label="Close">&times;</button>' +
        '<div class="np-pic" style="background-image:url(' + CFG.image + ')"></div>' +
        '<div class="np-body">' +
          '<div class="np-ey">New Client Special</div>' +
          '<h2 class="np-h">Free Consultation <b>+ 20% Off</b><br>Your First Treatment</h2>' +
          '<p class="np-sub">Physician-led care in Hudson, OH. Tell us where to send your offer.</p>' +
          '<div class="np-exp">Offer expires: ' + endOfMonth() + '</div>' +
          '<div class="np-form"><div class="hs-form-frame" data-region="' + CFG.hs.region +
            '" data-form-id="' + CFG.hs.form + '" data-portal-id="' + CFG.hs.portal + '"></div></div>' +
          '<a class="np-btn" href="' + CFG.book + '" target="_blank" rel="noopener">Continue to Booking &rsaquo;</a>' +
          '<span class="np-exist">Existing client? <a href="' + CFG.book + '" target="_blank" rel="noopener">Book now</a></span>' +
          '<div class="np-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>' +
          '<div class="np-rev">Loved by our Hudson patients</div>' +
          '<p class="np-consent">By submitting, you agree to be contacted by Serene Med Spa by phone, text, or email about your inquiry and offers. Message/data rates may apply; reply STOP to opt out.</p>' +
        '</div>' +
      '</div>';

    document.body.appendChild(ov);
    loadHubSpot();
    requestAnimationFrame(function () { ov.classList.add("in"); });

    ov.querySelector(".np-x").addEventListener("click", function () { close(ov); });
    ov.addEventListener("click", function (e) { if (e.target === ov) close(ov); });
    document.addEventListener("keydown", function esc(e) {
      if (e.key === "Escape") { close(ov); document.removeEventListener("keydown", esc); }
    });
  }

  function arm() {
    if (forced) { build(); return; }
    if (dismissedRecently()) return;
    var timer = setTimeout(build, CFG.delayMs);
    // exit-intent (desktop): mouse leaves toward the top
    document.addEventListener("mouseout", function ex(e) {
      if (!e.relatedTarget && e.clientY <= 0) { clearTimeout(timer); build(); document.removeEventListener("mouseout", ex); }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", arm);
  } else { arm(); }
})();
