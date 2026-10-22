from pathlib import Path
from html.parser import HTMLParser
import json,re
R=Path(__file__).resolve().parents[1]
class P(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.links=[];self.h1=0
 def handle_starttag(self,t,a):
  v=dict(a)
  if v.get('id'):self.ids.add(v['id'])
  if t=='a' and v.get('href'):self.links.append(v['href'])
  if t=='h1':self.h1+=1
for loc in ('en','ru'):
 rel='ru/index.html' if loc=='ru' else 'index.html'
 s=(R/rel).read_text('utf-8');p=P();p.feed(s)
 assert p.h1==1
 assert not re.search(r'10\\.(64|65)\\.0\\.|172\\.27\\.228\\.',s)
 for href in p.links:
  if href.startswith('#'): assert href[1:] in p.ids,(rel,href)
  elif not href.startswith(('http:','https:','mailto:','tel:')):
   target=((R/rel).parent/href)
   assert target.is_file() or (target.is_dir() and (target/'index.html').is_file()),(rel,href)
 data=json.loads((R/'site/content'/f'{loc}.json').read_text('utf-8'))
 assert len(data['experience']['jobs'])>=7 and len(data['experience']['early'])>=9
 assert not data['projects']
 pdf=R/'assets'/f'Akbar_Abdullaev_CV_{loc.upper()}.pdf'
 raw=pdf.read_bytes()
 assert raw.startswith(b'%PDF-') and len(raw)>10000
 assert pdf.name in s
 print('PASS',loc,'PDF',len(raw),'bytes')
print('CV_QUALITY_GATE_PASS')
