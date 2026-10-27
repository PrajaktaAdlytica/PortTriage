# PortTriage — first website build

A responsive concept website combining Harbor Atlas (direction 1) and Evidence Edition (direction 3).

## Run locally

```sh
npm install
npm run dev -- --host 127.0.0.1 --port 4281 --strictPort
```

Open http://127.0.0.1:4281 . Build with `npm run build`; verify hosting behavior with `npm run test:sites`.

## Included

- Original generated logo, favicon, harbor illustration, nautical map and evidence dossier assets.
- Local Newsreader display typography and DM Sans interface typography.
- Ivory, navy, sky blue and rose identity; keyboard focus/hover states and responsive navigation.
- GSAP reveals from left/right/up, entrance choreography and a pinned horizontal four-scene story; Lenis smooth scrolling.
- Short-screen and mobile vertical story layouts; OS reduced-motion fallback.
- Five independent product pages with module-specific preview cards, workflow, input/output boundaries and pilot status.
- Platform, features, why-change, integrations, trust, comparison, results, pilot and company pages.
- Four audience pages and three resource articles, including the complete research-stage business context.
- Hypothetical pricing, contact/review form, sign-in/access explanations, privacy/terms drafts and 404.
- Ten fictional cases; queue search/status filters; separate vessel/container/handoff events; source timestamps; pending review; approve/reject/reset; audit history; replay and report export.
- Every editorial chapter has a supporting evidence, responsibility, comparison, target or workflow diagram.

## Honest scope

This is a local frontend concept, not an operating logistics platform. There are no live integrations, message sending, terminal access, appointment changes, payment, real authentication or installed analytics. Forms prepare downloadable local request drafts and do not send leads. Demo state is held in memory. Sixteen key routes were checked in-browser, along with mobile homepage/product/workbench, review-state changes, source pane, local form success and empty-search feedback. See design-qa.md for evidence and limits.

Data rights, a signed paid pilot and retrospective lift remain integration gates. The demo approval applies to a message draft; it does not mark a case resolved. PEX-014 is the detailed timeline fixture. The other nine cases have compact synthetic case notes. The resolved replay is a separate prerecorded scenario, not an action executed by this demo.

## Structure

- src/App.jsx: routes and visual components
- src/data.js: proposed products, fictional fixtures and editorial copy
- src/styles.css: brand, responsive layout, component styling
- public/assets: optimized original image assets
- qa: actual browser captures and visual comparison
- docs/PortTriage-website-architecture.html: full planning package
- docs/PortTriage-builder-brief.json and docs/PortTriage-fixture-schema.json: builder handoff

## Asset provenance

Original AI-generated concept imagery, created for this task. No vendor logos, screenshots or maps were copied. The fictional map is illustrative and not navigational. Phosphor provides interface icons. Font packages bundle their licenses in node_modules. External DCSA and project44 links are reference reading and do not imply affiliation.

## Before public launch

Connect an authorized lead destination and consent-aware analytics, supply the real company/legal identity, review legal notices, validate data claims, configure production authentication if needed, run cross-browser/accessibility testing, then deploy and connect a verified domain. No deployment or domain connection was performed in this build.


## October 27 visual refresh

Shared cool-white theme, animated water backgrounds, interactive evidence dossier, unique module visuals, stacked product receipts and a dark editorial footer. Use the footer Water motion control to pause background motion. Reduced-motion preferences and offscreen pausing are supported. New original assets: `ocean-water-v2.webp` and `evidence-folio-v2.webp`. See `design-qa.md` and `qa/v2/research.html` for verification and references.


## Current handoff — 27 October 2026

Includes the latest six-second homepage intro, stationary ship, animated ocean overlays, upright title, automatic hero handoff and reduced-motion alternative. This is a browser animation, not an MP4. The user rejected the intro's visual quality; that remains unresolved. Functional QA passing is not visual approval.

Includes SVG branding, concept frames, assets, planning and QA evidence. Dependencies and generated builds are excluded. Reproduce with `npm ci` and `npm run build`. No backend or deployment is included.
