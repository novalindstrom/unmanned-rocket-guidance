# This file will contain functions that do all calculations and logic - without simulations
import numpy as np

# ------------ Helper - functions ------------
# Kolla på de funktioner som ges i instruktionen??


# ------------ Numeric solver ------------
def RK4_model(f, h, t, y0):
    y = np.zeros((len(t), len(y0)))
    y[0] = y0

    for i in range(len(t) - 1):
        ti = t[i]
        yi = y[i]
        
        k1 = f(ti, yi)
        k2 = f(ti + h/2, yi + (h/2) * k1)
        k3 = f(ti + h/2, yi + (h/2) * k2)
        k4 = f(ti + h, yi + h * k3)  
        y[i + 1] = yi + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

    return t, y

# Anropas typ : 
# t, y = RK4_model(ODE, steglängd, tspan, begynnelse villkoret)