"""Preliminary sizing and scenario economics; all inputs are assumptions."""
import math,json
from pathlib import Path
Q=2; dp=1000; rpm=1450; D=.56; b=.12; rho=1.2; blockage=.9; eta=.72; ref=.60; motor_eta=.9; hours=6000; price=.18; ef=.05
u=math.pi*D*rpm/60
shaft=Q*dp/eta; refshaft=Q*dp/ref
m=dict(air_power_kw=Q*dp/1000,tip_speed_m_s=u,pressure_coefficient=dp/(rho*u*u),exit_velocity_m_s=Q/(math.pi*D*b*blockage),shaft_power_kw=shaft/1000,torque_nm=shaft/(rpm*2*math.pi/60),motor_required_kw=shaft*1.2/1000,reference_kwh=refshaft/motor_eta*hours/1000,proposed_kwh=shaft/motor_eta*hours/1000)
m['saved_kwh']=m['reference_kwh']-m['proposed_kwh'];m['saved_eur']=m['saved_kwh']*price;m['saved_kgco2e']=m['saved_kwh']*ef
if __name__=='__main__':
 print(json.dumps(m,indent=2));Path(__file__).with_name('metrics.json').write_text(json.dumps(m,indent=2))
