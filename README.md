# mRead

Eine einfache Web-App fürs iPad, mit der Kinder Fotos von gedruckten Texten machen und sich den Text vorlesen lassen. Der erkannte Text erscheint groß in kindgerechter Druckschrift, beim Vorlesen läuft eine gelbe Markierung mit.

**App öffnen:** https://gionessbach.github.io/mread/

## Funktionen

- **Kurzbefehl „mRead Foto“ (empfohlen):** Nutzt die Texterkennung des iPads (Live Text). Sie ist deutlich genauer als die eingebaute und kommt auch mit schrägen oder gewölbten Seiten zurecht. Einrichtung siehe unten.

- **Foto machen:** Der große gelbe Knopf öffnet die Kamera. Über den Bild-Knopf unten links lässt sich auch ein Foto aus der Mediathek wählen.
- **Bereich wählen:** Nach dem Foto erscheint ein gelber Rahmen. Unten rechts lässt sich umschalten:
  - **Rechteck** (Standard): Eine Ecke ziehen ändert die Größe, das Rechteck bleibt gerade.
  - **4 Ecken:** Jede Ecke einzeln auf die Ecken des Textes oder der Seite ziehen – auch schräg. mRead zieht das Foto dann gerade, als wäre es genau von oben aufgenommen. Das verbessert die Erkennung bei schräg fotografierten oder gewölbten Seiten deutlich. Liegt das ganze Blatt sichtbar auf einem dunkleren Untergrund, **findet mRead die Seitenecken selbst** – dann nur noch prüfen und bei Bedarf nachziehen.

  In den Rahmen tippen und ziehen verschiebt ihn, daneben ziehen legt ein neues Rechteck an. „Ganzes Foto“ nimmt alles, der Dreh-Knopf unten links dreht das Foto um 90° (wichtig, wenn der Text quer liegt – sonst kann er nicht erkannt werden), der gelbe Haken startet das Lesen. Die gewählte Form merkt sich mRead.
- **Eingebaute Texterkennung:** Der Text wird direkt im Browser erkannt (Deutsch). Sie braucht ein gerade von oben aufgenommenes Foto. Auch verstreute Texte wie Beschriftungen neben Bildern werden gefunden und als eigene Bausteine behandelt. Bilder und Verzierungen auf der Seite werden weitgehend ignoriert, am Zeilenende getrennte Wörter wieder zusammengesetzt.
- **Kinderbuch-Schriften** (Zahnrad, standardmäßig an): mRead nutzt ein eigenes, nachtrainiertes deutsches Erkennungsmodell, das zusätzlich 63 Zier-, Comic-, Schreibschrift-, Handschrift- und Grundschul-Schriften kennt. Bei unbekannten Zierschriften halbiert es die Wortfehler, normale Schrift liest es mindestens so gut. Echte Handschrift deckt es nicht ab. Abschaltbar, dann wird das normale Modell verwendet. Details: [training/README.md](training/README.md).
- **Automatische Bildaufbereitung:** Vor dem Lesen wird das Foto Stück für Stück aufgehellt und der Kontrast verstärkt. Blasse Schrift, Text in farbigen Kästen und Schatten werden so besser erkannt. Ist das Ergebnis unsicher, liest mRead zusätzlich das unbearbeitete Foto und nimmt das bessere Ergebnis.
- **Lesereihenfolge wie ein Mensch:** mRead ordnet die Textbausteine nach ihrer Lage auf dem Foto: Bei einer Doppelseite oder echten Spalten erst links, dann rechts; sonst von oben nach unten, nebeneinander von links nach rechts. Sätze, die über mehrere Zeilen oder Bausteine laufen, werden wieder zu einem Satz verbunden.
- **Absätze wie im Original:** Überschriften, Absätze und Aufzählungspunkte aus dem Foto erscheinen auch in mRead als eigene Absätze. Erkannt werden sie an größerem Zeilenabstand, Einrückung, kurzer letzter Zeile, größerer Schrift oder einem Aufzählungspunkt. Beim Vorlesen gibt es an jedem Absatz eine kleine Pause.
- **Foto-Ansicht** (Umschalter oben rechts „Foto | Text“): Nach dem Lesen bleibt das Foto sichtbar. Beim Vorlesen leuchtet das gesprochene Wort direkt auf dem Foto auf, der ganze Satz leicht dahinter. Alle Texte, die vorgelesen werden können, sind hellgelb hinterlegt wie mit einem Textmarker; die Schrift bleibt dabei lesbar. Mit „Markierung“ oben rechts im Foto lässt sich das ausblenden. Mit zwei Fingern lässt sich das Foto vergrößern und verschieben (am Computer mit dem Mausrad); beim Vorlesen wandert das vergrößerte Foto mit. Die Lupe unten rechts zeigt wieder das ganze Foto. Mit **„Drehen“** oben rechts lässt sich das Foto samt Markierungen um 90° drehen, zum Beispiel wenn es quer aufgenommen wurde.
- **Bereich neu lesen** (gelber Knopf oben links in der Foto-Ansicht): Wurde etwas nicht oder falsch erkannt, einen Rahmen um diese Stelle ziehen. Passt der Rahmen nicht, einfach neu ziehen. Mit **„Lesen“** bestätigen (oder „Abbrechen“). Nur dieser Bereich wird noch einmal genauer gelesen (vergrößert und mit beiden Bildfassungen); die alten Wörter dort werden ersetzt, alles andere bleibt unverändert. Der neu erkannte Text wird danach sofort vorgelesen. Funktioniert auch im vergrößerten Foto. Ein Tipp auf eine markierte Zeile liest genau diesen Textbaustein vor, zum Beispiel eine Beschriftung neben einem Bild. Ideal für Kinder, die noch nicht lesen können. Gibt es nur bei Fotos, die mRead selbst liest (nicht beim Kurzbefehl oder Einfügen).
- **Lange drücken** (Foto-Ansicht): Einen Finger etwa eine halbe Sekunde auf eine Stelle halten – ein gelber Ring wächst. mRead liest dann die Umgebung dieser Stelle genauer und **ergänzt Text, der bisher gefehlt hat**, ohne das schon Erkannte zu verändern. Das Neue wird sofort vorgelesen. Gibt es dort nichts Neues, wird der Text an dieser Stelle vorgelesen. Einfacher als einen Rahmen zu ziehen, gut für Kinder.
- **Reihenfolge festlegen** (Knopf mit Nummernliste oben rechts in der Foto-Ansicht): Die Texte nacheinander antippen, in der gewünschten Lese-Reihenfolge. Neben jedem erscheint eine Nummer; nochmal antippen nimmt die Nummer weg. Mit **„Fertig“** übernehmen. Nicht angetippte Texte kommen danach in der bisherigen Reihenfolge. Praktisch bei Comics, Rätselseiten und Bildern mit vielen Beschriftungen.
- **Text-Ansicht:** Der erkannte Text groß als Fließtext, wie bisher.
- **Vorlesen:** Der gelbe Abspiel-Knopf liest den ganzen Text vor. Der aktuelle Satz wird hellgelb, das aktuelle Wort kräftig gelb markiert. Stopp hält an, beim nächsten Tippen geht es beim gleichen Satz weiter.
- **Wort antippen:** Liest genau dieses Wort vor.
- **Text einfügen** (Klemmbrett-Knopf): Fügt kopierten Text ein. Damit lässt sich auch mit Apples Texterkennung ein Bereich wählen: Foto in der Fotos-App öffnen, auf den Text tippen und halten, die Auswahl mit den Griffen auf den gewünschten Absatz ziehen, „Kopieren“, dann in mRead einfügen.
- **Stimme wählen** (Zahnrad): Alle deutschen Stimmen des iPads zum Probehören. Die beste wird automatisch gewählt.
- **KI-Stimmen** (Zahnrad → „KI-Stimmen“): **Kerstin, Ramona** (Frauenstimmen) und **Thorsten** (Männerstimme) klingen natürlicher als die meisten iPad-Stimmen und laufen ganz auf dem iPad, ohne Internet. Beim ersten Antippen wird die Stimme einmalig geladen (ca. 90 MB für die erste, ca. 63 MB für jede weitere – am besten im WLAN), danach steht „bereit – auch ohne Internet“. Die Wortmarkierung beim Vorlesen ist bei KI-Stimmen geschätzt und kann etwas vor- oder nachlaufen. Der erste Satz braucht nach dem Öffnen der App ein paar Sekunden. Zurück zur iPad-Stimme: einfach eine Stimme unter „Stimmen des iPads“ antippen. Braucht iPadOS 16.4 oder neuer.
- **Gründlich suchen** (Zahnrad, standardmäßig aus): mRead sucht zusätzlich nach einzelnen, verstreuten Wörtern und liest das Foto noch einmal in vier vergrößerten Stücken. Findet etwas mehr kleine Beschriftungen, das Lesen dauert dafür etwa doppelt so lange. Im Test: 287 statt 285 von 291 Wörtern auf 6 Testseiten.
- **Satz für Satz** (Knopf links neben dem Tempo, „Am Stück“ / „Satzweise“): mRead liest einen Satz und wartet dann. Der große Knopf zeigt „Weiter“ (Pfeil mit Strich) und liest den nächsten Satz. Der gerade gelesene Satz bleibt markiert – gut zum Mitlesen und Nachsprechen.
- **Tempo:** Umschalten zwischen normal und langsam.
- **A− / A+:** Schrift kleiner oder größer.
- **Abc / ABC:** Umschalten zwischen normaler Schreibweise und Großbuchstaben. Ä, Ö, Ü bleiben erhalten, ß wird zum großen ẞ.
- **Wortfilter:** Gängige Schimpfwörter werden als *** angezeigt und nicht vorgelesen.
- Der zuletzt erkannte Text bleibt gespeichert, auch wenn die App geschlossen wird.
- **Ohne Internet nutzbar:** Nach dem ersten Öffnen mit Internet funktioniert mRead komplett offline – Fotos lesen, Vorlesen mit iPad-Stimme und mit einmal geladenen KI-Stimmen. Alles liegt auf dem iPad, nichts wird ins Internet geschickt.

Die Schrift ist [Andika](https://fonts.google.com/specimen/Andika), eine Druckschrift für Leseanfänger (liegt in `vendor/andika`).

## Tipps für gute Fotos

- Das iPad **genau von oben** über die Seite halten, nicht schräg. Die ganze Zeile muss im Bild sein.
- Gutes Licht, keine Schatten auf dem Text.
- Lieber nah an den Text heran als die ganze Doppelseite.

## Kurzbefehl „mRead Foto“ einrichten

Einmalig in der App **Kurzbefehle** auf dem iPad:

1. Unten rechts bzw. oben auf **+** tippen, um einen neuen Kurzbefehl anzulegen. Oben als Namen **mRead Foto** eintragen.
2. Aktion **Foto aufnehmen** hinzufügen (im Suchfeld „Foto aufnehmen“ eingeben). Über den kleinen Pfeil kann **Vorschau anzeigen** ausgeschaltet werden, dann geht es schneller.
3. Aktion **Text aus Bild extrahieren** hinzufügen. Als Eingabe ist automatisch das Foto eingetragen.
4. Aktion **URL codieren** hinzufügen (im Suchfeld „codieren“ eingeben). Eingabe: der Text aus dem Bild.
5. Aktion **URL** hinzufügen und hineinschreiben: `https://gionessbach.github.io/mread/#t=`
   Direkt dahinter, ohne Leerzeichen, die Variable **URL-codierter Text** einfügen (sie erscheint über der Tastatur).
6. Aktion **URLs öffnen** hinzufügen.
7. Oben auf den Namen bzw. das Info-Symbol tippen → **Zum Home-Bildschirm**. Als Symbol kann ein Foto gewählt werden, zum Beispiel ein Bildschirmfoto des mRead-Logos.

Beim ersten Start fragt das iPad, ob der Kurzbefehl die Kamera nutzen und die Website öffnen darf. Beides mit **Erlauben** (bzw. **Immer erlauben**) bestätigen.

Danach: Symbol **mRead Foto** antippen → Foto machen → mRead öffnet sich mit dem erkannten Text.

Hinweis: Der Kurzbefehl öffnet mRead in **Safari**. Safari und ein Home-Bildschirm-Symbol der Website speichern ihre Einstellungen getrennt. Die Stimme also in der Safari-Version auswählen, die der Kurzbefehl öffnet.

## Einrichtung auf dem iPad

1. Die Adresse oben in **Safari** öffnen.
2. Über **Teilen → Zum Home-Bildschirm** als App-Symbol ablegen.
3. Beim ersten Öffnen speichert die App sich selbst, die Schrift und die Texterkennung auf dem iPad (ca. 6 MB). Danach geht es auch ohne Internet.
   Tipp: Als Home-Bildschirm-App bleibt der Speicher dauerhaft erhalten; in Safari kann iPadOS ihn nach längerer Nichtbenutzung löschen.
4. Tipp: Mit dem **Geführten Zugriff** (Einstellungen → Bedienungshilfen) lässt sich das iPad auf diese App sperren.

## Wortfilter erweitern

In `index.html` nach `EIGENE_WOERTER` suchen und Wörter klein geschrieben (ß als ss) eintragen:

```js
var EIGENE_WOERTER = ["doofi", "bloedmann"];
```

## Hinweise

- Erkannt wird **gedruckter** Text. Handschrift funktioniert kaum.
- Sehr verschnörkelte Schriften, Text auf bunten Bildern oder schräg fotografierte Seiten können Fehler ergeben.
- Fotos und Texte bleiben auf dem iPad. mRead lädt nur seine eigenen Dateien von GitHub Pages, keine fremden Dienste.

## Technik

Die App ist eine einzige Datei (`index.html`) ohne Build-Schritt. Text vom Kurzbefehl kommt über `#t=<URL-codierter Text>` in die Seite. Gehostet über GitHub Pages.

- **Texterkennung:** [Tesseract.js](https://github.com/naptha/tesseract.js) 5.1.1, alle Dateien in `vendor/tesseract/`. Kinderbuch-Modell in `tessdata/`, Standardmodell in `tessdata/std/`.
- **Vorlesen:** Web Speech API (iPad-Stimmen) oder [Piper](https://github.com/rhasspy/piper) (KI-Stimmen): Lautschrift mit espeak-ng als WebAssembly (`vendor/piper/`, aus `@diffusionstudio/piper-wasm`), Sprachmodelle `voices/*.onnx` (Piper-Stimmen „de-kerstin-low“, „de-ramona-low“, „de-thorsten-low“, 16 kHz), ausgeführt mit [onnxruntime-web](https://onnxruntime.ai) 1.18 (`vendor/ort/`).
- **Offline:** `sw.js` (Service Worker) speichert App, Schrift und Texterkennung beim ersten Öffnen; KI-Stimmen, sobald sie das erste Mal geladen werden. Nach Änderungen an Dateien in `vendor/` oder `tessdata/` die Versionsnummer `APP` in `sw.js` erhöhen.
- **Speicherung** des letzten Textes und der Einstellungen in `localStorage`.

Gedacht für die private Nutzung auf einem eigenen iPad.
