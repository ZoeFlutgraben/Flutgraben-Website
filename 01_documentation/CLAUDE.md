# Project Context

This is the **Flutgraben** website — a new public site for Flutgraben e.V., a Berlin-based art space and community. Built with HTML, CSS, and vanilla JavaScript. Replaces the current site at flutgraben.org entirely.

## About Flutgraben

Flutgraben e.V. is an art space and community in Berlin. The site's primary audience: artists in residence, external practitioners, and the general public discovering the space and its programming.

**Main objective:** present the space and what takes place in it. The home page is the entry point — it introduces the space and leads visitors into the site's sections.

**Tone:** artistic, unconventional, experimental. Warm, queer, culturally specific to the Berlin art scene. Avoid corporate structure, over-organized layouts, or standard institution aesthetics.

**Languages:** English by default. Language switcher (dropdown) in the global header. German and potentially French as additional languages.

### Visual identity

Flutgraben is designing its own display typeface to be used across its website and visual identity.

The typeface is built from atomic circular elements — dots and spots — whose edges dissolve outward like spray paint or halftone ink, giving characters a quality of reaching beyond their own boundaries.

The construction logic is geometric and modular, influenced by Bauhaus/Futura principles, but the visual result is organic and material.

The concept carries a deeper meaning: characters lean toward each other across whitespace, suggesting network, connection, and trans-individuality — rather than isolated, self-contained forms.

The visual identity includes a **grainy gradient generator** built as a creative tool to develop and explore identity assets — combining atomic dot patterns, scattered halos, and pixel grain to produce textures consistent with the typeface's aesthetic.

## Site Structure

Home page + 5 main sections + Impressum. Logo links to home page.

### Accueil — Main Page

Entry point of the site. Introduces Flutgraben — the space, its identity, and its programming. Leads visitors toward the main sections.

### Spree

Events and programming for the current year. The name references the river Spree — events flow through time like water.

| Subpage       | Scope                                        |
|---------------|----------------------------------------------|
| Upstream      | Past events from the current year            |
| In Flutgraben | Current month                                |
| Downstream    | Upcoming months within the current year      |
| Archive       | Past years — dropdown to select a year       |

The subnav component (segmented button group) is the standard navigation pattern used across all interior pages.

### Eddies

Everything that orbits the space — what Flutgraben generates and offers.

| Subpage   | Content                                                          |
|-----------|------------------------------------------------------------------|
| Overview  | What Flutgraben offers — general introduction                    |
| Moons     | How to join / gravitate around Flutgraben                        |
| Canteen   | Tuesday canteen cooked by an artist in residence                 |
| Rhizotype | Typography developed by and for Flutgraben — typeface presentation |
| Friends   | Partner organizations, collaborators (TBD)                       |

### Das Haus

The building — its architecture, people, and relationship to its environment.

| Subpage       | Content                                               |
|---------------|-------------------------------------------------------|
| Overview      | The building, its history, its spaces                 |
| Residents     | Artists and organizations based at Flutgraben         |
| News          | Building-related updates                              |
| Ecology       | Environmental practices and sustainability            |
| Accessibility | Access information (physical, sensory, financial)     |

### About

The organization — structure, values, how to engage.

| Subpage         | Content                                              |
|-----------------|------------------------------------------------------|
| Overview        | Who is Flutgraben e.V.                               |
| Mission         | Values, political and cultural positioning           |
| Structure       | Organizational structure (Vorstand, members, etc.)   |
| Members         | Current members of the association                   |
| Become a Member | How to join the association                          |
| Glossary        | Key terms and concepts used by the organization      |
| Donate          | How to support Flutgraben financially                |

### Bazar

Miscellaneous content — TBD. Navigation label: "other stuff".

### Impressum

Legal notice page. Standalone — accessible from the footer, not part of the main navigation.

| Content             |
|---------------------|
| Legal entity name and address |
| Contact information |
| Registration details (Vereinsregister) |
| Responsible person(s) |

## Design Tokens

### Colors

| Role       | Name       | Hex       | Usage                                      |
|------------|------------|-----------|--------------------------------------------|
| Background | Off-white  | `#e5e9ed` | Page background, large surfaces            |
| Text       | Rust       | `#573835` | Body text, headings, primary UI text       |
| Warm mid   | Terracotta | `#9f6861` | Secondary text, borders, subtle elements   |
| Accent     | Ochre      | `#c17d4c` | Highlights, links, hover states, CTAs      |
| Sky        | Dusty blue | `#7fb8d7` | Contrast accent, tags, secondary actions   |

### Typography

| Role        | Font                       | File                               | Usage                                     |
|-------------|----------------------------|------------------------------------|-------------------------------------------|
| Display     | FLUTGRABEN variable        | `FLUTGRABEN_variable.ttf`          | Hero titles, section headers, large text  |
| Display alt | FLUTGRABEN variable [RECT] | `FLUTGRABEN_variable[RECT].ttf`    | Alternate display, pull quotes            |
| Decorative  | FLUTGRABEN variable SPOT   | `FLUTGRABEN_variableSPOT.ttf`      | Accent letters, decorative elements       |
| Body        | DINish Bold                | `DINish-Bold.woff`                 | Body text, UI labels, navigation          |
| Body italic | DINish Bold Italic         | `DINish-BoldItalic.woff`           | Emphasis, captions, dates                 |

**Type scale:**

| Level | Size (rem) | Font           | Usage                     |
|-------|------------|----------------|---------------------------|
| xl    | 4–6 rem    | FLUTGRABEN var | Hero / page title         |
| h1    | 2.5 rem    | FLUTGRABEN var | Section title             |
| h2    | 1.75 rem   | FLUTGRABEN var | Subsection title          |
| h3    | 1.25 rem   | DINish Bold    | Card title, item heading  |
| body  | 1 rem      | DINish Bold    | Running text              |
| small | 0.875 rem  | DINish Bold    | Captions, metadata, dates |
| label | 0.75 rem   | DINish Bold    | Tags, nav items, UI labels|

### Grid

Derived from the window grid of the Flutgraben building (4×4, base unit 26×41 cm, 3 cm border).

| Property     | Value               |
|--------------|---------------------|
| Columns      | 4                   |
| Gutter ratio | 7.3% of total width |
| Aspect ratio | 26 : 41             |

The 4-column grid is maintained at all breakpoints — column widths and gutters shrink proportionally. Decorative elements (shapes, curves, GIFs) should align to column edges or be centered within cells.

**Asset sources:**
- `03_logo/` — geometric shapes (circles, crosses, polygons, squares, lines)
- `05_courbe/` — organic curves for non-structural decoration
- `06_gif_graffiti/` — animated GIFs, use sparingly as punctuation

## Coding Standards

### Comments
- **All comments must be written in English**, without exception
- Every function must have a comment explaining what it does
- Comment complex logic inline — explain *why*, not just *what*
- Use clear, concise language written for the next developer

```js
// Good example
// Scatters micro-dots around a central point to simulate spray paint bleed
function scatterDots(cx, cy, radius, count) { ... }
```

### HTML
- Use semantic tags (`<header>`, `<main>`, `<section>`, `<article>`, `<footer>`)
- Add comments to delimit major sections

```html
<!-- ===================== HEADER ===================== -->
<header>...</header>

<!-- ===================== CANVAS GENERATOR ===================== -->
<main>...</main>
```

### CSS
- Comment each major section
- Group related properties (layout, typography, colors)

```css
/* === Canvas container === */
.canvas-wrap { ... }

/* === Control panel === */
.controls { ... }
```

### JavaScript
- Comment every function (purpose, parameters, return value if relevant)
- Comment non-obvious logic, especially math related to rendering, grain, or geometry
- Use `const` by default, `let` only when reassignment is needed, never `var`

## Page types

The site has two distinct page structures. Never apply interior-page patterns to `index.html`, and never omit them from interior pages.

### `index.html` — Landing page

Unique layout, not derived from any shared template. Has its own structure and CSS. The header is present and shared with all other pages.

### Interior pages — all pages except `index.html`

All non-landing pages follow a shared template defined in `css/interior.css`. Every interior page includes:

| Element | Description |
|---------|-------------|
| Header | Shared with `index.html` |
| `bg-grid` | Decorative 4×4 ochre grid, `position: absolute`, `z-index: 0` |
| `gif-anchor` | Fixed circle bottom-right, mailto link |
| `subnav-bar` | Segmented button navigation, specific to each section |
| `details.row-item` | Expandable content rows — the core list primitive |

---

## CSS file structure

| File | Scope | Contains |
|------|-------|---------|
| `css/flutgraben.css` | All pages | Tokens (incl. `--cursor-pointer`), fonts, `html`/`body`/`main` layout, global reset, `.tags`, `.tag`, `.wip` |
| `css/header.css` | All pages | Topbar, nav, lang switcher |
| `css/interior.css` | Interior pages only | `bg-grid`, `gif-anchor`, `back-to-top`, `page-content`, `subnav`, `row-item`, lightbox, event card grid, event dialog |
| `css/index.css` | `index.html` only | Landing page grid and cell styles |

`css/style.css` no longer exists — its content was split into `flutgraben.css` (global rules) and `interior.css` (shared interior patterns) in May 2026.

`css/impressum.css` no longer exists — `impressum.html` was rebuilt using `interior.css` patterns only (May 2026).

`css/spree.css` no longer exists — merged into `interior.css` in May 2026. Event card grid and dialog styles now live in the shared interior stylesheet.

## Global UI Patterns

These elements appear on every interior page (all pages except `index.html`). CSS lives in `css/interior.css`; JS (where applicable) in `js/`.

| Pattern | Element | File(s) | Notes |
|---------|---------|---------|-------|
| Background grid | `<div class="bg-grid">` + 16× `<div class="bg-cell">` | `css/interior.css` | Decorative 4×4 ochre grid, `position: absolute`, `z-index: 0` |
| GIF anchor | see HTML below | `css/interior.css` | Fixed circle bottom-right. GIF src set via `<style>` inline per page. Contains a curved SVG label + full-circle mailto link. |
| Back to top | `<button class="back-to-top" aria-label="Back to top">↑</button>` | `css/interior.css`, `js/back-to-top.js` | Appears after 150px scroll, centered above gif-anchor. Script auto-detects scroll container (`.page-content` or `.impressum-outer`) |
| Residents search | see HTML below | `css/interior.css` | **Das Haus only — Residents tab.** Lives in the right slot of `.subnav-bar`. The wrapper `.residents-search-wrap` carries `.is-hidden` (visibility: hidden) when another tab is active, `.has-value` when the input is non-empty (shows clear button). |
| Lightbox | `<dialog id="lightbox">` — see HTML below | `css/interior.css`, inline `<script>` | **Pages with `.row-photo` images.** Click image to open fullscreen; navigate with arrows or ← → keys; close with ✕ button, backdrop click, or Échap. |
| Event cards + dialog | `<div class="events-grid">` + `<article class="event-card">` + `<dialog id="event-dialog">` — see section below | `css/interior.css`, inline `<script>` | **Spree + Das Haus (Residents).** 3-column grid, first card spans 2 cols (overridden in Das Haus — see below). Click any card to open dialog. |

When adding a new interior page: include bg-grid, gif-anchor, back-to-top in the HTML and add `<script src="js/back-to-top.js"></script>`. Add the lightbox dialog and JS only on pages that use `.row-photo`.

### Residents search — full pattern

```html
<!-- Right slot of .subnav-bar — Das Haus only -->
<div class="residents-search-wrap is-hidden">
  <input
    type="search"
    id="residents-search"
    class="residents-search"
    placeholder="Search"
    aria-label="Search residents"
    autocomplete="off"
  >
  <button class="residents-search-clear" aria-label="Clear search">✕</button>
</div>
```

JS (inline `<script>` at bottom of page):
- `is-hidden` toggled on `.residents-search-wrap` (not the input) — controls visibility
- `has-value` added to wrapper on each keystroke when input is non-empty — shows clear button
- Clear button resets input value, removes `has-value`, restores all hidden rows, and refocuses input
- On leaving Residents tab: input cleared, `has-value` removed, all rows shown

### GIF anchor — full pattern

```html
<div class="gif-anchor">
  <svg class="gif-anchor-label" viewBox="0 0 150 150" aria-hidden="true" focusable="false">
    <!-- Circular path along which the text travels — bottom arc, clockwise -->
    <path id="gif-circle-path" d="M 15,75 A 60,60 0 1,1 135,75" fill="none" />
    <text>
      <textPath href="#gif-circle-path" startOffset="50%" text-anchor="middle">
        contact@flutgraben.org
      </textPath>
    </text>
  </svg>
  <a href="mailto:contact@flutgraben.org" class="gif-anchor-link" aria-label="Write us — contact@flutgraben.org"></a>
</div>
```

- The SVG `viewBox` stays at `0 0 150 150` regardless of the rendered CSS size — it scales automatically
- The `<textPath>` text content is `contact@flutgraben.org` on all pages
- `.gif-anchor-link` is a transparent full-circle overlay — the entire bubble is clickable, not just the text
- The GIF image is set via inline `<style>` in each page (`.gif-anchor::before` and `:hover::before`)
- Static image uses `background-size: 105%` (slightly enlarged, slight edge crop) — hover GIF reverts to `contain` (defined in `css/interior.css`)
- Hover: text shifts from ochre → rust with slight letter-spacing expansion (defined in `css/interior.css`)

### Lightbox — full pattern

```html
<!-- Single instance per page, placed before </body> -->
<dialog id="lightbox">
  <button id="lightbox-prev" aria-label="Previous image">←</button>
  <img id="lightbox-img" src="" alt="">
  <button id="lightbox-next" aria-label="Next image">→</button>
  <button id="lightbox-close" aria-label="Close">✕</button>
</dialog>
```

JS (inline `<script>` at bottom of page):
- Click on `.row-photo img` → collects all sibling images from the same `.row-photo`, opens the dialog at the clicked index via `showModal()`
- `←` / `→` buttons and `ArrowLeft` / `ArrowRight` keys navigate within the set
- Prev/next arrows hide automatically at list boundaries (`visibility: hidden`)
- Backdrop click or `✕` button closes the dialog; Échap is handled natively by `<dialog>`
- `.row-photo img` carries `cursor: zoom-in` to signal the interaction
- **`<picture>` elements:** lightbox uses `img.currentSrc || img.src` — always loads the best-quality source the browser selected, not the fallback `src` attribute

**Rules:**
- One `<dialog id="lightbox">` per page — never duplicate
- Only add it on pages that use `.row-photo` images
- CSS in `css/interior.css`; JS is page-specific (inline), not a shared script

## Row item pattern

The expandable content row is the core UI primitive for all list-based interior pages. Use it for events, residents, spaces, or any future list.

```html
<details class="row-item">
  <summary>
    <span class="row-date">…</span>
    <span class="row-title">…</span>
    <div class="row-meta"><span class="tag">…</span></div>
  </summary>

  <!-- optional expanded content -->
  <div class="row-body">

    <!-- text column — max-width: 60ch, max-height: 400px, scrollable -->
    <div class="row-text">
      <p>…</p>
    </div>

    <!-- photo column — vertically scrollable, max-height: 400px, snap on each image -->
    <div class="row-photo">
      <picture>
        <source srcset="img-400w.webp 400w, img-800w.webp 800w" type="image/webp">
        <img src="img-800w.webp" alt="…" loading="lazy" decoding="async">
      </picture>
      <!-- additional <picture> elements go here — each snaps into view on scroll -->
    </div>

  </div>
</details>
```

### Rules

- All styles live in `css/interior.css`
- Never use `<h2>` inside `<summary>` — use `<span class="row-title">`
- `.row-body` is full-width by default (matches `<summary>`)
- `.row-body` becomes a 50/50 grid automatically when it contains `.row-photo` (via `:has(.row-photo)`)
- `.row-text` constrains text to `max-width: 60ch` and `max-height: 400px` with `overflow-y: auto` — text column scrolls when content is tall
- Links inside `.row-text` are underlined (`text-decoration: underline` via `.row-text a`)
- `.row-photo` is always a `<div>` container — never put `class="row-photo"` directly on `<picture>`
- `.row-photo` is a vertically scrollable column: `max-height: 400px`, `overflow-y: auto`, `scroll-snap-type: y proximity`
- Images render at their natural proportions (`width: 100%; height: auto`) — no forced aspect ratio, no cropping
- Multiple images stack vertically inside `.row-photo` — each `<picture>` snaps into view (`scroll-snap-align: start`)
- Prepare responsive images at 400w/800w/1200w/1920w variants; crop to landscape when the source is portrait to avoid excessive scroll height
- `.row-text` is always required inside `.row-body` — even when empty (use a placeholder comment)
- `.row-text` must be fully closed (`</div>`) before `.row-photo` opens — they are siblings inside `.row-body`, not nested
- Omit `.row-photo` if not needed — the layout degrades cleanly to single-column text
- **Never duplicate links** between `row-meta` and `row-body` — links belong in `row-meta` only (always visible), not repeated inside the expanded body
- The last `.row-item` in any list carries `margin-bottom: 33.33vh` — ensures the final row can scroll to a comfortable reading position

### `row-meta` and `row-date` — per-section conventions

The meaning of `row-date` and `row-meta` varies by section. Do not assume a single usage — follow the table below.

| Section | `row-date` | `row-meta` |
|---------|-----------|------------|
| Das Haus — History | Year / area / label | Tag (`.tag`) |
| Das Haus — Communs | Area in m² | Tag (floor: `.tag`) |
| Das Haus — Residents | **Replaced by `.event-card` grid** — no longer uses `row-item` | — |
| Das Haus — Accessibility | — | Tag (`.tag`) |

**Residents note:** the Residents section no longer uses `row-item`. It uses the `.event-card` grid pattern — see "Event card pattern" section above.

## Event card pattern — Spree + Das Haus (Residents)

Event cards replace `details.row-item` on the Spree page. Each card is an `<article>` with all event data in `data-*` attributes, consumed by the dialog JS at click time.

```html
<article class="event-card" tabindex="0" role="button"
  data-title="Event title"
  data-date="Day DD Mon · HHh"
  data-location="Venue · extra info"
  data-tag="Category"
  data-tag-class=""
  data-desc="Description shown in the dialog."
  data-imgs='["image/spree/archives/2023/slug_01_...-800w.webp"]'
>
  <div class="event-card__img">
    <!-- Real photo when available — injected as <img> covering the hatch -->
    <img src="image/spree/archives/2023/slug_01_...-800w.webp" alt="Event title" loading="lazy">
  </div>
  <div class="event-card__info">
    <div class="event-card__date">Day DD Mon · HHh</div>
    <h3 class="event-card__title">Event title</h3>
    <div class="event-card__meta">
      <span class="tag [tagClass]">Category</span>
      <span class="event-card__location">Venue</span>
    </div>
  </div>
</article>
```

- `data-tag-class` — one of: empty (outline only) · `sky` · `ochre` · `terra`
- `data-imgs` — JSON-stringified array of image paths (all sizes use `-800w.webp`). Omit entirely if no images. For static cards, set manually; for archive cards, injected by `renderArchiveYear`.
- When no image is available, `.event-card__img` shows a diagonal hatch background + category watermark
- Cards sit inside `.events-grid` (3-column grid, `css/spree.css`)
- First card in each `.events-grid` spans 2 columns (lead card) — no extra class needed
- `&` in data attribute values must be written as `&amp;`
- **`data-tag` content:** on Spree, holds the event category (e.g. "Concert"). On Das Haus Residents, holds a one-word practice keyword extracted from the description (e.g. "photography", "felt", "sound") — or `"undef"` when no clear keyword is available.
- **`data-location` as link:** the dialog renders `data-location` as a clickable `<a>` (JS creates the element dynamically). `mailto:` and `https://` prefixes are stripped for display; the full URL is used as `href`. CSS in `css/spree.css` under `.dialog-location a`.

### Das Haus Residents overrides

`das-haus.html` adds one page-scoped override in its inline `<style>`:

```css
/* No lead card — all residents cells equal width */
#residents .event-card:first-child { grid-column: span 1; }
```

Residents `data-date` holds the type label (`"artist"` / `"collective"` / `"initiative"`), shown in `.event-card__date`.

### Event dialog

One `<dialog id="event-dialog">` per page, placed before `</main>`. Opened by clicking any `.event-card`. Navigation stays within the current section's `.events-grid`.

```html
<dialog id="event-dialog" aria-modal="true" aria-labelledby="dialog-title-el">
  <div class="dialog-inner">
    <div class="dialog-img">
    </div>
    <div class="dialog-text">
      <button id="dialog-close" aria-label="Close">×</button>
      <div class="dialog-scrollable">
        <h2 class="dialog-title" id="dialog-title-el"></h2>
        <div class="dialog-date" id="dialog-date-el"></div>
        <div class="dialog-location" id="dialog-location-el"></div>
        <div class="dialog-tag-row"><span class="tag" id="dialog-tag-el"></span></div>
        <hr class="dialog-divider">
        <p class="dialog-desc" id="dialog-desc-el"></p>
      </div>
      <div class="dialog-nav">
        <button id="dialog-prev">← Prev</button>
        <button id="dialog-next">Next →</button>
      </div>
    </div>
  </div>
</dialog>
```

- Layout: image pane left 55% + text pane right 45% (scrollable middle, fixed nav bottom)
- `::backdrop` uses `--skytransparent`
- `←` / `→` keyboard arrows navigate between events within the open section
- Backdrop click or `×` button closes; Échap is handled natively by `<dialog>`
- CSS in `css/interior.css`; JS inline in `spree.html`
- **Multi-image carousel**: when `data-imgs` contains more than one path, ochre dot indicators appear at the bottom of the image pane. Clicking a dot jumps to that image; clicking the image itself cycles to the next. Dots: `border var(--ochre)` inactive, filled `var(--ochre)` active, `background: var(--bg)` always.

### Archive section — data & rendering

The archive section (`#archive`) is populated dynamically. Data lives in a `<script type="application/json">` block to avoid JS string-escaping issues with quotes and non-ASCII characters:

```html
<script type="application/json" id="archive-data">
[{"year":"2025","title":"…","date":"…","location":"…","tag":"News","tagClass":"","desc":"…","imgs":["image/spree/archives/2025/slug_01_…-800w.webp"]}]
</script>
```

JS reads it as: `const ARCHIVE_EVENTS = JSON.parse(document.getElementById('archive-data').textContent);`

**Data source:** `03_data_oldwebsite/archive_events_safe.json` — 36 events, years 2019–2025, generated from the scraped `flutgraben_events.json` with `ensure_ascii=True`. Fields: `year`, `title`, `date`, `location`, `tag`, `tagClass`, `desc`, `imgs[]`.

**Image paths:** `image/spree/archives/{year}/{slug}_NN_{...}-800w.webp`. Images organized by year subfolder. Each event's `imgs` array contains all available images in index order (`_01_`, `_02_`, …); `imgs[0]` is used for the card thumbnail.

**Archive button behavior:**
- Hover over Archive button → year dropdown appears (CSS only, no JS)
- Click a year → archive section activates, button label changes to the selected year
- Click Upstream / In Flutgraben / Downstream → archive button label resets to `"Archive ↓"`, active year dot cleared

**Subnav "In Flutgraben":** label updated dynamically to `"In Flutgraben in [month]"` via `new Date().toLocaleString('en-GB', { month: 'long' })` — auto-updates each month.

---

## Shared scripts

| Script | Scope | Purpose |
|--------|-------|---------|
| `js/logo.js` | All interior pages | Picks a random SVG from `image/svg/` and sets it as `src` on any `[data-random-svg] img`. Pool is defined as an array inside the IIFE — update when new SVGs are added to `image/svg/`. |
| `js/trail.js` | All interior pages | Mouse trail effect |
| `js/back-to-top.js` | All interior pages | Back-to-top button behaviour |

---

## General Rules

- Keep files focused — one responsibility per file when possible
- Prefer readability over cleverness
- Ask before making structural or architectural changes
- The visual output should always feel consistent with the Flutgraben aesthetic: atomic, grainy, organic-yet-geometric