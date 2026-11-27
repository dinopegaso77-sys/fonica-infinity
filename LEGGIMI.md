# rooMusic

La sala prove nel browser: tracce separate, testo sincronizzato, tablature, effetti, lezioni e video.

**Indirizzo dell'app:** https://roomusic.it
(il vecchio indirizzo `dinopegaso77-sys.github.io/fonica-infinity` porta qui da solo)

## Installarla sul telefono o sul tablet
Apri l'indirizzo con Chrome → menu **⋮** → **Aggiungi a schermata Home** (o **Installa app**).
Compare l'icona di rooMusic come una vera app.

## Cosa c'è in questo repository
| File o cartella | A cosa serve |
|---|---|
| `index.html` | tutta l'app |
| `sw.js` | fa funzionare l'app anche senza internet |
| `manifest.webmanifest`, `icon-*.png`, `apple-touch-icon.png` | icona e installazione |
| `rm-*.svg`, `rm-share.jpg`, `rm-text*.woff2` | logo, immagine quadrata per i link condivisi, caratteri |
| `intro-roomusic-chiaro.mp4`, `intro-roomusic-scuro.mp4` | animazione di apertura |
| `presentazione.html` | pagina che presenta l'app |
| `CNAME` | lo crea GitHub quando imposti il dominio: dice di pubblicare il sito su roomusic.it |
| `robots.txt`, `sitemap.xml` | aiutano Google a trovare e mostrare il sito |
| `video/` | video tutorial (orizzontale e verticale), copertine e tempi della voce |
| `voce/` | voce del tutorial e del video: `testi.json` (le frasi), `crea_voce.py` e i file `.mp3` |
| `.github/workflows/voce.yml` | crea da solo i file della voce |

## Aggiornare l'app
Carica i file ricevuti nello zip su questo repository (sostituiscono i vecchi) e premi **Commit changes**.
Chi usa l'app riceve l'aggiornamento alla successiva apertura.

## La voce del tutorial si aggiorna da sola
Quando carichi un nuovo `voce/testi.json`, GitHub Actions esegue `voce/crea_voce.py`:
crea solo le frasi nuove, toglie quelle non più usate, salva i `.mp3` nella cartella `voce/` e ripubblica il sito.
Non devi fare nulla a mano. Per rifarlo comunque: **Actions → Voce del tutorial → Run workflow**.

Serve una sola cosa, già fatta una volta: il segreto **RUNPOD_API_KEY** in
**Settings → Secrets and variables → Actions**. La chiave resta su GitHub e non entra mai nell'app.

## Privacy, in breve
La privacy è tutelata: **rooMusic non ha archivi propri** e nessun brano, registrazione, chiave o dato personale resta nei sistemi dell'autore.
- Brani, tracce, impostazioni e chiavi restano nella memoria del browser di chi usa l'app.
- Il cloud **R2** e **RunPod** sono account dell'utente, a suo nome: solo lui ha le chiavi, l'autore non vi accede. Su RunPod i file si cancellano a lavoro finito.
- Ai siti esterni (testi, copertine, MVSEP, TONE3000) va solo ciò che serve, quando l'utente lo sceglie; rooMusic non ne tiene copie.
- All'autore arrivano solo i messaggi scritti con «Dimmi la tua». Niente pubblicità, niente tracciamento.
Il testo completo è nell'app, alla voce «Note legali». Contatti: info@roomusic.it

## Dominio roomusic.it
- Registrato su Aruba. Nella Gestione DNS: quattro record **A** (`185.199.108.153`, `.109.153`, `.110.153`, `.111.153`)
  e un **CNAME** `www` → `dinopegaso77-sys.github.io`. I record della mail (MX) non si toccano.
- Su GitHub: **Settings → Pages → Custom domain** = `roomusic.it`, poi spunta **Enforce HTTPS**.
- Chi usava l'app al vecchio indirizzo recupera brani e chiavi con «Recupera i brani»:
  lo fa la piccola pagina del repository `roomusic-trasloco`.
