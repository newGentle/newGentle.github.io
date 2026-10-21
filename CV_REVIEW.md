# Executive CV / engineering-leader redesign - visual QA

Date: 2026-10-21. Status: Draft PR only; not released or merged.

## Design direction
- The user-selected suszczynski.dev/#hero is a visual reference only. Globe geometry and rendering are independently implemented.
- Deep navy background; turquoise technical lines; warm terracotta/orange accents.
- Canvas 3D projected globe with latitude/longitude grid and illuminated nodes, placed behind the approved portrait.
- Reduced-motion support; globe pauses when hero is not visible or document is hidden.
- EN/RU biography, career, expertise, qualifications and contact remain. Projects remain hidden.
- User-confirmed scale: IT team of five including the user; four direct reports; approximately 300 employees served at one six-storey clinic.
- No internal network identifiers, patient data or credentials included.

## QA
- python cv_validate.py: PASS all four pages.
- Chrome: English/Russian at 1440, 768, 390 and 320 px.
- No horizontal overflow, JavaScript errors or broken internal anchors; portrait loads; mobile menu works; canvas renders.
- Browser screenshots: C:/Users/Public/cv-audit-executive-20261021.
- Recruiter resumes remain separate. Active web assets: assets/style.css, assets/executive-design.css, assets/app.js, assets/executive-globe.js.
- Formal WCAG audit, career-date verification and publication approval are still pending.

## Release gate
The production gh-pages branch is untouched. Do not merge or publish without explicit user approval.
