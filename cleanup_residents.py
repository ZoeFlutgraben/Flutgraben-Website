import re

path = r'C:\Users\Zoe\Documents\09_autre_projets\website\05-11\00_maquette\export-A\das-haus.html'

with open(path, encoding='utf-8') as f:
    html = f.read()

# Isolate the residents section to avoid touching other sections
start = html.index('id="residents"')
end   = html.index('id="communs"')
before  = html[:start]
section = html[start:end]
after   = html[end:]

# 1. Remove all .tag spans inside row-meta in residents section
section = re.sub(r'\s*<span class="tag[^"]*">[^<]*</span>', '', section)

# 2. Empty filled row-date values (only "Painting" currently)
section = re.sub(r'(<span class="row-date">)[^<]+(</span>)', r'\1\2', section)

# 3a. Remove <p> elements whose content is exclusively <a> tags + separators (· / spaces)
def is_links_only_p(m):
    inner = m.group(1)
    # Strip all <a>...</a> tags and separators
    stripped = re.sub(r'<a\b[^>]*>.*?</a>', '', inner, flags=re.DOTALL)
    stripped = re.sub(r'[\s·\-/]+', '', stripped)
    return '' if stripped == '' else m.group(0)

section = re.sub(r'<p>(.*?)</p>', is_links_only_p, section, flags=re.DOTALL)

# 3b. Remove standalone <span><a ...>...</a></span> (link-only spans, not inside <p>)
#     These appear directly inside .row-text, not wrapped in <p>
section = re.sub(r'\s*<span><a [^>]+>[^<]*</a></span>', '', section)

html_out = before + section + after

with open(path, 'w', encoding='utf-8') as f:
    f.write(html_out)

print("Done.")
