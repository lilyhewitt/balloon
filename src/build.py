import base64, json, os, re, urllib.parse
d=os.path.join(os.path.dirname(os.path.abspath(__file__)),'sprites')
src={}
for f in sorted(os.listdir(d)):
    n,ext=os.path.splitext(f)
    mime='image/jpeg' if ext=='.jpg' else 'image/png'
    src[n]='data:%s;base64,%s'%(mime,base64.b64encode(open(os.path.join(d,f),'rb').read()).decode())
t=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'template.html')).read()
chars=set(re.findall(r'[　-鿿＀-￯]',t))|set('0123456789M!…，')
t=t.replace('/*FONTTEXT*/',urllib.parse.quote(''.join(sorted(chars))))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','index.html'),'w').write(t.replace('/*SPRITES*/',json.dumps(src)))
print(os.path.getsize(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','index.html')), len(chars))
