"""inject2.py — bio + meta links for Inga Zimprich → Wolfgang Schlegel"""
import re

HTML_PATH = r'C:\Users\Zoe\Documents\09_autre_projets\website\05-11\00_maquette\export-A\das-haus.html'

def para(text):
    text = text.replace('\r\n', '\n').strip()
    chunks = re.split(r'\n{2,}', text)
    parts = []
    for chunk in chunks:
        chunk = chunk.strip()
        if chunk:
            chunk = chunk.replace('\n', '<br>\n            ')
            parts.append(f'<p>{chunk}</p>')
    return '\n            '.join(parts)

def su(url, label=None):
    if not url.startswith('http'): url = 'https://' + url
    if label is None: label = re.sub(r'^https?://(www\.)?', '', url).rstrip('/')
    return f'<span><a href="{url}" target="_blank" rel="noopener">{label} ↗</a></span>'

def sm(email):
    return f'<span><a href="mailto:{email}">{email} ↗</a></span>'

def row_body(bio_html, links_html=''):
    body = f'        <div class="row-body">\n          <div class="row-text">\n            {bio_html}'
    if links_html: body += f'\n            {links_html}'
    return body + '\n          </div>\n        </div>'

# ── Bio content ───────────────────────────────────────────────────────────────

BIOS = {

'Jasna L. Vinovrški / Public in Private': row_body(
    para('Jasna L. Vinovrški works as a performer, choreographer and teacher. She grew up in Zagreb but lives and works abroad since the disintegration of Yugoslavia. At the beginning of the 90s she studied in Essen, at the Folkwang Hochschule. After her graduation, for 12 years, she has been working as a professional dancer and performer for various European dance companies.\n\nIn 2006 she received the scholarship from Kunststiftung Baden-Württemberg and DanceWeb scholarship from Goethe Institute. After moving to Berlin in 2008, together with her partner Clément Layes, she founded the company Public in Private.\n\nIn 2012 Jasna gains her MA degree in choreography at the HZT University in Berlin. In 2014 she was invited by the Croatian Institute for Contemporary Dance to participate in the two-year EU-Canada project "Migrant Bodies", resulting in her solo work "Staying Alive", on tour in Europe, Canada and New York since 2016.\n\nPublic in Private was founded in 2008 in Berlin by Clément Layes and Jasna L. Vinovrški. Its goal is to broaden the borders of choreographic language. Their main working space is Studio Public in Private at Atelierhouse Flutgraben.'),
    su('www.jasnavinovrski.com') + su('publicinprivate.com')
),

'Jo Zahn': row_body(
    para('Jo Zahn is a filmmaker, artist and musician. In his works he is developing perspectives on social, political and media issues. They are often created as collaborations, in dialogue processes and improvisation.')
),

'Julia Lipinsky': row_body(
    para('Julia Lipinsky plays with a variety of materials, textures and fabrics and creates colourful, cheerful worlds with them. Originally studying fashion design and fine art sculpture, she calls herself a textile sculptress.'),
    su('www.julialipinsky.de') + sm('contact@julialipinsky.de')
),

'Low Text': row_body(
    para('After the Eclipse is an open literary event format that provides a platform for writers, poets and artists working with text to share their work with audiences in an engaged, generous atmosphere. Originally initiated by Ebba Fransén Waldhör, Imri Kahn and Sarah M Harrison.\n\nThe cycle LOW TEXT aims to explore text production as a social practice and texts that become invisible in their ubiquity — emails, applications, manuals, automated texts. By taking a step back from individual authorship, this cycle takes a step towards it: how can we engage critically with such normative texts? Curated by Maru Mushtrieva, with co-curators Alexandra Zakharenko, Elena Vogman, Hrefna Hörn Leifsdóttir, Liudmila Saveliyeva.')
),

'Marei Löllmann': row_body(
    para('Marei Löllmann works as a solo artist and as part of different interdisciplinary collectives.'),
    su('www.mareirei.de')
),

'margot schmitt': row_body(
    para('margot schmitt, born in 1954, Germany. Freelance artist, art teacher, toolmaker. Studied political science, German, art history, art education and fine arts. Lives and works in Berlin.\n\nThe exploration of psychological and social identity – one\'s own and that perceived as »alien« – and its inscription in bodies and things was and is the »substance« of her artistic work. Material, form and presentation decisions are mostly made during and out of the »field research« on the chosen topic. After a phase of »Landscapes, Flowers and Blossoms – no politics«, she has returned to political issues in recent years.'),
    su('www.margotschmitt.com')
),

'Maria Turik': row_body(
    para('Born in East Siberia in 1982. First University degree in Linguistics. Studied Fine Arts at Burg Giebichenstein Academy Halle, and at Weißensee Academy of Art Berlin.\n\nIn current work, combining sculptural elements with movement and sound, creating performances and installations for the stage and open-air spaces. One of the important topics of her work is the birth of non-verbal sign systems and other ways to perceive and understand one another.'),
    su('www.mariaturik.online')
),

'Markus Draper': row_body(
    '',
    su('markusdraper.de')
),

'Marta Lodola': row_body(
    para('Marta Lodola is a multidisciplinary artist, graduate in painting from the Academy of Fine Arts Brera in Milan. Her artistic work turns around the relationship between body and territory and the practice of resistance and liberation. Her work was displayed by the city of Milan, the art academy of Weissensee, GAP Gathering Around Performance and CIPAF. Her work has been funded by the European Cultural Foundation.\n\nOngoing project: Actions Against Borders #1 Breaking Point (2017–ongoing)'),
    su('martalodola.wordpress.com') + su('1breaking-point.org')
),

'Mikala Hyldig Dal': row_body(
    para('Mikala Hyldig Dal (1979, Denmark) is an artist and curator working in the field of new media and performance. Her work embeds critical theory in immersive digital environments and intersects artistic practice with political activism. A graduate of the Berlin University of Arts, her work has been presented at Martin Gropius Bau, House of World Cultures, Townhouse Gallery Cairo, Museum of Contemporary Art Los Angeles, Nikolaj Kunsthal Copenhagen, Flux Factory New York and Azad Gallery Tehran.\n\nShe is the editor of the anthology Images of Transition on art and activism in the Arab Uprisings of 2011, initiator of Open/Occupy Flutgraben, and a founding member of the feminist artist collective MATERNAL FANTASIES.'),
    su('www.mikala-dal.art') + su('www.maternalfantasies.net')
),

'Nicole Schuck': row_body(
    para('Born in Herford / Westphalia, lives in Berlin. She studied fine arts at the Braunschweig University of Fine Arts, graduating as a master student with Professor John Armleder in 2004. Since then she has worked as a freelance artist, focusing her projects on wildlife, natural and urban habitats, ecology and nature conservation.\n\nIn 2020, her book "Geschätzte Tiere / Valued Animals" was published by Hatje Cantz Verlag. Her works are represented in collections including: Collection of contemporary art of the Federal Republic of Germany; Berlinische Galerie; LWL-Museum für Kunst und Kultur Münster.'),
    su('www.nicoleschuck.de')
),

'Nora Al-Badri': row_body(
    para('Nora Al-Badri is a multi-disciplinary and conceptual media artist with a German-Iraqi background. Her works are research-based as well as paradisciplinary and as much post-colonial as post-digital. She lives and works in Berlin.\n\nShe graduated in political sciences at Johann Wolfgang Goethe University Frankfurt/Main and was the first artist-in-residence at the Swiss Federal Institute for Technology (EPFL) and its Laboratory for Experimental Museology (eM+) in 2020. Her practice focuses on the politics and the emancipatory potential of new technologies such as machine intelligence or data sculpting, non-human agency and transcendence.'),
    su('www.nora-al-badri.de')
),

'Open Occupy': row_body(
    para('Since artists started squatting in the abandoned GDR factory at Flutgraben in the early 90s, they opened their studios regularly to the public. FLUTGRABEN, since 1998 a non-profit organisation and Berlin\'s largest self-organized artists\' studio building, continues to engage the public in an annual Open House.\n\nSince 2018 Open House Flutgraben has increasingly turned its attention to the financialization of urban space and examines how structures of exploitation can be countered through the practice of open, solidarity-based networks, and transdisciplinary collaboration. The initiative Open/Occupy is a direct response to an ongoing process of gentrification in Berlin.\n\nOpen/Occupy believes that the city needs free and open spaces because they generate critical knowledge and create community; foster alternative visions of the future through experiential forms of discourse; facilitate open-mindedness towards the unknown and the potential of becoming.'),
    su('https://openoccupy.com')
),

'raumlaborberlin': row_body(
    para('raumlabor is a collective of nine members with a shared background in architecture. As architects, artists, performers, inventors and curators, they have tapped into different spheres of action. The group developed in 1999 from a common interest in an expanded understanding of architecture, which has since been established as Urban Practice. raumlabor\'s working method is situational and action-oriented, with a focus on the collaborative production of space as an open and unbiased process.'),
    su('raumlabor.net')
),

'Roland Boden': row_body(
    para('Die Bilder Roland Bodens basieren auf architektonischen 3D-Modellen, die als perspektivische Rohskizzen dienen. Diese zwischen Modell, Simulation und Realität angesiedelten Konstrukte verharren in einer ambivalenten Welt zwischen Vergangenheit und Zukunft: Retro/Future.\n\nParallel hierzu entstehen umfangreiche textbasierte Arbeiten im historischen, wissenschaftlichen und militärhistorischen Kontext, die sich mit dem Begriff der Realität auseinandersetzen und als fiktionale Recherchen bezeichnet werden.\n\nRoland Boden, geboren 1962 in Dresden, lebt in Berlin. Ausstellungen u.a. Manifesta 3 Ljubljana, Busan Biennale, New Museum New York, ICA London, Künstlerhaus Bethanien Berlin, Westf. Landesmuseum Münster. Preise u.a. Deutsche Akademie Villa Massimo Rom 2003, Falkenrot-Preis Berlin 2020.'),
    su('www.rolandboden.de') + su('www.kronos-projekt.de')
),

'Ronald de Bloeme': row_body(
    para('Ronald de Bloeme, born 1971 in Leeuwarden (NL), studied painting & drawing at the Willem de Kooning Academy in Rotterdam (1992–1996). In his paintings and drawings, he examines several communication systems such as cutting patterns, subway plans or election results.\n\nIn 2007 he was awarded the Vattenfall Contemporary Art Prize, followed by solo exhibitions at the Berlinischen Galerie, Berlin and the Stedelijk Museum, Schiedam. His works are represented in the collections of the Berlinische Galerie, Staatliche Kunstsammlungen Dresden, Stedelijk Museum Schiedam, Museum Voorlinden and the SAFN Collection Reykjavik.'),
    su('www.ronalddebloeme.com')
),

'Sheree Domingo': row_body(
    para('Sheree Domingo, born 1989, is a freelance illustrator and comic book author. She was a finalist for the Berthold Leibinger Stiftung Comic Book Prize in 2016 with her project "Wie im Paradies," which evolved into her debut "Ferngespräch" (2019, Edition Moderne), and was awarded the Grimmelshausen Fellowship Prize in 2021. The half-autobiographical story combines the themes of labour migration, care work, and loneliness in old age.\n\nHer feminist attitude runs through all her work. As a comic artist, she works with the Museum für Naturkunde Berlin, the University of Tübingen and others, making the ethical questions raised by genome editing accessible to a broader public.')
),

'Stephan Kurr': row_body(
    para('Stephan Kurr studied between 1983 and 1991 at the Kunsthochschule in Kassel and the Academy of Fine Arts in Nuremberg. In 1992–93 he travelled to Yemen on a DAAD scholarship and studied architectural ornament. He was co-initiator of the Kreuzberg shop window gallery SOX36 and held residencies in Helsinki, Cali (Colombia) and Montréal.\n\nStephan Kurr worked at the art education program of documenta 11, taught at the Nuremberg Art Academy, and was visiting professor at Concordia University Montréal. Works of art are often created in exchange with colleagues or in collaboration with other people — with bar visitors in Helsinki, a band in Cali, a blind man in Hanoi, with young Roma, with employees of an energy company. Language is often his means of expression, in films, in texts but mainly as a visual language.'),
    su('www.kurr.org') + su('www.bezeichnung.org')
),

'The Watch': row_body(
    para('"It is difficult to be in this tower. There is nothing other than you. It is difficult even to enter, and hard to work on anything. There is no Internet connection, no one visits and, at the end of the day, no one is asking anything from you." (Clément Layes, The Watch, 2017)\n\nA trace from the border apparatus during the division of the city, the former GDR watchtower on Schlesischer Busch has had a long tradition of cultural and artistic production ever since Reunification. Under the care of FLUTGRABEN e.V. since 2004, the building has hosted several exhibitions, talks, screenings, and residencies.\n\nThe Watch invites producers to take time to watch, observe, contemplate and inhabit the tower, to adopt the building\'s passivity. Every year a group of artists decides on the thematic content, formats and programming, either through direct invitations or open calls.\n\nThe Watch currently consists of Jean-Ulrick Désert, Franziska König-Paratore, Dominique Hurth, Irina Novarese and Jo Zahn.'),
    su('thewatch-berlin.org') + sm('residency.wachturm@gmx.de')
),

'Wolfgang Schlegel': row_body(
    para('Lives in Brandenburg an der Havel and works in Berlin since 1999. Completed studies at the Academy of Visual Arts Düsseldorf as Master of Arts at the class of Fritz Schwegler. His artistic career is distinguished by residencies at New York\'s P.S.1 and London\'s Delfina Studio Trust, plus grants of Kunstfonds Bonn and Pollock Krasner Foundation USA.\n\nHis works have been exhibited in Germany, USA, Great Britain, Italy and France at places like Portikus Frankfurt, Kunsthalle Düsseldorf, Museum Kurhaus Kleve, Castello di Rivara Turin, and at galleries Jablonka Köln, Brose-Eiermann Berlin/Dresden, Unit London, Laura Mars Berlin.'),
    su('www.wolfgangschlegel.eu')
),

}

# ── Meta links ────────────────────────────────────────────────────────────────

META_LINKS = [
    ('Jasna L. Vinovrški / Public in Private', [su('www.jasnavinovrski.com'), su('publicinprivate.com')]),
    ('Julia Lipinsky',   [su('www.julialipinsky.de'), sm('contact@julialipinsky.de')]),
    ('Marei Löllmann',   [su('www.mareirei.de')]),
    ('margot schmitt',   [su('www.margotschmitt.com')]),
    ('Maria Turik',      [su('www.mariaturik.online')]),
    ('Markus Draper',    [su('markusdraper.de')]),
    ('Marta Lodola',     [su('martalodola.wordpress.com')]),
    ('Mikala Hyldig Dal',[su('www.mikala-dal.art'), su('www.maternalfantasies.net')]),
    ('Nicole Schuck',    [su('www.nicoleschuck.de')]),
    ('Nora Al-Badri',    [su('www.nora-al-badri.de')]),
    ('Open Occupy',      [su('https://openoccupy.com')]),
    ('raumlaborberlin',  [su('raumlabor.net')]),
    ('Roland Boden',     [su('www.rolandboden.de'), su('www.kronos-projekt.de')]),
    ('Ronald de Bloeme', [su('www.ronalddebloeme.com')]),
    ('Stephan Kurr',     [su('www.kurr.org'), su('www.bezeichnung.org')]),
    ('The Watch',        [su('thewatch-berlin.org'), sm('residency.wachturm@gmx.de')]),
    ('Wolfgang Schlegel',[su('www.wolfgangschlegel.eu')]),
]

# ── Inject ────────────────────────────────────────────────────────────────────

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# Bio injection
for title, body_html in BIOS.items():
    pattern = (r'(<span class="row-title">' + re.escape(title) + r'</span>'
               r'.*?</summary>)\s*\n(\s*</details>)')
    new_html, count = re.subn(pattern, r'\1\n' + body_html + r'\n\2', html, flags=re.DOTALL)
    if count == 0:
        print(f'BIO WARNING: {title}')
    else:
        html = new_html
        print(f'BIO OK: {title}')

# Meta links injection
for title, spans in META_LINKS:
    spans_html = ''.join(spans)
    pattern = (r'(<span class="row-title">' + re.escape(title) + r'</span>\s*'
               r'<div class="row-meta">(?:.*?))(</div>)')
    new_html, count = re.subn(pattern, r'\1' + spans_html + r'\2', html, flags=re.DOTALL)
    if count == 0:
        print(f'META WARNING: {title}')
    else:
        html = new_html
        print(f'META OK: {title}')

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print('\nDone.')
