# Visual refresh — 27 October 2026

final result: passed (local frontend scope)

## Reference and comparison

User reference: `qa/v2/source-reference.jpg`, 1024 × 1536. Actual desktop captures are 1440 × 900; mobile captures 390 × 844. `qa/v2/comparison.jpg` combines the supplied board with actual evidence and footer captures and was visually inspected. This is an adaptation of selected elements, not a pixel-identical clone: approved hero artwork remains, the source design-spec strip becomes a navigable company footer, and fictional evidence retains consistent source records.

## Changes verified

- Cool white #F6FBFF page foundation, white cards, sky-water sections and deep navy footer replace the dominant cream theme across shared page templates.
- Interactive evidence dossier, source/observed timestamps, Maya reviewer panel and activity ribbon; original folio art and three stacked receipts.
- Five different module visuals: lane map, evidence, appointment calendar, notice cards and illustrative count bars. Related product rails replace repeated full grids on detail pages.
- Slow transform-based water motion pauses offscreen, obeys reduced-motion preferences and has a working site-wide pause control. Existing Lenis/GSAP narrative remains.
- Pointer hover and keyboard focus treatments added to receipts, cards, navigation and CTAs.

## Findings and resolution

[P2 resolved] A mobile water opacity rule also lightened the dark footer. Added an explicit footer override; final mobile screenshot and computed opacity 0.1 verify the fix.

No unresolved P0/P1/P2 visual issues found in this refresh. Typography and spacing retain the established editorial serif/sans system; functional text is HTML rather than generated text. New images are original, optimized WebP assets. Reference cream is intentionally changed to cool white at the user's request.

## Validation

- Production build passed; all four Sites contract tests passed.
- Eight additional desktop routes checked: Desk, Signal, Report, platform, resources, pricing, request-demo and demo. No missing images or horizontal overflow. Review desktop and Proof mobile inspected separately.
- Receipt interaction verified; water animation measured running, then paused by its control, then restored. Browser error logs empty.
- Mobile evidence and footer fit 390 pixels without document overflow.
- Captures: `qa/v2/evidence-desktop.png`, `evidence-mobile.png`, `modules-desktop.png`, `product-receipts-desktop.png`, `footer-desktop.png`, `footer-mobile.png`. Machine-readable route checks: `qa/v2/route-checks.json`.
- Research and design rationale: `qa/v2/research.html`.

Limitations: local concept preview, not a deployment or live operational service. No real external messages, integrations or savings are represented. Reduced-motion behavior has stylesheet coverage; no separate OS preference screenshot was captured.

---

# PortTriage design QA

final result: passed

Scope: first local frontend build combining visual directions 1 and 3. This is not production-launch acceptance.

## Evidence

- Source visual truth: qa/visual-target.jpg, derived from generated hybrid exec-9ea096bb-e43e-4b55-bc08-b6b303f925e6.png. The user selected Harbor Atlas and Evidence Edition; the hybrid is the implementation interpretation of those directions.
- Source dimensions: 1122 × 1402 pixels; a multi-section visual board, not a browser capture with a known CSS viewport.
- Implementation: http://127.0.0.1:4281/ . Actual browser capture qa/home-desktop.png, 1440 × 900 pixels at a 1440 × 900 CSS viewport (1:1 pixels).
- Full-view comparison: qa/comparison.jpg (first comparison), qa/comparison-final.jpg (final composition).
- Focused hero comparison: qa/comparison-hero.jpg. Both crops are scaled to 700 pixels wide; source crop is 1122 × 560 and browser crop is 1440 × 780. Different source/viewport heights are explicit; this is an art-direction comparison, not a pixel-identical clone claim.
- Mobile: 390 × 844 CSS viewport, saved at 1:1 pixels in qa/home-mobile.png, qa/product-mobile.png, qa/demo-mobile.png and qa/demo-mobile-detail.png.
- Desktop detail captures: qa/product-desktop.png, qa/demo-desktop.png, qa/demo-evidence.png, qa/report-desktop.png and qa/platform-chapter.png.
- State: settled hero; detailed PEX-014 initially pending; evidence pane; mobile reviewer panel; fixed illustrative report counts.

## Comparison history and findings

1. [P2, resolved] Small hero-bottom text crossed a detailed photograph/illustration region. Added ivory backing to the two small edge labels. Final hero screenshot and comparison show readable text.
2. [P2, resolved] Scroll entrance transforms temporarily extended mobile document width from 390 to 402 pixels. Clipped the presentation overflow at main; subsequent DOM width check returned 390/390. Content remains accessible in normal flow.
3. [P1, resolved] Mobile workbench grid used intrinsic widths from the horizontal queue, stretching its case/reviewer panels. Explicit minmax(0,1fr), min-width:0 and bounded queue scrolling fixed the cause. Browser measured queue, case and action panels at 358 pixels within a 390-pixel viewport. Final mobile captures show filter, timeline and review controls in the page.
4. [P2, resolved] Compact two-column mobile product cards made text too small. Switched to single-column cards with larger labels and preview content.
5. [P2, resolved] PEX-014 sources and replay were shared by unrelated cases. Other records now show their own compact case-note evidence; the detailed delay replay is restricted to PEX-014. Completed/rejected fixtures retain their historical review state.
6. [P2, resolved] Timeline summaries only displayed an aggregate observation range. Each event now carries its source and observation time. Detailed evidence exposes event time, observed time, state, illustrative confidence and entitlement.
7. [P2, resolved] The synthetic-data label left view on mobile detail scroll. The demo banner now sticks below navigation. qa/demo-mobile-detail.png verifies both the label and the reviewer action in-frame.
8. [P2, resolved] A wide but short viewport could lose later horizontal-story scenes. Added short-screen grid fallback and matchMedia-controlled pinning. Browser scrolling at 1440 × 900 traversed the story and exited to the later sections.

## Required fidelity surfaces

- **Typography:** locally bundled Newsreader and DM Sans, deliberate serif display/sans UI contrast. Headlines wrap cleanly at desktop and 390 pixels. Source board has a heavier, tighter display face; the lighter Newsreader rhythm is an intentional Evidence Edition interpretation. Tiny provenance is supplemented by a readable evidence view.
- **Spacing/layout:** generous cinematic hero, bounded page width, alternating section compositions, modular cards and an operational three-column workbench. The full hero is taller than the compact source board, intentionally supporting the requested scroll narrative. Mobile stacks meaningful content and bounds only the queue/table for horizontal scrolling.
- **Colors/tokens:** navy #0F2C44, sky #5FADDD, rose #EC6E93 and ivory #F7F4EE. Text uses darker derived shades; rose state labels include text rather than relying on color alone. Hero edge-label contrast was corrected.
- **Image quality:** real original generated raster assets for harbor, atlas, dossier, logo and favicon. Optimized WebP illustrations total about 1.1 MB. The target's exact generated UI/text is replaced by functional HTML with accurate fictional provenance; no vendor screenshot or logo is represented as an integration. The nautical map is illustrative. Raster artwork is not replaced by CSS/SVG approximations.
- **Copy/content:** brand is PortTriage throughout. Five offers remain separable. Hypothesis pricing and pilot gates are explicit. No live feed, customer proof, savings, terminal release or notification authority is implied. The visible synthetic workbench is functional frontend UI.

## Interactions and verification

- Browser checked 16 key routes: all five products, platform, pricing, solutions, resources, company, integrations, comparison, report, pipeline, sign-in and privacy. qa/route-checks.json records nonempty headings, no broken images and no page-width overflow for those desktop checks.
- Desktop homepage scroll: reveal completion, pinned four-scene narrative and return to ordinary vertical sections.
- Mobile navigation open state, homepage, product detail, bounded exception queue and reviewer pane.
- Human approval: pending → approved in simulation; approve/reject controls disabled afterward; audit records decision and the reviewed draft. Reset returns to pending.
- Evidence tab: distinct sources and timestamps. Empty search: zero results with recovery text.
- Request form: fictional test data completed the local draft flow; success explicitly confirms nothing sent/no booking. The test did not transmit data.
- Report: four pending, two blocked, two completed, two rejected; no measured savings.
- Console error checks returned an empty error list in the browser after the verified interactions.
- npm run build passed. npm run test:sites passed all four hosting/route tests. Motion/vendor chunks are separated.

## Intentional deviations and residual checks

- Source-board generated vessel/container names and claims were replaced with coherent fictional records from the brief.
- Decorative route lines over the hero are not a live tracking representation. The atlas artwork and structured timeline carry the route/evidence story.
- No production backend, live feeds, payment, real auth, lead transmission or analytics is connected. No deployment was performed.
- Reduced-motion code and CSS are present, but OS-level preference emulation was not available in the browser capability used; test this on target devices before launch.
- Cross-browser/device, screen-reader and exhaustive keyboard/contrast testing remain prelaunch work. Local download buttons are implemented; downloaded payload inspection was not part of the browser pass.
- P3 polish: a future pass can add bespoke module-specific illustrations beyond the current shared atlas/dossier family, and refine route-line choreography after user feedback.

## Implementation checklist

- [x] Branding, favicon, local fonts and original illustration family.
- [x] Five module routes and supporting company/product/resource pages.
- [x] Scroll storytelling and narrow-screen fallbacks.
- [x] Isolated synthetic case workflow with evidence and human review.
- [x] Browser captures, comparison, mobile fixes, build and hosting checks.
- [ ] Public-launch integrations, operator/legal details, deployment and domain.

## Ribbon-free intro — October 27

Implemented a 14-second single-scene browser animation above the homepage hero. Original generated clean ocean plate and separate alpha ship replace the rose-ribbon concept. HTML typography and approved SVG logo stay sharp. This is not an exported video file.

Verified at 1440×900 and 390×844: no ribbons, readable composition, no mobile document overflow, no navigation over intro. Uninterrupted playback moved to the hero (scroll ~888px with navbar opacity 1). Pause freezes timeline and CSS water/ship animations; skip moves to hero. Manual scrolling cancels automatic handoff. Hidden tabs pause. Reduced-motion uses a static composition and explicit Continue control (code-reviewed; OS emulation not captured).

Build and all four Sites tests passed. Evidence: qa/v2/ocean-intro-desktop.png and qa/v2/ocean-intro-mobile.png. New source: src/OceanIntro.jsx and src/ocean-intro.css. Assets: public/assets/intro-ocean.webp and intro-ship.webp. No live tracking, external messaging or real operational data.


## GitHub handoff quick QA — 27 October 2026

Functional checks passed: build; four Sites tests; homepage, pricing, Port Desk, request-demo and demo routes had headings, no broken images, no page overflow and no captured browser errors. Current intro is six seconds with a fixed ship and animated texture overlays. Visual acceptance: NOT PASSED — user rejected the intro quality. No redesign attempted during quick-QA/push request.
