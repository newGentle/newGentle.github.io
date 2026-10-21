"""Build the EN/RU executive CV pages and recruiter-oriented print views.

Source content: site/content/en.json and site/content/ru.json.
Rendering is intentionally dependency-free for GitHub Pages.
"""
from pathlib import Path
from html import escape as html_escape
import json

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "site" / "content"

def e(value):
    return html_escape(str(value), quote=True)

def concat(items):
    return "\n".join(items)

def meta_html(data, ru):
    lang = data["lang"]
    path = "ru/" if ru else ""
    prefix = "../" if ru else ""
    canonical = f"https://newgentle.github.io/{path}"
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{e(data['meta']['description'])}">
<meta name="theme-color" content="#171616">
<title>{e(data['meta']['title'])}</title>
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="https://newgentle.github.io/">
<link rel="alternate" hreflang="ru" href="https://newgentle.github.io/ru/">
<meta property="og:type" content="profile">
<meta property="og:title" content="{e(data['meta']['title'])}">
<meta property="og:description" content="{e(data['meta']['description'])}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="https://newgentle.github.io/assets/og-{lang}.png">
<meta property="og:image:secure_url" content="https://newgentle.github.io/assets/og-{lang}.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(data['name'])} — Head of IT">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(data['meta']['title'])}">
<meta name="twitter:description" content="{e(data['meta']['description'])}">
<meta name="twitter:image" content="https://newgentle.github.io/assets/og-{lang}.png">
<link rel="stylesheet" href="{prefix}assets/site.css">
<link rel="stylesheet" href="{prefix}assets/reference-direction.css">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<script src="{prefix}assets/site.js" defer></script>
<script src="{prefix}assets/network-motion.js" defer></script>
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"Person","name":data["name"],"jobTitle":"Head of IT Department","url":canonical,"image":"https://newgentle.github.io/photo.webp","sameAs":[data["github"],data["linkedin"]]},ensure_ascii=False)}</script>"""

def nav_html(data, ru):
    nav = data["nav"]
    return concat(f'<a class="nav-link" href="#{key}">{e((nav.get(title) or data["qualifications"]["title"]))}</a>' for key, title in [("about","about"),("experience","experience"),("expertise","expertise"),("qualifications","qualifications"),("contact","contact")])

def hero_html(data, ru):
    h = data["hero"]
    p = "../" if ru else ""
    return f"""<section class="hero" id="top" aria-labelledby="hero-title">
    <div class="hero-ambient" aria-hidden="true"></div>
    <div class="wrap hero-layout">
      <div class="hero-copy" data-reveal>
        <p class="hero-eyebrow"><span class="signal" aria-hidden="true"></span>{e(h['eyebrow'])}</p>
        <h1 id="hero-title">{e(data['name'])}</h1>
        <p class="hero-role"><strong>{e(h['lead'])}</strong><span>{e(h['accent'])}</span></p>
        <p class="hero-intro">{e(h['description'])}</p>
        <div class="hero-actions">
          <a class="action-primary" href="#experience">{e(data['nav']['experience'])}<span aria-hidden="true">↗</span></a>
          <a class="action-secondary" href="resume/">{e(data['nav']['resume'])}<span aria-hidden="true">↗</span></a>
        </div>
        <p class="hero-meta">{e(h['location'])}<span class="meta-sep" aria-hidden="true"></span>{e(h['current'])}</p>
      </div>
      <figure class="portrait" data-reveal>
        <img src="{p}photo.webp" alt="{e(h['photoAlt'])}" width="340" height="430" fetchpriority="high">
        <figcaption><span class="signal" aria-hidden="true"></span>{e(h['photoLabel'])}</figcaption>
      </figure>
    </div>
    <div class="hero-edge wrap"><span>01 — {e(data['nav']['about'])}</span><span class="scroll-line" aria-hidden="true"></span></div>
  </section>"""

def highlights_html(data):
    # Not KPI cards: a single compact typographic band.
    return f"""<div class="highlights"><div class="wrap highlight-items">
    {concat(f'<div class="highlight"><strong>{e(item["value"])}</strong><span>{e(item["label"])}</span></div>' for item in data['proof'])}
  </div></div>"""

def section_head(data, key, title, intro=None):
    kicker = data["section"][key]
    note = f'<p class="section-note">{e(intro)}</p>' if intro else ""
    return f'<div class="section-intro" data-reveal><p class="section-label">{e(kicker)}</p><h2 id="{key}-title">{e(title)}</h2>{note}</div>'

def about_html(data):
    x = data["about"]
    values = concat(
        f'<li class="principle" data-reveal><span class="principle-number">{e(p["num"])}</span><div><span class="principle-tag">{e(p["eyebrow"])}</span><h3>{e(p["title"])}</h3><p>{e(p["text"])}</p></div></li>'
        for p in x["cards"]
    )
    return f"""<section id="about" class="content-section section-about" aria-labelledby="about-title">
    <div class="wrap section-layout">
      {section_head(data,"about",x["title"],x["note"])}
      <div class="section-detail"><p class="lead-copy" data-reveal>{e(x["intro"])}</p>
        <ol class="principles">{values}</ol>
      </div>
    </div></section>"""

def job_html(job):
    items = concat(f"<li>{e(v)}</li>" for v in job["bullets"])
    signal = f'<p class="job-signature">{e(job["highlight"])}</p>' if job.get("highlight") else ""
    return f"""<article class="job" data-reveal>
      <div class="job-meta"><time>{e(job['period'])}</time><p>{e(job['company'])}</p></div>
      <div class="job-main"><h3>{e(job['role'])}</h3><ul>{items}</ul>{signal}</div>
    </article>"""

def earlier_html(row):
    date, company, role = row
    return f'<div class="earlier-row"><time>{e(date)}</time><span>{e(role)}</span><span>{e(company)}</span></div>'

def experience_html(data):
    x = data["experience"]
    jobs = concat(job_html(j) for j in x["jobs"])
    earlier = concat(earlier_html(j) for j in x["early"])
    return f"""<section id="experience" class="content-section section-experience" aria-labelledby="experience-title">
      <div class="wrap section-layout">
        {section_head(data,"experience",x["title"],x["summary"])}
        <div class="section-detail"><div class="jobs">{jobs}</div>
          <details class="earlier"><summary>{e(x["older"])} <span aria-hidden="true">＋</span></summary><div class="earlier-list">{earlier}</div></details>
        </div>
      </div>
    </section>"""

def expertise_html(data):
    x = data["expertise"]
    groups = concat(
        f'<div class="skill-group" data-reveal><h3>{e(group["label"])}</h3><ul>{concat(f"<li>{e(item)}</li>" for item in group["items"])}</ul></div>'
        for group in x["groups"]
    )
    return f"""<section id="expertise" class="content-section section-expertise" aria-labelledby="expertise-title">
      <div class="wrap section-layout">
        {section_head(data,"expertise",x["title"])}
        <div class="section-detail"><div class="skill-groups">{groups}</div></div>
      </div>
    </section>"""

def qualification_html(data):
    x = data["qualifications"]
    training = concat(f'<div class="qualification-row"><span>{e(a)}</span><small>{e(b)}</small></div>' for a,b in x["training"])
    languages = concat(f'<div class="qualification-row"><span>{e(a)}</span><small>{e(b)}</small></div>' for a,b in x["languages"])
    return f"""<section id="qualifications" class="content-section section-qualifications" aria-labelledby="qualifications-title">
      <div class="wrap section-layout">
        {section_head(data,"qualifications",x["title"])}
        <div class="section-detail qualification-groups">
          <div class="qualification-group" data-reveal><h3>{e(x["trainingTitle"])}</h3>{training}
            <h3 class="education-heading">{e(x["educationTitle"])}</h3><p class="education-note">{e(x["education"])}</p>
          </div>
          <div class="qualification-group" data-reveal><h3>{e(x["languagesTitle"])}</h3>{languages}</div>
        </div>
      </div>
    </section>"""

def contact_html(data):
    x = data["contact"]
    social = concat(
        f'<a href="{e(data[key])}" target="_blank" rel="noopener noreferrer">{e(label)} <span aria-hidden="true">↗</span></a>'
        for key,label in [("linkedin","LinkedIn"),("github","GitHub"),("telegram","Telegram")]
    )
    return f"""<section id="contact" class="content-section section-contact" aria-labelledby="contact-title">
      <div class="wrap section-layout">
        {section_head(data,"contact",x["title"],x["intro"])}
        <div class="section-detail contact-detail" data-reveal>
          <a class="contact-email" href="mailto:{e(data['email'])}">{e(data['email'])}<span aria-hidden="true">↗</span></a>
          <a class="contact-phone" href="tel:{e(data['telephone'])}">{e(data['phone'])}</a>
          <nav class="social" aria-label="Social profiles">{social}</nav>
          <p class="contact-availability"><span class="signal" aria-hidden="true"></span>{e(x["availability"])}</p>
        </div>
      </div>
    </section>"""

def site_html(data):
    ru = data["lang"]=="ru"
    prefix = "../" if ru else ""
    switch = "../" if ru else "ru/"
    dest = "EN" if ru else "RU"
    root = "../" if ru else "./"
    skip = "Перейти к содержимому" if ru else "Skip to content"
    return f"""<!doctype html>
<html lang="{e(data['lang'])}">
<head>
{meta_html(data,ru)}
</head>
<body>
<a class="skip-link" href="#main">{skip}</a>
<header class="site-header">
 <div class="wrap header-inner">
  <a class="wordmark" href="{root}" aria-label="{e(data['name'])}"><span>{e(data['name'])}</span><small>Head of IT</small></a>
  <nav class="main-nav" id="main-navigation" aria-label="Main navigation" data-nav>{nav_html(data,ru)}</nav>
  <div class="header-actions"><a class="language" href="{switch}" hreflang="{('en' if ru else 'ru')}">{dest}</a><a class="resume-link" href="resume/">{e(data['nav']['resume'])} <span aria-hidden="true">↗</span></a></div>
  <button class="menu-toggle" type="button" aria-label="{e(data['nav']['openMenu'])}" aria-controls="main-navigation" aria-expanded="false" data-menu-button><span></span><span></span><span></span></button>
 </div>
 <div class="progress-track" aria-hidden="true"><div class="progress-line" data-progress></div></div>
</header>
<main id="main">
{hero_html(data,ru)}
{highlights_html(data)}
{about_html(data)}
{experience_html(data)}
{expertise_html(data)}
{qualification_html(data)}
{contact_html(data)}
</main>
<footer class="site-footer"><div class="wrap footer-inner"><span>© 2026 {e(data['name'])}</span><span>{e(data['footer'])}</span></div></footer>
</body></html>"""

def resume_html(data):
    # Intentionally simple, single-column ATS/recruiter markup.
    ru = data["lang"]=="ru"
    r = data["resume"]; x=data["experience"]; q=data["qualifications"]
    root = "../../" if ru else "../"
    jobs = concat(
        f'<section class="resume-job"><h3>{e(job["role"])} — {e(job["company"])}</h3><p class="period">{e(job["period"])}</p><ul>{concat(f"<li>{e(t)}</li>" for t in job["bullets"])}</ul></section>'
        for job in x["jobs"]
    )
    skills = ", ".join(e(v) for group in data["expertise"]["groups"] for v in group["items"][:4])
    training = "; ".join(e(a)+" — "+e(b) for a,b in q["training"])
    langs = "; ".join(e(a)+" — "+e(b) for a,b in q["languages"])
    return f"""<!doctype html>
<html lang="{e(data['lang'])}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,follow"><title>{e(data['name'])} · {e(r["label"])}</title>
<style>
:root{{--accent:#B5523A;--ink:#3E2A1F;--muted:#806D61}}
body{{font:15px/1.5 Arial,sans-serif;color:#222;max-width:790px;margin:0 auto;padding:34px 38px;background:#fff}}
a{{color:inherit}}h1{{font-size:30px;letter-spacing:-.035em;margin:0 0 2px}}h2{{font-size:15px;letter-spacing:.07em;text-transform:uppercase;border-bottom:1px solid #dac7b7;color:var(--ink);padding-bottom:6px;margin:22px 0 11px}}h3{{font-size:14px;margin:13px 0 2px}}p{{margin:5px 0}}.role{{color:var(--accent);font-size:16px;font-weight:700}}.print-toolbar{{background:#F8EFE6;padding:12px 14px;margin-bottom:24px;display:flex;justify-content:space-between;align-items:center;gap:14px}}button{{background:var(--accent);border:0;padding:9px 12px;color:white;border-radius:5px;cursor:pointer;font-weight:700}}header{{padding-bottom:15px;border-bottom:2px solid var(--accent)}}.resume-job{{break-inside:avoid;margin:0 0 12px}}.period{{color:var(--muted);font-size:12px}}ul{{padding-left:19px;margin:7px 0}}li{{margin:3px 0}}.note{{color:var(--muted);font-size:12px}}@media(max-width:500px){{body{{padding:18px}}.print-toolbar{{display:grid}}}}@page{{size:A4;margin:14mm 16mm}}@media print{{body{{max-width:none;padding:0;font:10.5pt/1.4 Arial,sans-serif}}.print-toolbar{{display:none}}h1{{font-size:22pt}}h2{{font-size:12pt;margin:14px 0 8px}}h3{{font-size:10.5pt}}.resume-job{{break-inside:avoid}}}}
</style></head><body>
<div class="print-toolbar"><a href="{root}">{e(r["web"])} ↗</a><button type="button" onclick="window.print()">{e(r["print"])}</button></div>
<header><h1>{e(data["name"])}</h1><p class="role">{e(r["role"])}</p>
<p><a href="mailto:{e(data["email"])}">{e(data["email"])}</a> · <a href="tel:{e(data["telephone"])}">{e(data["phone"])}</a> · Uzbekistan</p>
<p><a href="{e(data["linkedin"])}">LinkedIn</a> · <a href="{e(data["github"])}">GitHub</a></p></header>
<main><h2>{e(r["summaryTitle"])}</h2><p>{e(r["summary"])}</p>
<h2>{e(r["strengthsTitle"])}</h2><p>{skills}</p>
<h2>{e(r["experienceTitle"])}</h2>{jobs}
<h2>{e(r["educationTitle"])}</h2><p>{e(q["education"])}</p><p>{training}</p>
<h2>{e(r["languagesTitle"])}</h2><p>{langs}</p>
<p class="note">{e(r["notice"])}</p></main></body></html>"""

def build():
    for lang in ("en","ru"):
        source = DATA / f"{lang}.json"
        data = json.loads(source.read_text(encoding="utf-8"))
        assert data["lang"]==lang
        assert not data["projects"], "Portfolio work must remain hidden until approved"
        dest = ROOT / ("ru/index.html" if lang=="ru" else "index.html")
        out = ROOT / ("ru/resume/index.html" if lang=="ru" else "resume/index.html")
        dest.write_text(site_html(data), encoding="utf-8")
        out.write_text(resume_html(data), encoding="utf-8")
        print(f"BUILT {dest.relative_to(ROOT)} ({dest.stat().st_size} bytes)")
        print(f"BUILT {out.relative_to(ROOT)} ({out.stat().st_size} bytes)")

if __name__=="__main__":
    build()
