 # -*- coding: utf-8 -*-

import matplotlib.pyplot as pl
import pandas as pd
from math import pi

from pybemt.solver import Solver
from pybemt.config import Config

config = Config(
    rpm=2200.0,
    v_inf=0,
    diameter=0.7112,
    radius_hub=0.03,
    section=["NACA_4412", "GOE_450", "GOE_450", "GOE_450", "GOE_450", "GOE_450", "GOE_408", "GOE_408"],
    radius=[0.07112, 0.10668, 0.14224, 0.1778, 0.21336, 0.24892, 0.28448, 0.32004],
    chord=[0.056, 0.07, 0.07, 0.065, 0.058, 0.05, 0.043, 0.034],
    pitch=[19.6, 17.9, 14.4, 11.6, 9.7, 8.4, 7.2, 6.7]
)

s = Solver(config)

df, sections = s.run_sweep('rpm', 20, 1000.0, 3200.0)

ax = df.plot(x='rpm', y='T') 
ax2 = df.plot(x='rpm', y='P') 

df_exp = pd.read_csv("./examples/tmotor28_data.csv", delimiter=';')

df_exp.plot(x='RPM',y='T(N)',style='o',ax=ax)
pl.figure(1)
pl.ylabel('Thrust (N)')
pl.legend(('BEMT','Experiment'))
df_exp.plot(x='RPM',y='P(W)',style='o',ax=ax2)
pl.figure(2)
pl.ylabel('Power (W)')
pl.legend(('BEMT','Experiment'))


pl.show()

