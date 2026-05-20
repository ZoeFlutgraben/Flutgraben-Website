"""restore_meta.py — Restore row-meta links that were wiped by cleanup_residents.py"""
import re

HTML_PATH = r'C:\Users\Zoe\Documents\09_autre_projets\website\05-11\00_maquette\export-A\das-haus.html'

def su(url, label=None):
    if not url.startswith('http'): url = 'https://' + url
    if label is None: label = re.sub(r'^https?://(www\.)?', '', url).rstrip('/')
    return f'<span><a href="{url}" target="_blank" rel="noopener">{label} ↗</a></span>'

def sm(email):
    return f'<span><a href="mailto:{email}">{email} ↗</a></span>'

# Complete list of row-meta links per resident
# (original HTML links + inject2.py META_LINKS combined)
META = [
    # ── Original HTML links ────────────────────────────────────────────────────
    ('acting from zero',                    sm('mari@nothingtalks.com')),
    ('Adrian Rovatkay',                     su('rovatkay.blogspot.com')),
    ('Alfonso Moral',                       su('alfonsomoral.net') + su('anti-books.net')),
    ('alpha nova &amp; galerie futura',     su('galeriefutura.de')),
    ('Andres Villarreal',                   su('andresvillarreal.net')),
    ('Barbara Ott',                         su('barbaraott.com') + sm('mail@barbaraott.com')),
    ('Benedikt Rugar',                      su('benediktrugar.de')),
    ('Clément Layes / Public in Private',   su('clementlayes.com') + su('publicinprivate.com')),
    ('Clémentine M. Songe',                 su('clementine-mensonge.com')),
    ('Cornelia Herfurtner',                 su('corneliaherfurtner.net')),
    ('Dagmar Binder',                       su('textillabor.de') + sm('dagmar@textillabor.de')),
    ('Daniel Franke',                       su('daniel-franke.com')),
    ('Darius Kolski',                       su('soundcloud.com/kolkyer', 'soundcloud/kolkyer')),
    ('Dirk Lebahn',                         su('oqbo.de')),
    ('Dominique Hurth',                     su('dominiquehurth.com')),
    ('Fehras Publishing Practices',         su('fehraspublishingpractices.org')),
    ('Frank Zucht',                         su('frankzucht.com') + sm('mail@frankzucht.com')),
    ('Hannah Dougherty',                    su('hannahdougherty.net')),
    ('Harald Birck',                        su('harald-birck.de')),
    # ── inject2.py META_LINKS ─────────────────────────────────────────────────
    ('Jasna L. Vinovrški / Public in Private', su('jasnavinovrski.com') + su('publicinprivate.com')),
    ('Julia Lipinsky',                      su('julialipinsky.de') + sm('contact@julialipinsky.de')),
    ('Marei Löllmann',                      su('mareirei.de')),
    ('margot schmitt',                      su('margotschmitt.com')),
    ('Maria Turik',                         su('mariaturik.online')),
    ('Markus Draper',                       su('markusdraper.de')),
    ('Marta Lodola',                        su('martalodola.wordpress.com') + su('1breaking-point.org')),
    ('Mikala Hyldig Dal',                   su('mikala-dal.art') + su('maternalfantasies.net')),
    ('Nicole Schuck',                       su('nicoleschuck.de')),
    ('Nora Al-Badri',                       su('nora-al-badri.de')),
    ('Open Occupy',                         su('openoccupy.com')),
    ('raumlaborberlin',                     su('raumlabor.net')),
    ('Roland Boden',                        su('rolandboden.de') + su('kronos-projekt.de')),
    ('Ronald de Bloeme',                    su('ronalddebloeme.com')),
    ('Stephan Kurr',                        su('kurr.org') + su('bezeichnung.org')),
    ('The Watch',                           su('thewatch-berlin.org') + sm('residency.wachturm@gmx.de')),
    ('Wolfgang Schlegel',                   su('wolfgangschlegel.eu')),
]

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

for title, links_html in META:
    # Match the empty (or whitespace-only) row-meta for this exact resident
    pattern = (r'(<span class="row-title">' + re.escape(title) + r'</span>\s*'
               r'<div class="row-meta">)\s*(</div>)')
    replacement = r'\g<1>' + links_html + r'\g<2>'
    new_html, count = re.subn(pattern, replacement, html, flags=re.DOTALL)
    if count == 0:
        print(f'SKIP (not empty or not found): {title}')
    else:
        html = new_html
        print(f'OK: {title}')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print('\nDone.')
