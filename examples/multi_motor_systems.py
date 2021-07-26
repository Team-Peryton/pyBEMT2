 # -*- coding: utf-8 -*-

import matplotlib.pyplot as pl
import pandas as pd
from math import pi
from scipy.interpolate import interp1d

from pybemt.solver import Solver
from pybemt.config import Config
from pybemt.analysis import tip_speed, max_rpm_from_tip_speed

radius_range = [0.1,0.15,0.2,0.25,0.3,0.35]

thrust = 30

power_required = []
power_required2 = []
power_required3 = []

for radius in radius_range:

    config = Config(
        rpm=2200.0,
        v_inf=15,
        diameter=0.7112,
        radius_hub=0.03,
        section=["NACA_4412", "GOE_450", "GOE_450", "GOE_450", "GOE_450", "GOE_450", "GOE_408", "GOE_408"],
        radius=[0.07112, 0.10668, 0.14224, 0.1778, 0.21336, 0.24892, 0.28448, 0.32004],
        chord=[0.056, 0.07, 0.07, 0.065, 0.058, 0.05, 0.043, 0.034],
        pitch=[19.6, 17.9, 14.4, 11.6, 9.7, 8.4, 7.2, 6.7]
    )

    config.radius = [r/0.3556*radius for r in config.radius]
    config.chord = [c/0.3556*radius for c in config.chord]
    config.diameter = radius*2
    config.radius_hub = 0.03/0.3556 * radius
    config.rpm = max_rpm_from_tip_speed(radius*2)/2
    #config.pitch = [p/0.7112*diameter for p in config.pitch]

    s = Solver(config)

    # pitch = s.optimize_pitch()
    
    # config.pitch = pitch.x.tolist()

    # print(pitch)

    # s = Solver(config)

    df, sections = s.run_sweep('rpm', 20, 1000.0, max_rpm_from_tip_speed(radius*2))

    df["T/P"] = df["T"] / df["P"]

    if radius == 0.1:
        ax = df.plot(x='rpm', y='T/P')
        ax2 = df.plot(x='rpm', y='P')
    else:
        df.plot(x='rpm',y='T/P',ax=ax)
        df.plot(x='rpm',y='P',ax=ax2)

    # find the required power at the given thrust
    f = interp1d(df["T"], df["P"])
    try:
        power_required.append(f(thrust).tolist())
    except:
        power_required.append(0)
    
    try:
        power_required2.append(f(thrust/2).tolist()*2)
    except:
        power_required2.append(0)
    
    try:
        power_required3.append(f(thrust/3).tolist()*3)
    except:
        power_required3.append(0)



pl.figure(1)
pl.legend(radius_range)


# ax = df.plot(x='rpm', y='T') 
# ax2 = df.plot(x='rpm', y='P') 

# df_exp = pd.read_csv("./examples/tmotor28_data.csv", delimiter=';')

# # df_exp.plot(x='RPM',y='T(N)',style='o',ax=ax)
# pl.figure(1)
# pl.ylabel('Thrust (N)')
# pl.legend(('BEMT','Experiment'))
# # df_exp.plot(x='RPM',y='P(W)',style='o',ax=ax2)
# pl.figure(2)
# pl.ylabel('Power (W)')
# pl.legend(('BEMT','Experiment'))


pl.show()

