# Executive CV — Draft PR review

**Status:** Candidate for review only. Do not merge or publish without separate explicit approval.

## Change summary
- Executive-first positioning: IT leadership, infrastructure, integrations and reliable delivery.
- EN/RU site generated from `site/content/en.json` and `site/content/ru.json`, using `site/build.py`.
- Shared responsive styling and lightweight navigation in `assets/site.css` / `assets/site.js`, SVG favicon.
- Five case studies structured as challenge / personal contribution / outcome or status; three diagrams are explicitly **conceptual**, not application screenshots.
- Standalone recruiter-oriented HTML CV at `resume/` and `ru/resume/`, designed for print-to-PDF.
- The existing portrait `photo.webp` is reused.
- No added third-party scripts, external assets, analytics, internal URLs or production files.

## Local validation
1. `python site/build.py`
2. `python cv_validate.py` — checks both site languages and both recruiter CVs, local assets, anchors and project statuses.
3. Desktop browser QA: Chrome 155, EN/RU, viewport widths 1440 / 768 / 390 / 320 pixels: no horizontal overflow or page errors; portrait loads; mobile menu opens.
4. Both recruiter CV pages rendered as printable PDFs through Chrome.

## Publication blockers / fact-checking
- Confirm that the company name and public references to SAYANA / ForgeMCP / FaceID are authorized.
- Reconfirm project deployment statuses: Director, Cash, attendance, network observability, ForgeMCP and Mobile Portal.
- Verify public phone/email/LinkedIn, employment dates, language levels and course completions.
- Collect approved quantitative outcomes (team size, locations, served endpoints, availability, time savings etc.) before advertising any numbers. None have been invented.
- Conceptual system diagrams intentionally do not depict production screens, infrastructure addresses or real records.
- Test keyboard focus, screen reader flows, performance metrics and PDF pagination before approving any public release.

## Merge gate
Production branch: `gh-pages`; the branch must remain unchanged. Do not merge without new user authorization.
