// rooMusic: tiene l'app disponibile anche senza internet (le funzioni online restano online)
const C='roomusic-v2',LIB='purevoltage-lib'; /* LIB tiene il vecchio nome: così le librerie già scaricate restano */
/* motore degli amplificatori e altre librerie prese da internet: si salvano, così la Sala prove suona anche senza connessione */
const LIBHOST=/(^|\.)(cdn\.jsdelivr\.net|esm\.sh)$/;
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png','./icon-maskable-512.png','./rm-text.woff2','./rm-text-italic.woff2'])));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C&&x!==LIB).map(x=>caches.delete(x)))));self.clients.claim()});
self.addEventListener('fetch',e=>{const u=new URL(e.request.url);if(e.request.method!=='GET')return;
  if(u.origin!==location.origin){if(!LIBHOST.test(u.hostname))return;
    e.respondWith(fetch(e.request).then(r=>{if(r.ok){const cp=r.clone();caches.open(LIB).then(c=>c.put(e.request,cp))}return r}).catch(()=>caches.match(e.request,{cacheName:LIB}).then(r=>r||Response.error())));return}
  /* controllo della versione e ricaricamento dopo un aggiornamento: sempre da internet, senza salvarli */
  if(u.searchParams.has('vc')||u.searchParams.has('r'))return;
  /* la pagina dell'app si chiede sempre fresca (senza la copia vecchia del browser), così dopo un aggiornamento arriva subito la versione nuova */
  const page=e.request.mode==='navigate'||/(\/|\.html)$/.test(u.pathname);
  /* se il sito si è spostato (es. su roomusic.it) il browser segue il rimando invece di restare sulla copia vecchia */
  const nav=e.request.mode==='navigate';
  e.respondWith((page?fetch(u.href,{cache:'no-cache',credentials:'same-origin',redirect:nav?'manual':'follow'}):fetch(e.request)).then(r=>{if(r.type==='opaqueredirect')return r;if(!r.ok){if(page)throw new Error('http '+r.status);return r}const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request).then(r=>r||caches.match('./index.html'))))});
