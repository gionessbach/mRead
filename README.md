# mRead

Eine einfache Web-App fürs iPad, mit der Kinder Fotos von gedruckten Texten machen und sich den Text vorlesen lassen. Der erkannte Text erscheint groß in kindgerechter Druckschrift, beim Vorlesen läuft eine gelbe Markierung mit.

**App öffnen:** https://gionessbach.github.io/mread/

## Funktionen

- **Kurzbefehl „mRead Foto“ (empfohlen):** Nutzt die Texterkennung des iPads (Live Text). Sie ist deutlich genauer als die eingebaute und kommt auch mit schrägen oder gewölbten Seiten zurecht. Einrichtung siehe unten.

- **Foto machen:** Der große gelbe Knopf öffnet die Kamera. Über den Bild-Knopf unten links lässt sich auch ein Foto aus der Mediathek wählen.
- **Bereich wählen:** Nach dem Foto erscheint ein gelber Rahmen. Unten rechts lässt sich umschalten:
  - **Rechteck** (Standard): Eine Ecke ziehen ändert die Größe, das Rechteck bleibt gerade.
  - **4 Ecken:** Jede Ecke einzeln auf die Ecken des Textes oder der Seite ziehen – auch schräg. mRead zieht das Foto dann gerade, als wäre es genau von oben aufgenommen. Das verbessert die Erkennung bei schräg fotografierten oder gewölbten Seiten deutlich.

  In den Rahmen tippen und ziehen verschiebt ihn, daneben ziehen legt ein neues Rechteck an. „Ganzes Foto“ nimmt alles, der gelbe Haken startet das Lesen. Die gewählte Form merkt sich mRead.
- **Eingebaute Texterkennung:** Der Text wird direkt im Browser erkannt (Deutsch). Sie braucht ein gerade von oben aufgenommenes Foto. Auch verstreute Texte wie Beschriftungen neben Bildern werden gefunden und als eigene Bausteine behandelt. Bilder und Verzierungen auf der Seite werden weitgehend ignoriert, am Zeilenende getrennte Wörter wieder zusammengesetzt.
- **Automatische Bildaufbereitung:** Vor dem Lesen wird das Foto Stück für Stück aufgehellt und der Kontrast verstärkt. Blasse Schrift, Text in farbigen Kästen und Schatten werden so besser erkannt. Ist das Ergebnis unsicher, liest mRead zusätzlich das unbearbeitete Foto und nimmt das bessere Ergebnis.
- **Absätze wie im Original:** Überschriften, Absätze und Aufzählungspunkte aus dem Foto erscheinen auch in mRead als eigene Absätze. Erkannt werden sie an größerem Zeilenabstand, Einrückung, kurzer letzter Zeile, größerer Schrift oder einem Aufzählungspunkt. Beim Vorlesen gibt es an jedem Absatz eine kleine Pause.
- **Foto-Ansicht** (Umschalter oben rechts „Foto | Text“): Nach dem Lesen bleibt das Foto sichtbar. Beim Vorlesen leuchtet das gesprochene Wort direkt auf dem Foto auf, der ganze Satz leicht dahinter. Alle Texte, die vorgelesen werden können, sind hellgelb hinterlegt wie mit einem Textmarker; die Schrift bleibt dabei lesbar. Mit „Markierung“ oben rechts im Foto lässt sich das ausblenden. Mit zwei Fingern lässt sich das Foto vergrößern und verschieben (am Computer mit dem Mausrad); beim Vorlesen wandert das vergrößerte Foto mit. Die Lupe unten rechts zeigt wieder das ganze Foto.
- **Bereich neu lesen** (Knopf oben links in der Foto-Ansicht): Wurde etwas nicht oder falsch erkannt, einen Rahmen um diese Stelle ziehen. Nur dieser Bereich wird noch einmal genauer gelesen (vergrößert und mit beiden Bildfassungen); die alten Wörter dort werden ersetzt, alles andere bleibt unverändert. Funktioniert auch im vergrößerten Foto. Ein Tipp auf eine markierte Zeile liest genau diesen Textbaustein vor, zum Beispiel eine Beschriftung neben einem Bild. Ideal für Kinder, die noch nicht lesen können. Gibt es nur bei Fotos, die mRead selbst liest (nicht beim Kurzbefehl oder Einfügen).
- **Text-Ansicht:** Der erkannte Text groß als Fließtext, wie bisher.
- **Vorlesen:** Der gelbe Abspiel-Knopf liest den ganzen Text vor. Der aktuelle Satz wird hellgelb, das aktuelle Wort kräftig gelb markiert. Stopp hält an, beim nächsten Tippen geht es beim gleichen Satz weiter.
- **Wort antippen:** Liest genau dieses Wort vor.
- **Text einfügen** (Klemmbrett-Knopf): Fügt kopierten Text ein. Damit lässt sich auch mit Apples Texterkennung ein Bereich wählen: Foto in der Fotos-App öffnen, auf den Text tippen und halten, die Auswahl mit den Griffen auf den gewünschten Absatz ziehen, „Kopieren“, dann in mRead einfügen.
- **Stimme wählen** (Zahnrad): Alle deutschen Stimmen des iPads zum Probehören. Die beste wird automatisch gewählt.
- **Tempo:** Umschalten zwischen normal und langsam.
- **A− / A+:** Schrift kleiner oder größer.
- **Abc / ABC:** Umschalten zwischen normaler Schreibweise und Großbuchstaben. Ä, Ö, Ü bleiben erhalten, ß wird zum großen ẞ.
- **Wortfilter:** Gängige Schimpfwörter werden als *** angezeigt und nicht vorgelesen.
- Der zuletzt erkannte Text bleibt gespeichert, auch wenn die App geschlossen wird.

Die Schrift ist [Andika](https://fonts.google.com/specimen/Andika), eine Druckschrift für Leseanfänger.

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
3. Beim ersten Foto lädt die App die deutsche Texterkennung (ca. 4 MB). Danach geht es schneller.
4. Tipp: Mit dem **Geführten Zugriff** (Einstellungen → Bedienungshilfen) lässt sich das iPad auf diese App sperren.

## Wortfilter erweitern

In `index.html` nach `EIGENE_WOERTER` suchen und Wörter klein geschrieben (ß als ss) eintragen:

```js
var EIGENE_WOERTER = ["doofi", "bloedmann"];
```

## Hinweise

- Erkannt wird **gedruckter** Text. Handschrift funktioniert kaum.
- Sehr verschnörkelte Schriften, Text auf bunten Bildern oder schräg fotografierte Seiten können Fehler ergeben.
- Fotos und Texte bleiben auf dem iPad. Aus dem Internet werden nur die Texterkennung und die Schrift geladen.

## Technik

Eine einzige Datei (`index.html`) ohne Build-Schritt. Text vom Kurzbefehl kommt über `#t=<URL-codierter Text>` in die Seite. Eingebaute Texterkennung mit [Tesseract.js](https://github.com/naptha/tesseract.js) (läuft im Browser, deutsche Sprachdaten von jsDelivr), Vorlesen mit der Web Speech API, Speicherung in `localStorage`. Gehostet über GitHub Pages.

Gedacht für die private Nutzung auf einem eigenen iPad.
