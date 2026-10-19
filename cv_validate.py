from pathlib import Path
from html.parser import HTMLParser
root=Path(r"C:\Users\Public\newgentle-cv-pr-20261019")
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=set();self.links=[];self.images=[];self.lang=None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="html":self.lang=a.get("lang")
        if "id" in a:self.ids.add(a["id"])
        if tag=="a":self.links.append(a.get("href",""))
        if tag=="img":self.images.append(a.get("src",""))
for file in (root/"index.html",root/"ru"/"index.html"):
    s=file.read_text(encoding="utf-8");p=Page();p.feed(s)
    broken=[x for x in p.links if x.startswith("#") and x[1:] not in p.ids]
    assert p.lang in ("ru","en")
    assert not broken,(file,broken)
    assert all((file.parent/x).exists() for x in p.images)
    assert "CV_preview_" not in s
    assert "@media print" in s
    assert "application/ld+json" in s
    assert "contact-section{display:block!important" in s
    print(file.relative_to(root), "PASS", "lang",p.lang,"ids",len(p.ids),"links",len(p.links),"images",len(p.images),"bytes",len(s.encode()))
print("LOCAL_VALIDATION_PASS")
