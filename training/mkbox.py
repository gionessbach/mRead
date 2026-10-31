import sys, unicodedata
from PIL import Image
for png in sys.argv[1:]:
    base = png[:-4]
    text = open(base + ".gt.txt").read().strip()
    w, h = Image.open(png).size
    lines = ["WordStr 0 0 %d %d 0 #%s" % (w, h, text)]
    lines.append("\t 0 0 %d %d 0" % (w, h))
    open(base + ".box", "w").write("\n".join(lines) + "\n")
