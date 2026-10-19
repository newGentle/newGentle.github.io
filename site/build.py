from pathlib import Path
from html import escape as esc
import json
ROOT=Path(r"C:\Users\Public\newgentle-cv-pr-20261019")
def e(v):return esc(str(v),quote=True)
def rowlist(rows,fmt):return "\n".join(fmt(x) for x in rows)
def build(d):
 ru=d["lang"]=="ru"; pre="../" if ru else ""; lang=d["lang"]; nav=d["nav"]; hero=d["hero"]; sec=d["section"]; work=d["work"]; ab=d["about"]; ex=d["experience"]; qual=d["qualifications"]; ct=d["contact"]
 alternate="../" if ru else "ru/"
 home="../" if ru else "./"
 def navlink(k,ref):return f'<a href="#{ref}">{e(nav[k])}</a>'
 def proof(p):return f'<div class="proof-item"><strong>{e(p["value"])}</strong><span>{e(p["label"])}</span><small>{e(p["detail"])}</small></div>'
 def principle(p):return f'<article class="principle"><span class="number">{e(p["num"])}</span><p class="label">{e(p["eyebrow"])}</p><h3>{e(p["title"])}</h3><p>{e(p["text"])}</p></article>'
 def case(p):
  diagram="" if not p["diagram"] else f'<div class="case-diagram"><p class="case-diagram-label">{e(work["diagramLabel"])}</p><div class="diagram-flow">'+'<span class="diagram-arrow" aria-hidden="true">→</span>'.join(f'<div class="diagram-node">{e(t)}</div>' for t in p["diagram"])+'</div></div>'
  facts=''.join(f'<div class="fact"><dt>{e(work[k])}</dt><dd>{e(p[k])}</dd></div>' for k in ("challenge","action","outcome"))
  tags=''.join(f'<span>{e(t)}</span>' for t in p["chips"])
  return f'<article class="case {"case-wide" if p["featured"] else ""}" id="case-{e(p["id"])}"><div class="case-head"><div class="case-top"><span class="case-index">{e(work["caseLabel"])} / {e(p["no"])}</span><span class="status {"status-operational" if p["statusKind"]=="operational" else ""}">{e(p["status"])}</span></div><p class="case-kind">{e(p["category"])}</p><h3>{e(p["title"])}</h3></div><div class="case-main"><dl class="case-info">{facts}</dl>{diagram}</div><div class="case-tags">{tags}</div></article>'
 def job(j):
  return f'<article class="job"><div><div class="job-date">{e(j["period"])}</div><div class="job-company">{e(j["company"])}</div></div><div><h3>{e(j["role"])}</h3><ul>{"".join("<li>"+e(t)+"</li>" for t in j["bullets"])}</ul>{("<p class=\"job-spot\">"+e(j["highlight"])+"</p>") if j.get("highlight") else ""}</div></article>'
 def expertise(g):return f'<article class="skill"><h3>{e(g["label"])}</h3><ul>{"".join("<li>"+e(t)+"</li>" for t in g["items"])}</ul></article>'
 def qr(pair):return f'<div class="qual-row"><strong>{e(pair[0])}</strong><span>{e(pair[1])}</span></div>'
 def early(t):return f'<div class="older-row"><div><b>{e(t[2])}</b><div>{e(t[1])}</div></div><span>{e(t[0])}</span></div>'
 title=d["meta"]["title"];descr=d["meta"]["description"];canonical="https://newgentle.github.io/"+("ru/" if ru else "");alternate_url="https://newgentle.github.io/"+("" if ru else "ru/");portrait=pre+"photo.webp"
 mark='<span class="mark">A<b>·</b>A</span>'
 printview=("ru/resume/" if not ru else "resume/")
 html=f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(descr)}"><meta name="theme-color" content="#0b1d2b">
<link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="en" href="https://newgentle.github.io/"><link rel="alternate" hreflang="ru" href="https://newgentle.github.io/ru/">
<link rel="icon" type="image/svg+xml" href="{pre}assets/favicon.svg"><link rel="stylesheet" href="{pre}assets/site.css">
<meta property="og:type" content="profile"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(descr)}"><meta property="og:image" content="https://newgentle.github.io/photo.webp"><meta property="og:url" content="{canonical}">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"Person","name":d["name"],"jobTitle":"Head of IT Department","url":canonical,"image":"https://newgentle.github.io/photo.webp","sameAs":[d["github"],d["linkedin"]]},ensure_ascii=False)}</script>
<script src="{pre}assets/site.js" defer></script></head><body>
<a class="skip" href="#main">{"Перейти к содержанию" if ru else "Skip to content"}</a>
<header class="site-header"><div class="wrap nav">
<a class="logo" href="{home}" aria-label="{e(d["name"])}">{mark}<span class="brand">{e(d["name"])}<small>Head of IT · Systems integration</small></span></a>
<nav id="site-nav" class="links" aria-label="{"Навигация" if ru else "Main navigation"}" data-nav="true" data-open="false">{navlink("about","about")}{navlink("work","work")}{navlink("experience","experience")}{navlink("expertise","expertise")}{navlink("contact","contact")}</nav>
<div class="nav-actions"><a class="lang" href="{alternate}" hreflang="{"en" if ru else "ru"}">{"EN" if ru else "RU"}</a><a class="cta" href="{printview}">{e(nav["resume"])} ↗</a></div><button type="button" class="menu-button" aria-expanded="false" aria-controls="site-nav" aria-label="{e(nav["openMenu"])}" data-menu-button>☰</button></div></header>
<main id="main">
<section class="hero" id="top" aria-labelledby="hero-title"><div class="wrap hero-grid"><div><p class="eyebrow">{e(hero["eyebrow"])}</p><p class="hero-name">{e(d["name"])}</p>
<h1 id="hero-title">{e(hero["lead"])}<br><em>{e(hero["accent"])}</em></h1><p class="hero-description">{e(hero["description"])}</p>
<div class="actions"><a class="btn btn-primary" href="#work">{e(hero["primary"])} ↗</a><a class="btn btn-secondary" href="{printview}">{e(hero["secondary"])} ↗</a></div><div class="meta-line"><span>{e(hero["location"])}</span><span>{e(hero["current"])}</span></div></div>
<figure class="portrait"><img src="{portrait}" alt="{e(hero["photoAlt"])}" width="330" height="413" fetchpriority="high"><figcaption>{e(hero["photoLabel"])}</figcaption></figure>
</div></section>
<div class="wrap"><div class="proof" aria-label="{"Фокус" if ru else "Focus"}">{rowlist(d["proof"],proof)}</div></div>
<section class="section" id="about" aria-labelledby="about-title"><div class="wrap"><p class="kicker">{e(sec["about"])}</p><div class="about-layout"><div><h2 id="about-title">{e(ab["title"])}</h2></div><div><p class="about-text">{e(ab["intro"])}</p><p class="about-note">{e(ab["note"])}</p></div></div><div class="principles">{rowlist(ab["cards"],principle)}</div></div></section>
<section class="section section-soft" id="work" aria-labelledby="work-title"><div class="wrap"><p class="kicker">{e(sec["work"])}</p><h2 id="work-title">{e(work["title"])}</h2><p class="section-intro">{e(work["intro"])}</p><div class="project-list">{rowlist(d["projects"],case)}</div></div></section>
<section class="section" id="experience" aria-labelledby="experience-title"><div class="wrap"><p class="kicker">{e(sec["experience"])}</p><h2 id="experience-title">{e(ex["title"])}</h2><p class="section-intro">{e(ex["summary"])}</p><div class="experience-list">{rowlist(ex["jobs"],job)}</div><details class="older"><summary>{e(ex["older"])} · {e(ex["expand"])}</summary><div class="older-list">{rowlist(ex["early"],early)}</div></details></div></section>
<section class="section section-soft" id="expertise" aria-labelledby="expertise-title"><div class="wrap"><p class="kicker">{e(sec["expertise"])}</p><h2 id="expertise-title">{e(d["expertise"]["title"])}</h2><div class="skills">{rowlist(d["expertise"]["groups"],expertise)}</div></div></section>
<section class="section" id="qualifications" aria-labelledby="qualifications-title"><div class="wrap"><p class="kicker">{e(sec["qualifications"])}</p><h2 id="qualifications-title">{e(qual["title"])}</h2><div class="qual-grid"><div><h3>{e(qual["trainingTitle"])}</h3>{rowlist(qual["training"],qr)}<h3>{e(qual["educationTitle"])}</h3><p class="education">{e(qual["education"])}</p></div><div><h3>{e(qual["languagesTitle"])}</h3>{rowlist(qual["languages"],qr)}</div></div></div></section>
<section class="contact-section" id="contact" aria-labelledby="contact-title"><div class="wrap contact-grid"><div><p class="kicker">{e(sec["contact"])}</p><h2 id="contact-title">{e(ct["title"])}</h2><p>{e(ct["intro"])}</p><p class="contact-note">{e(ct["availability"])}</p></div><div class="contact-links"><a href="mailto:{e(d["email"])}">{e(d["email"])}</a><a href="tel:{e(d["telephone"])}">{e(d["phone"])}</a><div class="social"><a href="{e(d["linkedin"])}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><a href="{e(d["github"])}" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="{e(d["telegram"])}" target="_blank" rel="noopener noreferrer">Telegram ↗</a></div><a class="print-link" href="{printview}">{e(nav["download"])} ↗</a></div></div></section>
</main><footer class="footer"><div class="wrap"><span>© 2026 {e(d["name"])}</span><span>{e(d["footer"])}</span></div></footer></body></html>'''
 out=ROOT/("ru/index.html" if ru else "index.html");out.write_text(html,encoding="utf-8");print("BUILT",out,len(html))
 resume=d["resume"]
 resume_head=f'<header><h1>{e(d["name"])}</h1><p class="role">{e(resume["role"])}</p><p><a href="mailto:{e(d["email"])}">{e(d["email"])}</a> · <a href="tel:{e(d["telephone"])}">{e(d["phone"])}</a> · Uzbekistan</p><p><a href="{e(d["linkedin"])}">LinkedIn</a> · <a href="{e(d["github"])}">GitHub</a> · <a href="{e(canonical)}">{e(resume["web"])}</a></p></header>'
 def rjob(j):return f'<section class="job"><h3>{e(j["role"])} — {e(j["company"])}</h3><p class="period">{e(j["period"])}</p><ul>{"".join("<li>"+e(t)+"</li>" for t in j["bullets"])}</ul></section>'
 def proj(p):return f'<section class="project"><h3>{e(p["title"])} <span>· {e(p["status"])}</span></h3><p><b>{e(work["action"])}:</b> {e(p["action"])}</p><p><b>{e(work["outcome"])}:</b> {e(p["outcome"])}</p></section>'
 strengths=" · ".join([", ".join(g["items"][:4]) for g in d["expertise"]["groups"]])
 resume_html=f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,follow"><title>{e(d["name"])} · {e(resume["label"])}</title><link rel="icon" href="{pre}../assets/favicon.svg" type="image/svg+xml"><style>body{{font:15px/1.47 Arial,sans-serif;color:#1c2932;max-width:810px;margin:0 auto;padding:34px 38px}}h1{{font-size:30px;margin:0 0 3px}}h2{{font-size:16px;color:#0b5360;text-transform:uppercase;letter-spacing:.05em;border-bottom:1px solid #b9ced5;padding-bottom:5px;margin:23px 0 11px}}h3{{font-size:14px;margin:12px 0 2px}}p{{margin:5px 0}}header{{border-bottom:2px solid #0c6e73;padding-bottom:16px}}a{{color:inherit}}.role{{font-size:16px;font-weight:700;color:#096d72}}.job,.project{{break-inside:avoid;margin-bottom:12px}}.period,.project span{{color:#6d7d83;font-size:12px}}ul{{margin:7px 0;padding-left:18px}}li{{margin:3px 0}}.toolbar{{background:#ebf5f4;padding:10px;border-radius:8px;margin-bottom:20px;display:flex;justify-content:space-between;gap:10px}}button{{background:#0d5c60;color:white;border:0;padding:9px 13px;border-radius:6px;cursor:pointer}}.small{{font-size:12px;color:#52646c}}@page{{size:A4;margin:15mm 16mm}}@media print{{body{{max-width:none;padding:0;font:10.5pt/1.4 Arial,sans-serif}}.toolbar{{display:none}}h1{{font-size:22pt}}h2{{font-size:12pt;margin:14px 0 7px}}h3{{font-size:10.5pt}}.job,.project{{break-inside:avoid}}}}@media(max-width:500px){{body{{padding:22px 18px}}.toolbar{{display:grid}}}}</style></head><body><div class="toolbar"><a href="{("../" if not ru else "../../")}">{e(resume["web"])} ↗</a><button onclick="window.print()">{e(resume["print"])}</button></div>{resume_head}
<h2>{e(resume["summaryTitle"])}</h2><p>{e(resume["summary"])}</p>
<h2>{e(resume["strengthsTitle"])}</h2><p>{e(strengths)}</p>
<h2>{e(resume["experienceTitle"])}</h2>{rowlist(ex["jobs"],rjob)}
<h2>{e(resume["workTitle"])}</h2>{rowlist(d["projects"],proj)}
<h2>{e(resume["educationTitle"])}</h2><p>{e(qual["education"])}</p><p>{"; ".join(e(x[0])+" — "+e(x[1]) for x in qual["training"])}</p>
<h2>{e(resume["languagesTitle"])}</h2><p>{", ".join(e(x[0])+" — "+e(x[1]) for x in qual["languages"])}</p>
<p class="small">{e(resume["notice"])}</p></body></html>'''
 p=ROOT/("ru/resume/index.html" if ru else "resume/index.html");p.write_text(resume_html,encoding="utf-8");print("BUILT",p,len(resume_html))
for l in ("en","ru"):build(json.loads((ROOT/"site/content"/(l+".json")).read_text(encoding="utf-8")))
