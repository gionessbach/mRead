import sys, glob, subprocess, os
from concurrent.futures import ThreadPoolExecutor
def lev(a, b):
    p = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        c = [i]
        for j, cb in enumerate(b, 1):
            c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (ca != cb)))
        p = c
    return p[-1]
def run(tessdir, png):
    r = subprocess.run(["tesseract", png, "-", "--tessdata-dir", tessdir, "-l", "deu", "--psm", "7"], capture_output=True, text=True)
    return r.stdout.strip()
tessdir, pattern = sys.argv[1], sys.argv[2]
show = len(sys.argv) > 3
files = sorted(glob.glob(pattern))
with ThreadPoolExecutor(2) as ex:
    outs = list(ex.map(lambda f: run(tessdir, f), files))
err = tot = 0; werr = wtot = 0
for f, o in zip(files, outs):
    gt = open(f[:-4] + ".gt.txt").read().strip()
    e = lev(o, gt); err += e; tot += len(gt)
    gw = gt.split(); ow = o.split(); werr += sum(1 for w in gw if w not in ow); wtot += len(gw)
    if show: print("%-12s %-36s | %s" % (os.path.basename(f)[:-4], gt, o))
print("CER %.1f%%  Wörter falsch %.1f%%  (%d Zeilen)" % (100 * err / tot, 100 * werr / wtot, len(files)))
