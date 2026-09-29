# This file will contain functions that do all calculations and logic - without simulations
import numpy as np
import matplotlib.pyplot as plt

# -------------- Constants ---------------------

k = 700 # m/s som kraft
c = 0.05 # kg/m
g = 9.82 #gravitation
curr_angle = 0 #nuvarande vinkeln
# ------------ Helper - functions -------------

def m(t): 
    if t <= 10:
        return 8 - 0.4*(t), -0.4  

    return 4, 0 


# Bestämmer raketens styrvinkel i radianer utifrån dess höjd y. 
# Så länge raketen befinner sig under 20 meters höjd returneras np.pi / 2
def rocket_moves(y_pos):
    if y_pos < 20:
        return np.pi / 2
    else: 
        return curr_angle 

def uvec(t, y):
    y_pos = y[1]
    u = np.zeros(2)
    u[0] = k * np.cos(rocket_moves(y_pos))
    u[1] = k * np.sin(rocket_moves(y_pos))
    return u

def um(t, y):
    x_pos, y_pos, vx, vy = y # hämta tillståndsvektor
    return np.sqrt(vx** 2 + vy**2)

#------------------ Rocket ODE ------------------
def rocket_ODE(t, y):
    x_pos, y_pos, vx, vy = y # hämta tillståndsvektorn
    m_val, m_der = m(t)

    u = uvec(t, y)
    v_t = um(t, y)

    der = np.zeros(4)
    der[0] = vx
    der[1] = vy

    der[2] = (-c * v_t * vx)/m_val - (m_der/m_val) * u[0]
    der[3] = -g + (-c * v_t * vy)/m_val - (m_der/m_val) * u[1]

    return der 

