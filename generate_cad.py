"""Conceptual impeller geometry in mm. Requires cadquery. No structural validation."""
import cadquery as cq
import math, csv
from pathlib import Path
P=Path(__file__).parent
R=280; r0=180; width=120; thickness=3; beta=math.radians(35); count=10
# Log spiral, trailing relative to CCW rotation. Constant approximate normal thickness.
def blade_points():
    sides=[[],[]]
    for i in range(61):
        r=r0+(R-r0)*i/60
        a=-math.log(r/r0)/math.tan(beta)
        x,y=r*math.cos(a),r*math.sin(a)
        # normal to outward tangent sin(beta)*er-cos(beta)*etheta
        nx=math.cos(beta)*math.cos(a)-math.sin(beta)*math.sin(a)
        ny=math.cos(beta)*math.sin(a)+math.sin(beta)*math.cos(a)
        for j,sign in enumerate([1,-1]): sides[j].append((x+sign*thickness/2*nx,y+sign*thickness/2*ny))
    return sides[0]+sides[1][::-1]
back=cq.Workplane('XY').circle(R).circle(20).extrude(5)
front=cq.Workplane('XY').workplane(offset=125).circle(R).circle(r0).extrude(3)
hub=cq.Workplane('XY').workplane(offset=-35).circle(45).circle(20).extrude(35)
blade=cq.Workplane('XY').workplane(offset=5).polyline(blade_points()).close().extrude(width)
# Trim outer edge to nominal envelope
blade=blade.intersect(cq.Workplane('XY').workplane(offset=5).circle(R).extrude(width))
parts=[('backplate',back,1),('front_shroud',front,1),('hub',hub,1),('blade',blade,count)]
assy=cq.Assembly(name='concept_impeller')
solids=[]
for name,obj,qty in parts:
    assert obj.val().isValid(),name
    cq.exporters.export(obj,str(P/(name+'.step')))
    for i in range(qty):
        piece=obj.rotate((0,0,0),(0,0,1),i*360/qty) if qty>1 else obj
        assy.add(piece,name=f'{name}_{i+1}',color=cq.Color(0.28,0.48,0.65) if name=='blade' else cq.Color(0.65,0.70,0.74))
        solids.append(piece.val())
assy.save(str(P/'impeller.step'))
compound=cq.Compound.makeCompound(solids)
cq.exporters.export(compound,str(P/'impeller.stl'),tolerance=0.2,angularTolerance=0.15)
with open(P/'bom.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['component','quantity','material_candidate','unit_mass_kg','total_mass_kg'])
    for name,obj,qty in parts:
        mass=obj.val().Volume()*7.85e-6;w.writerow([name,qty,'S235 mild steel',round(mass,3),round(mass*qty,3)])
print('CAD valid, solids:',len(solids),'mass kg:',sum(s.Volume()*7.85e-6 for s in solids))
