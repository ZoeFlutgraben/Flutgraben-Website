# Flutgraben Website — Design Tokens

## Colors

| Role        | Name       | Hex       | Usage                                      |
|-------------|------------|-----------|--------------------------------------------|
| Background  | Off-white  | `#e5e9ed` | Page background, large surfaces            |
| Text        | Rust       | `#573835` | Body text, headings, primary UI text       |
| Warm mid    | Terracotta | `#9f6861` | Secondary text, borders, subtle elements   |
| Accent      | Ochre      | `#c17d4c` | Highlights, links, hover states, CTAs      |
| Sky         | Dusty blue | `#7fb8d7` | Contrast accent, tags, secondary actions   |

## Typography

### Font Assignments

| Role        | Font                      | File                              | Usage                                  |
|-------------|---------------------------|-----------------------------------|----------------------------------------|
| Display     | FLUTGRABEN variable       | `FLUTGRABEN_variable.ttf`         | Hero titles, section headers, large text |
| Display alt | FLUTGRABEN variable [RECT]| `FLUTGRABEN_variable[RECT].ttf`   | Alternate display, pull quotes         |
| Decorative  | FLUTGRABEN variable SPOT  | `FLUTGRABEN_variableSPOT.ttf`     | Accent letters, decorative elements    |
| Body        | DINish Bold               | `DINish-Bold.woff`                | Body text, UI labels, navigation       |
| Body italic | DINish Bold Italic        | `DINish-BoldItalic.woff`          | Emphasis, captions, dates              |

### Type Scale

| Level  | Size (rem) | Font            | Usage                        |
|--------|------------|-----------------|------------------------------|
| xl     | 4–6 rem    | FLUTGRABEN var  | Hero / page title            |
| h1     | 2.5 rem    | FLUTGRABEN var  | Section title                |
| h2     | 1.75 rem   | FLUTGRABEN var  | Subsection title             |
| h3     | 1.25 rem   | DINish Bold     | Card title, item heading     |
| body   | 1 rem      | DINish Bold     | Running text                 |
| small  | 0.875 rem  | DINish Bold     | Captions, metadata, dates    |
| label  | 0.75 rem   | DINish Bold     | Tags, nav items, UI labels   |

## Grid

### Principle
The grid is derived from the window grid of the Flutgraben building.
It must remain visually coherent with the architecture of the space.

### Specification

| Property         | Value                  | Source                          |
|------------------|------------------------|---------------------------------|
| Columns          | 4                      | 4×4 window grid                 |
| Rows             | 4 (per section)        | 4×4 window grid                 |
| Gutter ratio     | 7.3% of total width    | 3 cm / 41 cm (window dimension) |
| Aspect ratio     | 26 : 41                | Window grid origin dimensions   |

### Responsive behavior
The 4-column grid is maintained at all breakpoints.
Column widths shrink proportionally — gutters scale with the same 7.3% ratio.
Layout adaptation (stacking, reordering) is left to Claude Design.

### Gutter sizes at common widths (approx.)

| Viewport  | Width   | Gutter (7.3%) |
|-----------|---------|---------------|
| Desktop   | 1440px  | ~105px        |
| Laptop    | 1280px  | ~93px         |
| Tablet    | 768px   | ~56px         |
| Mobile    | 390px   | ~28px         |
| Mobile sm | 360px   | ~26px         |

## Spacing & Decoration

Spacing scale and component-level padding are left to Claude Design.

Decorative elements (geometric shapes, curves, GIFs) should follow the grid —
aligned to column edges or centered within cells. See:
- `03_logo/` — geometric shapes (circles, crosses, polygons, squares, lines)
- `05_courbe/` — organic curves for non-structural decoration
- `06_gif_graffiti/` — animated GIFs, use sparingly as punctuation
