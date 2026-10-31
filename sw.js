/* mRead – Offline-Speicher (Service Worker)
   Beim ersten Öffnen werden App, Schrift und Texterkennung auf dem iPad gespeichert.
   Danach funktioniert mRead auch ohne Internet. KI-Stimmen werden gespeichert, sobald sie einmal geladen wurden.
   Bei Änderungen an Dateien in vendor/ oder tessdata/ die Versionsnummer erhöhen. */
var APP = "mread-app-6";
var BIG = "mread-voices-1";      // große Dateien (KI-Stimmen, Sprachmodelle) – bleiben bei App-Updates erhalten
var SHELL = [
  "./", "index.html", "apple-touch-icon.png", "favicon.png", "manifest.webmanifest", "icon-192.png",
  "shortcut-foto.png", "shortcut-weiter.png", "shortcut-einfuegen.png",
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
    // nur eigene alte Speicher löschen – andere Apps unter github.io (z. B. Wortmaler) teilen sich den Speicher
    return Promise.all(keys.filter(function(k){ return /^mread-app-/.test(k) && k !== APP; }).map(function(k){ return caches.delete(k); }));
  }).then(function(){ return self.clients.claim(); }));
});

function isBig(url){ return /\/(voices|vendor\/piper|vendor\/ort)\//.test(url); }

// Android: Foto oder Text über „Teilen“ an mRead schicken (siehe share_target in manifest.webmanifest)
function shared(req){
  return req.formData().then(function(fd){
    var file = fd.get("image");
    if(file && file.size){
      return caches.open("mread-share").then(function(c){
        return c.put("geteiltes-foto", new Response(file, { headers: { "Content-Type": file.type || "image/jpeg" } }));
      }).then(function(){ return Response.redirect("./?geteilt=foto", 303); });
    }
    var text = [fd.get("title"), fd.get("text"), fd.get("url")].filter(function(t){ return t && String(t).trim(); }).join("\n");
    return Response.redirect("./#t=" + encodeURIComponent(text), 303);
  }).catch(function(){ return Response.redirect("./", 303); });
}

self.addEventListener("fetch", function(e){
  var req = e.request;
  var url = new URL(req.url);
  if(req.method === "POST" && url.origin === location.origin && /\/teilen$/.test(url.pathname)){ e.respondWith(shared(req)); return; }
  if(req.method !== "GET") return;
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
