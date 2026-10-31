# mRead

Eine einfache Web-App fürs iPad, mit der Kinder Fotos von gedruckten Texten machen und sich den Text vorlesen lassen. Der erkannte Text erscheint groß in kindgerechter Druckschrift, beim Vorlesen läuft eine gelbe Markierung mit.

**App öffnen:** https://gionessbach.github.io/mread/

## Funktionen

- **Foto machen:** Der große gelbe Knopf öffnet die Kamera. Über den Bild-Knopf unten links lässt sich auch ein Foto aus der Mediathek wählen.
- **Texterkennung:** Der Text wird direkt auf dem iPad erkannt (Deutsch). Bilder und Verzierungen auf der Seite werden weitgehend ignoriert, am Zeilenende getrennte Wörter wieder zusammengesetzt.
- **Vorlesen:** Der gelbe Abspiel-Knopf liest den ganzen Text vor. Der aktuelle Satz wird hellgelb, das aktuelle Wort kräftig gelb markiert. Stopp hält an, beim nächsten Tippen geht es beim gleichen Satz weiter.
- **Wort antippen:** Liest genau dieses Wort vor.
- **Tempo:** Umschalten zwischen normal und langsam.
- **A− / A+:** Schrift kleiner oder größer.
- **Abc / ABC:** Umschalten zwischen normaler Schreibweise und Großbuchstaben. Ä, Ö, Ü bleiben erhalten, ß wird zum großen ẞ.
- **Foto ansehen:** Das kleine Vorschaubild oben zeigt das Originalfoto zum Vergleichen.
- **Wortfilter:** Gängige Schimpfwörter werden als *** angezeigt und nicht vorgelesen.
- Der zuletzt erkannte Text bleibt gespeichert, auch wenn die App geschlossen wird.

Die Schrift ist [Andika](https://fonts.google.com/specimen/Andika), eine Druckschrift für Leseanfänger.

## Tipps für gute Fotos

- Das iPad gerade und ruhig über die Seite halten, die ganze Zeile muss im Bild sein.
- Gutes Licht, keine Schatten auf dem Text.
- Lieber nah an den Text heran als die ganze Doppelseite.

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

Eine einzige Datei (`index.html`) ohne Build-Schritt. Texterkennung mit [Tesseract.js](https://github.com/naptha/tesseract.js) (läuft im Browser, deutsche Sprachdaten von jsDelivr), Vorlesen mit der Web Speech API, Speicherung in `localStorage`. Gehostet über GitHub Pages.

Gedacht für die private Nutzung auf einem eigenen iPad.
