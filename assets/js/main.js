// Header hairline, scroll reveal, index hover preview, lightbox.
(() => {
  const header = document.querySelector(".site-header");
  const onScroll = () => header && header.classList.toggle("is-scrolled", window.scrollY > 8);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // reveal on scroll
  const reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      for (const en of entries) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      }
    }, { rootMargin: "0px 0px -8% 0px" });
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("is-in"));
  }

  // index: image preview following the cursor (pointer devices only)
  const preview = document.querySelector(".index-preview");
  if (preview && window.matchMedia("(hover: hover)").matches) {
    let x = 0, y = 0, raf = 0;
    const place = () => {
      raf = 0;
      const w = preview.offsetWidth, h = preview.offsetHeight;
      const px = Math.min(x + 28, window.innerWidth - w - 16);
      const py = Math.min(Math.max(y - h / 2, 16), window.innerHeight - h - 16);
      preview.style.transform = `translate(${px}px, ${py}px)`;
    };
    document.querySelectorAll(".index-list .row").forEach((row) => {
      row.addEventListener("mouseenter", () => {
        preview.src = row.dataset.preview;
        preview.classList.add("is-on");
      });
      row.addEventListener("mouseleave", () => preview.classList.remove("is-on"));
    });
    window.addEventListener("mousemove", (ev) => {
      x = ev.clientX; y = ev.clientY;
      if (!raf) raf = requestAnimationFrame(place);
    }, { passive: true });
  }

  // lightbox — groups by data-lightbox value
  const lb = document.querySelector(".lightbox");
  if (!lb) return;
  const lbImg = lb.querySelector("img");
  const lbCap = lb.querySelector(".lb-caption");
  const stage = lb.querySelector(".lb-stage");
  let group = [], idx = 0, lastFocus = null;

  const show = (i) => {
    idx = (i + group.length) % group.length;
    const a = group[idx];
    lb.classList.remove("is-zoomed");
    lbImg.src = a.getAttribute("href");
    lbImg.alt = a.dataset.caption || "";
    lbCap.textContent = a.dataset.caption || "";
    stage.scrollTo(0, 0);
    const many = group.length > 1;
    lb.querySelector(".lb-prev").style.visibility = many ? "visible" : "hidden";
    lb.querySelector(".lb-next").style.visibility = many ? "visible" : "hidden";
  };
  const open = (a) => {
    group = [...document.querySelectorAll(`[data-lightbox="${a.dataset.lightbox}"]`)];
    lastFocus = document.activeElement;
    show(group.indexOf(a));
    lb.hidden = false;
    lb.setAttribute("aria-hidden", "false");
    document.documentElement.style.overflow = "hidden";
    requestAnimationFrame(() => lb.classList.add("is-open"));
    lb.querySelector(".lb-close").focus();
  };
  const close = () => {
    lb.classList.remove("is-open", "is-zoomed");
    lb.setAttribute("aria-hidden", "true");
    document.documentElement.style.overflow = "";
    setTimeout(() => { lb.hidden = true; lbImg.removeAttribute("src"); }, 300);
    if (lastFocus) lastFocus.focus();
  };

  document.addEventListener("click", (ev) => {
    const a = ev.target.closest("[data-lightbox]");
    if (!a || ev.metaKey || ev.ctrlKey) return;
    ev.preventDefault();
    open(a);
  });
  lb.querySelector(".lb-close").addEventListener("click", close);
  lb.querySelector(".lb-prev").addEventListener("click", () => show(idx - 1));
  lb.querySelector(".lb-next").addEventListener("click", () => show(idx + 1));
  lbImg.addEventListener("click", () => lb.classList.toggle("is-zoomed"));
  stage.addEventListener("click", (ev) => { if (ev.target === stage) close(); });
  document.addEventListener("keydown", (ev) => {
    if (lb.hidden) return;
    if (ev.key === "Escape") close();
    else if (ev.key === "ArrowLeft") show(idx - 1);
    else if (ev.key === "ArrowRight") show(idx + 1);
  });

  // swipe
  let sx = null;
  lb.addEventListener("touchstart", (ev) => { sx = ev.touches[0].clientX; }, { passive: true });
  lb.addEventListener("touchend", (ev) => {
    if (sx === null || lb.classList.contains("is-zoomed")) return;
    const dx = ev.changedTouches[0].clientX - sx;
    if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
    sx = null;
  });
})();
