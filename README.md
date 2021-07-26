# pyBEMT2

To see the orignal repository and docs please see https://github.com/kegiljarhus/pyBEMT

I haven't found a good programmatic tool for propeller analysis, so I'm modifying this one. The aim is to be able to evaulate propeller selection tradeoffs for UAVs quickly.

Other tools I have found:
- https://github.com/old-NWTC/AeroDyn replaced by openFAST
- https://github.com/OpenFAST/openfast
- http://www.q-blade.org/ based on XFLR5
- https://sites.google.com/site/joaomorgado23/Home based on QBlade
- https://www.mh-aerotools.de/airfoils/javaprop.htm 

Propeller data:
- https://m-selig.ae.illinois.edu/props/propDB.html
- T motor website contains a lot of static testing
- https://www.apcprop.com/technical-information/performance-data/ contains simulation data - my initial findings have shown this to be pretty off, especially in power estimation
- https://database.rcbenchmark.com

Changes:
- Propeller geometry input is now done through a python dataclass instead of through an input file. This enables programmatic batch analysis. 

Planned:
- More experimental validation
- Visualisation tools
  - 2d / 3d variable plotting
  - propeller geometry plot
- Fix tests to new formats


See examples/run_propeller.py

```python
config = Config(
    rpm = 1100.0,
    v_inf = 1.0,
    n_blades = 3,
    diameter = 3.054,
    radius_hub = 0.375,
    section= ["CLARKY", "CLARKY", "CLARKY", "CLARKY", "CLARKY", "CLARKY", "CLARKY", "CLARKY"],
    radius = [0.375, 0.525, 0.675, 0.825, 0.975, 1.125, 1.275, 1.425],
    chord = [0.18, 0.18, 0.225, 0.225, 0.21, 0.1875, 0.1425, 0.12],
    pitch = [17, 17, 17, 17, 17, 17, 17, 17]
)

s = Solver(config)
```