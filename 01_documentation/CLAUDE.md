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

## Global UI Patterns

These elements appear on every interior page (all pages except `index.html`). They are defined in `css/style.css` and their JS (where applicable) lives in `js/`.

| Pattern | Element | File(s) | Notes |
|---------|---------|---------|-------|
| Background grid | `<div class="bg-grid">` + 16× `<div class="bg-cell">` | `css/style.css` | Decorative 4×4 ochre grid, `position: absolute`, `z-index: 0` |
| GIF anchor | `<div class="gif-anchor"></div>` | `css/style.css` | Decorative animated GIF, `position: fixed` bottom-right. GIF src set via `<style>` inline in each page |
| Back to top | `<button class="back-to-top" aria-label="Back to top">↑</button>` | `css/style.css`, `js/back-to-top.js` | Appears after 150px scroll, centered above gif-anchor. Script auto-detects scroll container (`.page-content` or `.impressum-outer`) |
| Residents search | `<input class="residents-search" type="search" placeholder="Search…" aria-label="Search residents">` | `css/interior.css` | **Das Haus only — Residents tab.** Lives in the right slot of `.subnav-bar`. Hidden via `.is-hidden` (visibility: hidden) when another tab is active. |

When adding a new interior page: include all three elements in the HTML and add `<script src="js/back-to-top.js"></script>`.

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

    <!-- text column — max-width: 60ch -->
    <div class="row-text">
      <p>…</p>
    </div>

    <!-- photo column — one or more <picture> elements stacked vertically -->
    <div class="row-photo">
      <picture>
        <source srcset="img-400w.webp 400w, img-800w.webp 800w" type="image/webp">
        <img src="img-800w.webp" alt="…" loading="lazy" decoding="async">
      </picture>
      <!-- additional <picture> elements go here -->
    </div>

  </div>
</details>
```

### Rules

- All styles live in `css/interior.css`
- Never use `<h2>` inside `<summary>` — use `<span class="row-title">`
- `.row-body` is full-width by default (matches `<summary>`)
- `.row-body` becomes a 50/50 grid automatically when it contains `.row-photo` (via `:has(.row-photo)`)
- `.row-text` constrains text to `max-width: 60ch` for readability
- `.row-photo` is always a `<div>` container — never put `class="row-photo"` directly on `<picture>`
- Multiple images: add multiple `<picture>` elements inside `.row-photo` — they stack vertically by default
- `.row-text` is always required inside `.row-body` — even when empty (use a placeholder comment)
- Omit `.row-photo` if not needed — the layout degrades cleanly to single-column text

## General Rules

- Keep files focused — one responsibility per file when possible
- Prefer readability over cleverness
- Ask before making structural or architectural changes
- The visual output should always feel consistent with the Flutgraben aesthetic: atomic, grainy, organic-yet-geometric