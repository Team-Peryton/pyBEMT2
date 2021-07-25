 # -*- coding: utf-8 -*-

import matplotlib.pyplot as pl
import pandas as pd
from math import pi

from pybemt.solver import Solver
from pybemt.config import Config

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

df, sections = s.run_sweep('v_inf', 20, 1, 44.0)

df_exp = pd.read_csv("./examples/propeller_data.csv", delimiter=' ')

ax = df.plot(x='J', y='eta', legend=None) 
df_exp.plot(x='J',y='eta',style='C0o',ax=ax, legend=None)
pl.legend(('BEMT, $\eta$','Exp, $\eta$'),loc='center left')

pl.ylabel('$\eta$')
ax2 = ax.twinx()
pl.ylabel('$C_P, C_T$')

df.plot(x='J', y='CP', style='C1-',ax=ax2, legend=None) 
df_exp.plot(x='J',y='CP',style='C1o',ax=ax2, legend=None)

df.plot(x='J', y='CT', style='C2-',ax=ax2, legend=None) 
df_exp.plot(x='J',y='CT',style='C2o',ax=ax2, legend=None)


pl.legend(('BEMT, $C_P$','Exp, $C_P$',
    'BEMT, $C_T$','Exp, $C_T$'),loc='center right')

pl.show()

