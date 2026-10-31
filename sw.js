/* mRead – Offline-Speicher (Service Worker)
   Beim ersten Öffnen werden App, Schrift und Texterkennung auf dem iPad gespeichert.
   Danach funktioniert mRead auch ohne Internet. KI-Stimmen werden gespeichert, sobald sie einmal geladen wurden.
   Bei Änderungen an Dateien in vendor/ oder tessdata/ die Versionsnummer erhöhen. */
var APP = "mread-app-3";
var BIG = "mread-voices-1";      // große Dateien (KI-Stimmen, Sprachmodelle) – bleiben bei App-Updates erhalten
var SHELL = [
  "./", "index.html", "apple-touch-icon.png", "favicon.png",
  "vendor/andika/andika-latin-400-normal.woff2", "vendor/andika/andika-latin-700-normal.woff2",
  "vendor/andika/andika-latin-ext-400-normal.woff2", "vendor/andika/andika-latin-ext-700-normal.woff2",
  "vendor/tesseract/tesseract.min.js", "vendor/tesseract/worker.min.js", "vendor/tesseract/tesseract-core-simd-lstm.wasm.js",
  "tessdata/deu.traineddata.gz"
];

self.addEventListener("install", function(e){
  e.waitUntil(caches.open(APP).then(function(c){ return c.addAll(SHELL); }).then(function(){ return self.skipWaiting(); }));
});

self.addEventListener("activate", function(e){
  e.waitUntil(caches.keys().then(function(keys){
    return Promise.all(keys.filter(function(k){ return k !== APP && k !== BIG; }).map(function(k){ return caches.delete(k); }));
  }).then(function(){ return self.clients.claim(); }));
});

function isBig(url){ return /\/(voices|vendor\/piper|vendor\/ort)\//.test(url); }

self.addEventListener("fetch", function(e){
  var req = e.request;
  if(req.method !== "GET") return;
  var url = new URL(req.url);
  if(url.origin !== location.origin) return;
  // die App selbst: erst im Internet nach einer neuen Fassung schauen, sonst die gespeicherte nehmen
  if(req.mode === "navigate" || /\/(index\.html)?$/.test(url.pathname)){
    e.respondWith(fetch(req).then(function(res){
      if(res.ok){ var copy = res.clone(); caches.open(APP).then(function(c){ c.put("index.html", copy); }); }
      return res;
    }).catch(function(){
      return caches.match("index.html", { ignoreSearch: true });
    }));
    return;
  }
  // alles andere: gespeicherte Fassung, sonst laden und speichern
  e.respondWith(caches.match(req, { ignoreSearch: true }).then(function(hit){
    if(hit) return hit;
    return fetch(req).then(function(res){
      if(res.ok && res.status === 200){
        var copy = res.clone();
        caches.open(isBig(url.pathname) ? BIG : APP).then(function(c){ c.put(req, copy); });
      }
      return res;
    });
  }));
});
