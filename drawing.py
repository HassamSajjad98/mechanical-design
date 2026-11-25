from pathlib import Path
import math
P=Path(__file__).parent
# orthographic diagram, actual nominal geometry with shroud omitted in front view
s=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="650" viewBox="0 0 1000 650"><rect width="1000" height="650" fill="white"/><g font-family="Arial" fill="#142d50"><text x="35" y="38" font-size="24" font-weight="bold">CF-560 | Concept impeller — general arrangement</text><text x="35" y="65" font-size="14">Dimensions in mm • Not for manufacture • Front shroud omitted in front view for clarity</text>']
cx,cy,k=310,345,.78
for r in [280,180,45,20]:s.append(f'<circle cx="{cx}" cy="{cy}" r="{r*k}" fill="none" stroke="#476681" stroke-width="1.4" {"stroke-dasharray=\"5 4\"" if r==180 else ""}/>')
for i in range(10):
 pts=[]
 for j in range(61):
  r=180+100*j/60;a=2*math.pi*i/10-math.log(r/180)/math.tan(math.radians(35));pts.append(f'{cx+k*r*math.cos(a):.2f},{cy-k*r*math.sin(a):.2f}')
 s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#217d98" stroke-width="3"/>')
s.append('<g stroke="#142d50" fill="none" stroke-width="1"><path d="M92 345H528 M92 336v18 M528 336v18"/><path d="M310 103v484" stroke-dasharray="6 5"/><path d="M82 345H538" stroke-dasharray="6 5"/></g><rect x="267" y="332" width="86" height="22" fill="white"/><text x="275" y="348" font-size="15">Ø560</text><text x="95" y="600" font-size="14">10 × curved blades, 3 mm nominal thickness</text><text x="95" y="620" font-size="14">Inlet Ø360; bore Ø40; hub Ø90</text>')
# axial section, schematic scale same
x=720;y=345
for xx,ww,hh in [(x,5*.78,560*.78),(x+125*.78,3*.78,560*.78)]:
 if xx==x:s.append(f'<rect x="{xx}" y="{y-hh/2}" width="{ww}" height="{hh}" fill="#8196a8"/>')
 else:
  for yy in [y-280*.78,y+180*.78]:s.append(f'<rect x="{xx}" y="{yy}" width="{ww}" height="78" fill="#8196a8"/>')
s.append(f'<rect x="{x-35*.78}" y="{y-45*.78}" width="{35*.78}" height="{90*.78}" fill="#8196a8"/><path d="M{x+4} {y-218} H{x+97} M{x+4} {y+218} H{x+97}" stroke="#217d98" stroke-width="3"/><path d="M{x-45} {y} H{x+130}" stroke="#142d50" stroke-dasharray="6 5"/><path d="M{x+4} 110H{x+97} M{x+4} 102v16 M{x+97} 102v16" stroke="#142d50"/><text x="{x+30}" y="100" font-size="14">120</text><text x="665" y="600" font-size="14">Axial envelope: 163 mm incl. hub</text><text x="665" y="620" font-size="14">Backplate 5 mm; shroud 3 mm</text></g></svg>')
(P/'drawing.svg').write_text(''.join(s))
