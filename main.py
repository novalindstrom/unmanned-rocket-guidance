# This file will import the "physics-file" and 
# run the actuall simulation -> plotting the graph
import rocket_physics.py
import numpy as np
import matplotlib.pyplot as plt

# -------------- Numeric solver -----------------
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

# -------------- Pyhon solver --------------
h = 0.1
t = np.arange(0, 10 + h, h)
v0 = [0, 0, 0, 0]

t, y = RK4_model(rocket_ODE, h, t, v0)

plt.scatter([80], [60], color='red', s=70, label="Mål (80, 60)")
plt.title("Simulering av raketens bana", fontsize=14)
plt.xlabel("")
plt.ylabel("höjd (m)")
plt.xlim(0, 700)
plt.ylim(0, 200)
plt.legend()
plt.grid(True)
plt.plot(y[:, 0], y[:, 1], "-b", label="Raketens bana")
plt.show()
