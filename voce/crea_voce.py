# Crea i file audio della voce del tutorial con la stessa voce AI di Ciaksigira (MiniMax Speech 02 HD su RunPod).
# Lo esegue GitHub da solo quando cambia voce/testi.json: crea solo le frasi nuove e toglie quelle non più usate.
# La chiave RunPod sta nei "Secrets" di GitHub (RUNPOD_API_KEY), mai nell'app.
import json, os, time, urllib.request
VOCE = 'Patient_Man'   # altre voci maschili: Deep_Voice_Man, Elegant_Man, Determined_Man, Casual_Guy
VELOCITA = 1.0
D = os.path.dirname(os.path.abspath(__file__))
KEY = os.environ['RUNPOD_API_KEY'].strip()
API = os.environ.get('VOCE_API', 'https://api.runpod.ai/v2/minimax-speech-02-hd')
def rp(path, body=None):
    req = urllib.request.Request(API + path, data=json.dumps(body).encode() if body else None,
                                 headers={'Authorization': 'Bearer ' + KEY, 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())
def link(out):
    if isinstance(out, str): return out
    if isinstance(out, dict):
        for k in ('audio_url', 'result', 'url', 'audio'):
            if isinstance(out.get(k), str): return out[k]
        if isinstance(out.get('output'), dict): return link(out['output'])
    return None
L = json.load(open(os.path.join(D, 'testi.json'), encoding='utf-8'))
voluti = {e['h']: e['t'] for e in L}
for f in os.listdir(D):
    if f.endswith('.mp3') and f[:-4] not in voluti:
        os.remove(os.path.join(D, f))
mancano = [(h, t) for h, t in voluti.items() if not os.path.exists(os.path.join(D, h + '.mp3'))]
print('Da creare:', len(mancano), '- caratteri:', sum(len(t) for _, t in mancano))
for n, (h, t) in enumerate(mancano, 1):
    for prova in range(3):
        try:
            r = rp('/run', {'input': {'prompt': t, 'voice_id': VOCE, 'speed': VELOCITA, 'volume': 1, 'pitch': 0,
                                      'emotion': 'neutral', 'english_normalization': False}})
            out = r.get('output') if r.get('status') == 'COMPLETED' else None
            for _ in range(80):
                if out is not None: break
                time.sleep(2.5)
                s = rp('/status/' + r['id'])
                if s.get('status') == 'COMPLETED': out = s.get('output')
                elif s.get('status') in ('FAILED', 'CANCELLED', 'TIMED_OUT'): raise RuntimeError(str(s.get('error') or s.get('status')))
            u = link(out)
            if not u: raise RuntimeError('nessun audio: ' + json.dumps(out)[:200])
            with urllib.request.urlopen(u, timeout=120) as a, open(os.path.join(D, h + '.mp3'), 'wb') as f:
                f.write(a.read())
            print(n, '/', len(mancano), h)
            break
        except Exception as e:
            print('Errore su', h, '(tentativo', prova + 1, '):', e)
            time.sleep(5)
    else:
        print('Frase saltata, verrà riprovata al prossimo giro:', h)
