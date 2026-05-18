# Flutgraben Website — Design Brief

## Project

New website for Flutgraben e.V., a Berlin-based art space and community.
Current site: https://flutgraben.org/ — to be replaced entirely.

## Audience

- Artists in residence at Flutgraben
- External artists and practitioners
- General public — primarily people coming to find out about the programming and the space

The main use case is: someone discovers Flutgraben and wants to understand what's happening there.

## Primary Objective

Present the space and what takes place in it.
**The programming is the main page** — this is the entry point and must be immediately accessible.

## Tone

Artistic, unconventional, experimental.
The site should feel alive and non-corporate — queer, warm, and culturally specific to the Berlin art scene.
Avoid: bureaucratic structure, over-organized layouts, anything that feels like a standard institution website.

## Languages

- Default: English
- Multilingual — language switcher via dropdown menu
- German and potentially French as additional languages

## Navigation Philosophy

The current site has too many tabs — this must be simplified.
Navigation should feel intuitive and light, not exhaustive.

Priority sections (in order of importance):
1. **Eddies** — programming / events (main page)
2. **Das Haus** — the building, the space
3. **About** — the organization, its people and mission

Secondary sections (present but not foregrounded):
- Spree (context: the river, upstream/downstream)
- Bazar

## Visual Direction

### Grid
Inspired by the window grids of the building (see `04_grille/`).
Base unit: 26 × 41 cm, 3 cm border. Always maintains the same ratio.
4×4 grid — translate to web columns with consistent gutters.

### Shapes & Decoration
Geometric shapes (circles, crosses, polygons, squares, lines) extracted from the building's visual language — see `03_logo/`.
Used as decorative and structural elements, not icons.
Curves and organic forms (`05_courbe/`) to counterbalance the grid — modern, queer dimension.

### Animation
GIFs inspired by graffiti found in the building (`06_gif_graffiti/`).
Use sparingly — as punctuation, not wallpaper.

### Logo
SVG logo using DINish font: `03_logo/Flutgraben_logo_dinish.svg`

### Typography
- **DINish** (web font, woff): body text, UI elements — `07_fonts/DINish-Bold.woff`, `DINish-BoldItalic.woff`
- **FLUTGRABEN variable** (custom font, ttf): display / headings — `07_fonts/FLUTGRABEN_variable.ttf`
- **FLUTGRABEN variable SPOT**: accent / decorative use — `07_fonts/FLUTGRABEN_variableSPOT.ttf`
- **FLUTGRABEN variable [RECT]**: alternate display variant — `07_fonts/FLUTGRABEN_variable[RECT].ttf`

### Color Palette

| Role        | Name       | Hex       |
|-------------|------------|-----------|
| Text        | Rust       | `#573835` |
| Warm mid    | Terracotta | `#9f6861` |
| Accent      | Ochre      | `#c17d4c` |
| Sky         | Dusty blue | `#7fb8d7` |
| Background  | Off-white  | `#e5e9ed` |

## What to Avoid

- Too many navigation tabs (current site problem)
- Rigid, corporate, or over-structured layouts
- Generic institution aesthetics
- Heavy, slow-loading pages
