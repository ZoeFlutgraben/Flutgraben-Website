# Image Rights — Residents (Das Haus)

Artist images in the Residents section are the property of their respective authors. Follow these conventions every time images are added.

## robots.txt

The `/image/residents/` folder is blocked from indexing. If new subfolders are created for artist images, add a matching `Disallow` rule in `robots.txt`:

```
Disallow: /image/residents/
```

## Copyright caption (HTML)

Every artist image must include a visible copyright line immediately below it:

```html
<figure>
  <img src="/image/residents/artist-name.jpg" alt="Description">
  <figcaption>© [Artist Name] — all rights reserved</figcaption>
</figure>
```

- Use the artist's full name as they provide it
- Keep the caption consistent: `© [Name] — all rights reserved`
- If the artist specifies a different credit format, use their version exactly

## Image folder

Store all resident images in: `/image/residents/`

Name files with the artist's name in lowercase, hyphenated: `firstname-lastname.jpg`