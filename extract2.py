import gzip, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

gz = r'C:\Users\Zoe\Documents\09_autre_projets\website\05-11\00_maquette\export-A\03_data_oldwebsite\flutgraben.org-20260519T141806Z-3-001\flutgraben.org\content\updraft\backup_2026-02-15-1320_Flutgraben_Berlin_ac7418709ae3-db.gz'
with gzip.open(gz, 'rt', encoding='utf-8', errors='replace') as f:
    db = f.read()

def find_pid(name):
    m = re.search(r"\(\d+,(\d+),'(?:last_name|first_name)','[^']*" + re.escape(name) + r"[^']*'\)", db, re.IGNORECASE)
    return m.group(1) if m else None

def get_field(pid, field):
    m = re.search(r"\(\d+," + pid + r",'" + re.escape(field) + r"','((?:[^'\\]|\\.)*)'\)", db, re.DOTALL)
    return m.group(1).replace("\\'", "'") if m else ''

def clean(text):
    en = re.search(r'\[:en\](.*?)(?:\[:de\]|\[:\])', text, re.DOTALL)
    text = en.group(1) if en else re.search(r'\[:de\](.*?)(?:\[:\]|$)', text, re.DOTALL)
    if hasattr(text, 'group'): text = text.group(1)
    elif text is None: return ''
    text = re.sub(r'<[^>]+>', ' ', str(text))
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'\r\n', '\n', text)
    text = re.sub(r' {2,}', ' ', text)
    return re.sub(r'\n{3,}', '\n\n', text).strip()

residents = [
    ('Inga', 'Zimprich'),
    ('Janine', 'Eisenächer'),
    ('Jasna', 'Vinovrški'),
    ('Jo', 'Zahn'),
    ('Jugoslav', 'Mitevski'),
    ('Julia', 'Lipinsky'),
    ('Katharina', 'Schoeller'),
    ('Katja', 'Brinkmann'),
    ('Lap', 'Yip'),
    ('Low', 'Text'),
    ('Lydia', 'Hamann'),
    ('Manuel', 'Klauser'),
    ('Marei', 'Löllmann'),
    ('margot', 'schmitt'),
    ('Maria', 'Turik'),
    ('Markus', 'Draper'),
    ('Marta', 'Lodola'),
    ('Matthias', 'Krause Hamrin'),
    ('Mikala', 'Hyldig Dal'),
    ('Natacha', 'Le Duff'),
    ('Nicole', 'Schuck'),
    ('Nino', 'Bulling'),
    ('Nora', 'Al-Badri'),
    ('Olaf', 'Holzapfel'),
    ('Open', 'Occupy'),
    ('Pascal', 'Stodieck'),
    ('QUASI', 'OBJECTS'),
    ('raumlabor', 'raumlaborberlin'),
    ('RILABEN', 'RILABEN'),
    ('Roland', 'Boden'),
    ('Ronald', 'de Bloeme'),
    ('Sheree', 'Domingo'),
    ('Sönke', 'Hallmann'),
    ('Sophia', 'Elstermann'),
    ('Sphen', 'Heinrich'),
    ('Stefan', 'Bernhard'),
    ('Stephan', 'Kurr'),
    ('The', 'Watch'),
    ('Ute', 'Ringel'),
    ('Wolfgang', 'Schlegel'),
]

for first, last in residents:
    pid = find_pid(last) or find_pid(first)
    if not pid:
        print(f'=== {first} {last} ===\nNOT FOUND\n')
        continue
    bio = clean(get_field(pid, 'bio'))
    website = get_field(pid, 'website').strip()
    email = get_field(pid, 'email').strip()
    discipline = get_field(pid, 'discipline').strip()
    print(f'=== {first} {last} (id:{pid}) ===')
    if bio: print(f'BIO:\n{bio}')
    if website: print(f'WEBSITE: {website}')
    if email: print(f'EMAIL: {email}')
    if discipline: print(f'DISCIPLINE: {discipline}')
    print()
