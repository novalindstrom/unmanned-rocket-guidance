from scipy.integrate import solve_ivp 
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import scipy
import scipy.integrate as sp_int
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def f(t, y):
    yprim = np.exp(t*np.sin(y))
    return [yprim]

y0 = [0] #representeras som lista
tspan = (0, 3) #kommatecken

sol = solve_ivp(f, tspan, y0, method = 'RK45' )

