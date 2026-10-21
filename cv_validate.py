from pathlib import Path
from html.parser import HTMLParser
import json
ROOT=Path(__file__).resolve().parent
class HTMLCheck(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.anchors=[];self.resources=[];self.lang=None;self.h1=0;self.main=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if a.get('id'):self.ids.append(a['id'])
  if tag=='a' and a.get('href','').startswith('#'):self.anchors.append(a['href'][1:])
  if tag=='link' and a.get('rel')=='stylesheet':self.resources.append(a.get('href'))
  if tag=='link' and a.get('rel')=='icon':self.resources.append(a.get('href'))
  if tag=='script' and a.get('src'):self.resources.append(a.get('src'))
  if tag=='img' and a.get('src'):self.resources.append(a.get('src'))
  if tag=='h1':self.h1+=1
  if tag=='main':self.main+=1
for loc,files in [('en',['index.html','resume/index.html']),('ru',['ru/index.html','ru/resume/index.html'])]:
 data=json.loads((ROOT/'site'/'content'/(loc+'.json')).read_text(encoding='utf-8'))
 assert data['lang']==loc
 for filename in files:
  path=ROOT/filename;p=HTMLCheck();p.feed(path.read_text(encoding='utf-8'))
  assert p.lang==loc,(filename,p.lang)
  assert len(p.ids)==len(set(p.ids)),filename
  assert not set(p.anchors).difference(p.ids),(filename,set(p.anchors).difference(p.ids))
  assert p.h1==1,(filename,p.h1)
  assert all((path.parent/name).is_file() for name in p.resources if not name.startswith(('https://','http://'))),(filename,p.resources)
  assert not any(key in path.read_text(encoding='utf-8') for key in ('10.64.0.','10.65.0.','172.27.228.'))
  print('PASS',filename,'resources',len(p.resources),'anchors',len(p.anchors))
 assert len(data['projects'])==0
 assert all(x['statusKind'] in ('operational','development') for x in data['projects'])
print('SITE_VALIDATION_PASS')
