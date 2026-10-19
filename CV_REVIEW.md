# Executive CV — Draft PR review

**DRAFT ONLY — NO MERGE / PUBLICATION**

## Current review scope (SAYANA-brand revision)
- The header is text-only: removed the AA icon/monogram; the website no longer links to its prior favicon.
- Selected Projects/Work section and navigation links are removed from EN and RU pages. Project entries are omitted from EN/RU recruiter resumes. Project material remains recoverable from earlier Git history (commit 820eea7).
- Visual language references approved SAYANA Brand Tokens v2.2 from `newGentle/clinik_report/director_dashboard/react_app/src/brand/sayana-tokens.css`: Terracotta #B5523A, Cream #F8EFE6, Deep Brown #3E2A1F, Rose Clay #D9A08C. Aura Teal #58B8AE remains a secondary brand accent.
- Layout retains four sections after introduction: Approach, Experience, Expertise, Qualifications and Contacts.
- EN/RU pages generated using `site/build.py` from `site/content/*.json`; ATS-focused one-column HTML resumes remain available.

## Tests
`python site/build.py`
`python cv_validate.py` -> PASS all four pages
Chrome 155 headless EN/RU at widths 1440, 768, 390 and 320 -> no overflow, no JS errors, loaded portrait and working mobile menu, 0 visible project cards.
Recruiter resume print-to-PDF has been generated for both languages. Visual PDF pagination, full WCAG and Lighthouse are pending.

## Publication gate
Verify employment data, language/education claims, contact information, and permission to mention internal organizations before approving a future deployment. No merge or publication without explicit approval.
