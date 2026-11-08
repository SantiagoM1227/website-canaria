#!/usr/bin/env python3
"""Genera un callejero vectorial autoalojado a partir de datos abiertos de OpenStreetMap.
Fuente: Geofabrik, https://download.geofabrik.de/africa/canary-islands.html
Atribución obligatoria: © OpenStreetMap contributors, ODbL.
La página/archivo roads.js son datos derivados y se distribuyen según los requisitos ODbL.
"""
from __future__ import annotations
import json
import math
import os
from pathlib import Path
import tempfile
from urllib.request import urlretrieve, Request, urlopen

# The GitHub Action installs osmium (pyosmium) at build time.
import osmium

P=Path(__file__).resolve().parent
URL='https://download.geofabrik.de/africa/canary-islands-latest.osm.pbf'
REGION=(-15.755,-15.415,28.064,28.186)
NEAR=(-15.673,-15.585,28.122,28.163)
KINDS={'motorway','trunk','primary','secondary','tertiary','residential','unclassified','service','living_street','pedestrian','footway','path','track','steps'}
ALIASES={'living_street':'residential'}
# Paths in the broader frame are only useful near a proposed excursion.
TRAIL_NEAR=[(-15.633,28.139),(-15.5929,28.0876),(-15.5842,28.1108),(-15.5355,28.1513),(-15.556,28.1458),(-15.5711,28.1443),(-15.7107,28.1026),(-15.4513,28.129),(-15.656,28.145)]

def in_box(lon:float,lat:float,b,buf=0):
 return b[0]-buf<=lon<=b[1]+buf and b[2]-buf<=lat<=b[3]+buf

def simple(points:list[tuple[float,float]], tol:float):
 """Ramer-Douglas-Peucker in degrees; preserve endpoints and characteristic bends."""
 if len(points)<4:return points
 sq=tol*tol
 def dist(p,a,b):
  dx=b[0]-a[0];dy=b[1]-a[1];len2=dx*dx+dy*dy
  if not len2:return (p[0]-a[0])**2+(p[1]-a[1])**2
  t=max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/len2))
  return (p[0]-a[0]-t*dx)**2+(p[1]-a[1]-t*dy)**2
 keep={0,len(points)-1}; stack=[(0,len(points)-1)]
 while stack:
  l,r=stack.pop();a,b=points[l],points[r];mx=-1;which=-1
  for i in range(l+1,r):
   d=dist(points[i],a,b)
   if d>mx:mx=d;which=i
  if mx>sq:keep.add(which);stack.extend([(l,which),(which,r)])
 return [points[i] for i in sorted(keep)]

class Paths(osmium.SimpleHandler):
 def __init__(self):
  super().__init__();self.general=[];self.cerca=[];self.total=0;self.bad=0
 def way(self,w):
  k=w.tags.get('highway')
  if k not in KINDS:return
  pts=[]
  for node in w.nodes:
   if not node.location.valid():continue
   lon,lat=node.location.lon,node.location.lat
   if math.isfinite(lon) and math.isfinite(lat):pts.append((lon,lat))
  if len(pts)<2:return
  hits_general=any(in_box(x,y,REGION,.0005) for x,y in pts)
  if not hits_general:return
  hits_near=any(in_box(x,y,NEAR,.0001) for x,y in pts)
  name=str(w.tags.get('name') or '')[:60]
  kind=ALIASES.get(k,k)
  if hits_near:
   self.cerca.append([kind,name,[[round(x,6),round(y,6)] for x,y in simple(pts,.000014)]])
  if kind in {'path','track','footway','steps','pedestrian','service'}:
   if not any(any(abs(x-hx)<.013 and abs(y-hy)<.013 for hx,hy in TRAIL_NEAR) for x,y in pts):return
  self.general.append([kind,name,[[round(x,5),round(y,5)] for x,y in simple(pts,.000065)]])
  self.total+=1

def main():
 file=os.environ.get('OSM_FILE')
 if file and Path(file).is_file():path=Path(file)
 else:
  path=P/'canary-islands-latest.osm.pbf'
  print('Descargando datos abiertos de OpenStreetMap desde Geofabrik (aprox. 60 MB)...',flush=True)
  req=Request(URL,headers={'User-Agent':'GranCanariaOfflineGuide/1.0 (GitHub Pages, personal trip planning)'})
  with urlopen(req,timeout=160) as response,open(path,'wb') as f:
   while True:
    chunk=response.read(2*1024*1024)
    if not chunk:break
    f.write(chunk)
    if f.tell()%(20*1024*1024)<2*1024*1024:print(f'  descargados {f.tell()/1e6:.1f} MB',flush=True)
 print('Leyendo caminos y carreteras reales...',flush=True)
 h=Paths();h.apply_file(str(path),locations=True)
 assert h.general and h.cerca,'No se encontraron calles; fallo del extracto.'
 content={'generated':True,'source':'© OpenStreetMap contributors · Geofabrik / ODbL','general':h.general,'cerca':h.cerca}
 (P/'roads.js').write_text('window.GC_ROADS='+json.dumps(content,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf8')
 print(f'Callejero listo: general={len(h.general)} trazados, cercano={len(h.cerca)} trazados, bytes={(P/"roads.js").stat().st_size/1e6:.2f} MB')
 if not file and path.exists():path.unlink()

if __name__=='__main__':main()
