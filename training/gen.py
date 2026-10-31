"""Erzeugt Trainings-/Testzeilen: deutsche Texte in vielen Schriften, fotoähnlich verfremdet.
Aufruf: python3 gen.py <ausgabeordner> <zeilen_pro_font> <fontliste.txt> [seed]"""
import sys, os, random, math, io, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from wordfreq import top_n_list

out, per_font, fontlist = sys.argv[1], int(sys.argv[2]), sys.argv[3]
seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
random.seed(seed)
os.makedirs(out, exist_ok=True)
fonts = [l.strip() for l in open(fontlist) if l.strip()]

saetze = [l.strip() for l in open(os.path.join(os.path.dirname(__file__), "saetze.txt")) if l.strip()]
words = [w for w in top_n_list("de", 25000) if w.isalpha() and len(w) > 1]
NAMES = ["Lena", "Tom", "Mia", "Ben", "Emma", "Paul", "Anna", "Leo", "Ida", "Max", "Oskar", "Frieda", "Arianna",
         "Colleen", "Dario", "Erik", "Bernd", "Alex", "Carmen", "Olli", "Oscar", "Mister Morrison", "Rotkäppchen"]

def chunk(s):
    ws = s.split()
    out, i = [], 0
    while i < len(ws):
        n = random.randint(2, 7)
        out.append(" ".join(ws[i:i + n])); i += n
    return random.choice(out)

def cap(w):
    return w[0].upper() + w[1:]

def random_line():
    r = random.random()
    if r < 0.38:
        t = random.choice(saetze)
        if len(t) > 38 and random.random() < 0.7: t = chunk(t)
    elif r < 0.72:
        n = random.randint(2, 7)
        ws = [random.choice(words[:8000] if random.random() < 0.7 else words) for _ in range(n)]
        ws = [cap(w) if random.random() < 0.35 else w for w in ws]
        if random.random() < 0.2: ws.insert(random.randrange(len(ws) + 1), random.choice(NAMES))
        ws[0] = cap(ws[0])
        t = " ".join(ws)
        p = random.random()
        if p < 0.45: t += "."
        elif p < 0.55: t += "!"
        elif p < 0.65: t += "?"
        elif p < 0.75: t = t.replace(" ", ", ", 1)
        if random.random() < 0.08: t = "„" + t + "“"
    elif r < 0.9:
        t = random.choice(saetze)
        if len(t) > 30: t = chunk(t)
        t = t.upper()
    else:
        t = random.choice([
            "Seite %d" % random.randint(1, 200), "Kapitel %d" % random.randint(1, 30),
            "%d. %s" % (random.randint(1, 12), cap(random.choice(words[:3000]))),
            "%d Äpfel und %d Birnen" % (random.randint(2, 20), random.randint(2, 20)),
            "Um %d Uhr geht es los!" % random.randint(1, 12), "%d + %d = %d" % (2, 3, 5),
            "%s, %s und %s" % tuple(random.sample(NAMES, 3)),
        ])
    return t.replace("ẞ", "SS")

def render(text, fontfile):
    size = random.randint(30, 60)
    ft = ImageFont.truetype(fontfile, size)
    l, t, r, b = ft.getbbox(text)
    w, h = r - l, b - t
    pad = (random.randint(6, 24), random.randint(6, 18))
    W, H = w + pad[0] * 2, h + pad[1] * 2
    bg = random.choice([(255, 255, 255), (250, 246, 236), (243, 238, 224), (235, 240, 248), (238, 246, 233),
                        (252, 240, 200), (220, 232, 245), (248, 228, 230), (230, 230, 230)])
    bg = tuple(max(0, min(255, c + random.randint(-12, 8))) for c in bg)
    fg = random.choice([(20, 20, 20), (40, 35, 30), (30, 40, 90), (110, 30, 30), (60, 60, 60), (25, 70, 40), (90, 60, 120)])
    if random.random() < 0.15:  # schwacher Kontrast
        fg = tuple(int(c + (bc - c) * random.uniform(0.35, 0.55)) for c, bc in zip(fg, bg))
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)
    d.text((pad[0] - l, pad[1] - t), text, font=ft, fill=fg)
    # leicht schief / gedreht
    if random.random() < 0.6:
        im = im.rotate(random.uniform(-1.6, 1.6), resample=Image.BICUBIC, expand=True, fillcolor=bg)
    if random.random() < 0.3:
        sh = random.uniform(-0.12, 0.12)
        im = im.transform(im.size, Image.AFFINE, (1, sh, -sh * im.size[1] / 2, 0, 1, 0), resample=Image.BICUBIC, fillcolor=bg)
    # Licht ungleichmäßig
    if random.random() < 0.35:
        g = Image.linear_gradient("L").rotate(random.choice([0, 90, 180, 270])).resize(im.size)
        dark = Image.new("RGB", im.size, tuple(int(c * random.uniform(0.55, 0.8)) for c in bg))
        im = Image.composite(im, dark, g.point(lambda v: 150 + v * 105 // 255))
    # Unschärfe, Auflösung, Rauschen, JPEG
    if random.random() < 0.6:
        im = im.filter(ImageFilter.GaussianBlur(random.uniform(0.3, 1.3)))
    if random.random() < 0.4:
        f = random.uniform(0.45, 0.8)
        small = im.resize((max(8, int(im.width * f)), max(8, int(im.height * f))), Image.BILINEAR)
        im = small.resize(im.size, Image.BILINEAR)
    g = im.convert("L")
    if random.random() < 0.5:
        px = g.load()
        for _ in range(int(g.width * g.height * random.uniform(0.01, 0.06))):
            x, y = random.randrange(g.width), random.randrange(g.height)
            px[x, y] = max(0, min(255, px[x, y] + random.randint(-35, 35)))
    if random.random() < 0.5:
        g = ImageEnhance.Contrast(g).enhance(random.uniform(0.6, 1.4))
    if random.random() < 0.5:
        buf = io.BytesIO(); g.save(buf, "JPEG", quality=random.randint(35, 85)); buf.seek(0); g = Image.open(buf).convert("L")
    # Zeilenhöhe vereinheitlichen (Tesseract skaliert ohnehin)
    target = random.randint(40, 64)
    g = g.resize((max(16, int(g.width * target / g.height)), target), Image.BICUBIC)
    return g

meta = []
n = 0
for fname in fonts:
    path = os.path.join(os.path.dirname(__file__), "fonts", fname + ".woff")
    if not os.path.exists(path):
        path = fname  # Systemschrift (voller Pfad)
    for i in range(per_font):
        text = random_line()
        try:
            img = render(text, path)
        except Exception as e:
            continue
        base = "%s/%s_%04d" % (out, os.path.basename(fname).replace(".woff", "").replace(".ttf", ""), i)
        img.save(base + ".png")
        open(base + ".gt.txt", "w").write(text + "\n")
        n += 1
print("zeilen:", n)
