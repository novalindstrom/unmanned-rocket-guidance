# This file will contain functions that do all calculations and logic - without simulations
import numpy as np
import matplotlib.pyplot as plt

# -------------- Constants ---------------------
# funktion av t och anger riktning och
# fart av bränslet som skjuts ut från raketen. Vi kan anta att ¯u(t) är en känd
# funktion som piloten (du) kan använda för att styra raketen i en önskad bana.
k = 700 # m/s som kraft
c = 0.05 # kg/m
g = 9.81 # gravitation
motortid = 10
g = 9.82 #gravitation
sträcka = 0 #tom variabel just nu

# ------------ Helper - functions -------------
def m(t): # motorn på 10 secunder förbränning, while eller bara en tillbaka?
    if t <= 10:
        return 8 - 0.4*(t), -0.4   #retunerar massan just nu vid detta tidssteg + derivatan

    return 4, 0 #retunerar massan när 10s har gått, då är förändringshastighet 0

def uvec(t, y):
    y_pos = y[1]
    u = np.zeros(2)
    u[0] = k * np.cos(rocket_moves(y_pos))
    u[1] = k * np.sin(rocket_moves(y_pos))
    return u


def um(t, y): #hastighetsvektor
    x_pos, y_pos, vx, vy = y
    return np.sqrt(vx** 2 + vy**2)


#-------------- Get steering angle --------------
def get_angle(t, y):
    x_pos, y_pos, vx, vy = y 

def rocket_moves(y_pos):
    if y_pos < 20:
        angle = np.pi / 2
    else:
        #angle = np.pi / 34 # Change later
        angle = np.pi / 12

    return angle

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

