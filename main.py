# This file will import the "physics-file" and run the actuall simulation -> plotting the graph
import rocket_physics
import numpy as np
import matplotlib.pyplot as plt

# Using solve_ivp (to compare with our solver?)
# sol = solve_ivp(f, tspan, y0, method = 'RK45')
# t, y = RK4_model(ODE, h, tspan, y0, --params??--)

# Finding correct angle function?


endPoint = (60, 80)
plt.plot(endPoint, 'r')
plt.show()