# Training des Kinderbuch-Modells

`tessdata/deu.traineddata.gz` ist das deutsche Tesseract-Modell (tessdata_best, Version 4), nachtrainiert auf
Kinderbuch-, Comic-, Schreibschrift-, Handschrift- und Grundschul-Schriften.

## Vorgehen

1. **Schriften:** 63 freie Schriften von Google Fonts (über die npm-Pakete `@fontsource/*`), z. B. Patrick Hand, Caveat,
   Schoolbell, Comic Neue, Indie Flower, Kalam, Permanent Marker, Amatic SC, Bangers, Dancing Script, Pacifico,
   Kaushan Script, Lobster, Sacramento, Andika sowie die deutschen Schulschriften **Playwrite DE Grund, SAS, VA und LA**.
   Dazu 8 normale Schriften (DejaVu, Liberation), damit normaler Druck nicht verlernt wird. Liste: `fonts_train.txt`.
2. **Texte:** eigene Kinderbuch-Sätze (`saetze.txt`), zufällige Wortfolgen aus den 25 000 häufigsten deutschen Wörtern
   (Paket `wordfreq`), Zeilen in Großbuchstaben (Handlettering), Zahlen und Namen.
3. **Zeilenbilder** (`gen.py`): 30–60 px Schrift, verschiedene Papier- und Kastenfarben, schwacher Kontrast,
   leichte Drehung und Schrägstellung, ungleichmäßiges Licht, Unschärfe, Rauschen, JPEG-Artefakte.
   Insgesamt rund 11 700 Trainingszeilen (`build.sh`).
4. **Nachtrainieren** (`train.sh`): `lstmtraining --continue_from deu.lstm`, Lernrate 0,0001, etwa ein Durchgang
   durch alle Zeilen (12 000 Zeilen), danach `--stop_training --convert_to_int`.

## Ergebnis (Zeichenfehler / falsche Wörter)

| Test | Standard-Modell | Kinderbuch-Modell |
|---|---|---|
| 480 Zeilen in 8 **nicht trainierten** Zierschriften (Mali, Sriracha, Bad Script, Delius Swash Caps, Mansalva, Playwrite AT, Charm, Special Elite) | 2,6 % / 8,7 % | **1,6 % / 4,4 %** |
| 160 Zeilen in normalen Schriften | 0,5 % / 3,6 % | **0,1 % / 0,1 %** |
| 17 ausgeschnittene Zeilen aus echten Buchfotos | 0,5 % / 3,1 % | 0,5 % / 3,1 % |
| 6 ganze Seiten (gefundene Wörter) | 286 / 291 | 285 / 291 |

Auf Zeilenebene halbiert das Modell die Wortfehler bei unbekannten Zierschriften. Bei ganzen Seiten ist es gleich gut;
der begrenzende Faktor ist dort meist das **Finden** der Textstellen, nicht das Lesen der Buchstaben.

Echte Handschrift ist nicht enthalten (keine frei ladbaren deutschen Handschrift-Daten verfügbar);
die Handschrift-Fonts decken nur gleichmäßige „Druck-Handschrift“ ab.

## Nachbauen

Benötigt Tesseract 5 mit Trainingswerkzeugen (`lstmtraining`, `combine_tessdata`), Python mit Pillow, fontTools, wordfreq.
`deu.traineddata` aus `tessdata_best` herunterladen, Schriften nach `fonts/*.woff` legen, dann `build.sh` und `train.sh`.
