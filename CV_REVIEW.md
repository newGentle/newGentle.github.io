# Executive CV · unified SAYANA engineering-leader design

Draft only. No merge, deployment or production changes approved.

## Scope of the update
- Entire portfolio site (not only hero) redesigned to one dark executive/engineering visual system.
- SAME design across introduction, career timeline, skills, training and languages, contact, and footer.
- SAYANA palette: Terracotta #B5523A, Rose Clay #D9A08C, Deep Brown #3E2A1F, Aura Teal #58B8AE, Cream #F8EFE6.
- Soft reveal-on-scroll via IntersectionObserver and light ambient background motion; supports prefers-reduced-motion. Scroll progress and active section affordances. No external JavaScript dependencies.
- Logos and project section remain absent from both languages and recruiter CVs. Public production references and project metrics are intentionally omitted.
- Separate single-column recruiter/ATS-oriented CVs remain available in resume/ and ru/resume/.

## Quality gates
- Build: python site/build.py.
- Four-page structure validation: python cv_validate.py.
- Browser QA: Chrome 155; EN and RU at widths 1440, 768, 390 and 320; no JS errors, no broken anchors, no horizontal overflow; portrait renders; mobile menu opens.
- Browser screenshots reviewed for EN/RU desktop and mobile.
- Full Lighthouse, WCAG and print pagination review remain future tasks; do not claim these checks passed.

## Release gate
Review details of job history, language levels, courses, and public contact fields before publication. Do not merge the Draft PR or publish without separate explicit approval.
