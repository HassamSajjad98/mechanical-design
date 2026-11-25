# CF-560 — Industrial centrifugal fan concept
Independent mechanical engineering portfolio case study. Concept only; not a manufactured, certified or tested fan.

## Requirements
2 m³/s (7200 m³/h), total pressure rise 1000 Pa, 1450 rpm, target total fan efficiency 72%, reference efficiency 60%, air density 1.2 kg/m³. Diameter 560 mm, inlet 360 mm, passage width 120 mm, ten 3 mm blades, 35° backward outlet angle. These are design assumptions, not experimentally derived dimensions. Pressure coefficient defined here as Δp/(ρU²); calculated 0.461, not a validated aerodynamic prediction. Exit blockage factor 0.9 assumed.

## Design and results
Air power QΔp = 2 kW; shaft power 2.778 kW; tip velocity 42.516 m/s; torque 18.294 Nm; radial exit velocity 10.526 m/s. Motor sizing at 20% margin 3.333 kW; candidate 4 kW motor. Blade geometry is a constant-angle logarithmic spiral with polygonal approximation, no aerodynamic optimisation claimed. CAD comprises 13 separate solids, checked for geometric validity; nominal mass 19.336 kg. No welds, fits, keyway, shaft, bearings, enclosure or guards are detailed. STEP is importable geometry, not native SolidWorks feature history. STL is a multi-part visualization mesh, not a print-ready fused model.

## Energy scenario
At equal duty, 90% assumed motor efficiency, 6000 h/year, electricity €0.18/kWh and illustrative 0.05 kg CO2e/kWh: reference 22222 kWh/year, target 18519 kWh/year, difference 3704 kWh/year (16.67%), €667/year and 185 kg CO2e/year. Not measured or guaranteed; carbon factor and tariff are scenario inputs, not official French values.

## Manufacturing concept
Laser cut backplate and shroud, cut and roll-form blade blanks using a jig, machine hub, tack and weld using a qualified procedure with controlled sequence, inspect geometry and welds, apply corrosion protection, dynamically balance and validate. Material candidate S235 subject to fatigue, weld and corrosion assessment. No tolerances, weld sizing or safety release specified.

## Validation gates
1. CFD: inlet and volute geometry, mesh convergence, flow/pressure curve, shaft power and efficiency; compare test data.
2. Structural FEA: centrifugal load, weld fatigue, stress concentration, modal/critical speed, overspeed case and mesh convergence.
3. Mechanical design: shaft, bearings, hub connection, housing/clearances, guarding and motor starting load.
4. Prototype: dimensional inspection, dynamic balance, vibration/noise and airflow/pressure/power testing under applicable AMCA/ASHRAE procedures. Establish safe operating envelope before manufacture or operation.

## Files and reproduction
Open index.html in a browser. Download impeller.step for CAD; individual STEP components also provided. drawing.svg is a concept general arrangement, not a production drawing. Python 3: `python analysis.py` regenerates metrics.json; `pip install cadquery` then `python generate_cad.py` regenerates CAD and BOM. `python drawing.py` regenerates the SVG. No browser libraries required.

## References
- ASHRAE Handbook, Fans: https://handbook.ashrae.org/Handbooks/S20/SI/S20_Ch21/s20_ch21_si.aspx
- ANSI/AMCA 210-25 / ANSI/ASHRAE 51-25: https://www.amca.org/assets/resources/public/pdf/Publications/amca-210-25-downloadable.pdf
These provide engineering and test context; no compliance is claimed.
