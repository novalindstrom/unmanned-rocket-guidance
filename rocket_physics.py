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
Ang0 = (np.pi)/2 #startvinkel som ej får ändras innan 20m

# ----------TODO: ta bort?? --------------------
motortid = 10
bransletank = 1 #behövs en sådan?


# ------------ Helper - functions --------------
#retunerar massan beroende på förbränt bränsle
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


#-------------- Get steering angle -------------
def rocket_moves(y_pos):
    if y_pos < 20:
        angle = np.pi / 2
    else:
        #angle = np.pi / 34 # Change later
        angle = 0.4636

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
h = 0.01
t = np.arange(0, 20 + h, h)
v0 = [0.0, 0.0, 0.0, 0.0]

t, y = RK4_model(rocket_ODE, h, t, v0)

plt.scatter([80], [60], color='red', s=70, label="Mål (80, 60)")
plt.title("Simulering av raketens bana", fontsize=14)
plt.xlabel("")
plt.ylabel("höjd (m)")
plt.xlim(0, 100)
plt.ylim(0, 80)
plt.legend()
plt.grid(True)
plt.plot(y[:, 0], y[:, 1], "-b", label="Raketens bana")
plt.show()
