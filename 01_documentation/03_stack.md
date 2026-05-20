# Technical Stack — Recommendations

## Context

The current maquette is built in static HTML/CSS/JS. Before moving to production, the project needs a stack that allows:
- Non-technical maintainers to update content (events, news, residents, members)
- Preserving the custom design system entirely
- Free and open-source tooling
- Minimal ongoing maintenance

---

## Recommended Stack

### Astro — Static Site Generator

[astro.build](https://astro.build) — open-source, free

Astro generates static HTML/CSS from components. The entire current design system (tokens, CSS files, grid, header) transfers directly — Astro outputs the same HTML the maquette already produces.

**Key benefit:** the sidebar/header lives in a single `Base.astro` layout component instead of being copy-pasted into every HTML file. Each page passes its active state as a parameter.

### Decap CMS — Content Interface

[decapcms.org](https://decapcms.org) — open-source, free (formerly Netlify CMS)

A browser-based interface for editing content. The maintainer logs in, fills in forms (title, date, location, status), clicks Publish — no code required. Content is stored as Markdown files in Git.

**Key benefit:** content editors never touch code. Events, news, and other dynamic content are managed entirely through a visual interface.

### Content as Markdown

Each piece of dynamic content (event, news article, tenant) becomes a Markdown file with frontmatter:

```markdown
---
title: Stille Wasser — performance
date: Thu 22 May · 19h
status: current
tag: Performance
tagColor: terra
location: Hall 3
---
```

Astro reads these files and renders them into the page templates automatically.

---

## Hosting

**Recommended: Vercel or Netlify** — both free for this scale.

| | GitHub Pages | Netlify | Vercel |
|---|---|---|---|
| Cost | Free | Free | Free |
| Custom domain | Yes | Yes | Yes |
| HTTPS | Yes | Yes | Yes |
| Auto build on commit | Manual setup | Native | Native |
| Decap CMS integration | Possible | Native | Possible |

**You only pay for the domain name** — approximately 10–15€/year for a `.org`.

Workflow once deployed:
1. Designer/developer pushes code changes to Git → site rebuilds automatically
2. Content maintainer logs into `/admin` on the site → edits events/content → site rebuilds automatically

---

## Project Structure

```
flutgraben-site/
├── public/
│   ├── fonts/
│   ├── logos/
│   ├── gifs/
│   └── admin/           ← Decap CMS interface
│       └── config.yml
├── src/
│   ├── layouts/
│   │   └── Base.astro   ← shared header/sidebar (replaces copy-paste)
│   ├── pages/
│   │   ├── index.astro
│   │   ├── spree.astro
│   │   ├── impressum.astro
│   │   └── ...
│   ├── content/
│   │   └── events/      ← one .md file per event
│   └── styles/
│       ├── flutgraben.css
│       ├── header.css
│       ├── style.css
│       └── spree.css
└── astro.config.mjs
```

---

## What changes vs. the current maquette

| | Current maquette | Astro |
|---|---|---|
| CSS | Static files | Same static files |
| HTML structure | Copy-pasted per page | Single layout component |
| Event content | Hardcoded in HTML | Markdown files |
| Content updates | Edit HTML | Web interface (Decap) |
| Adding a page | Copy header manually | Create `.astro` file |
| Hosting | — | Vercel/Netlify, free |

The design does not change. Astro generates the exact same HTML/CSS output.

---

## Migration path from the current maquette

1. Initialize Astro project
2. Move `css/` and `public/` assets as-is
3. Extract `<header>` into `Base.astro`
4. Convert each `.html` page to `.astro` (mostly find/replace)
5. Move hardcoded events to Markdown files in `src/content/events/`
6. Configure Decap CMS for the `events` collection
7. Deploy to Vercel/Netlify, connect custom domain
