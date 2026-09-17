# This file will contain functions that do all calculations and logic - without simulations
import numpy as np

# ------------ Constants ---------------------
k = 700 #m/s som kraft
#     funktion av t och anger riktning och
#   fart av bränslet som skjuts ut från raketen. Vi kan anta att ¯u(t) är en känd
#   funktion som piloten (du) kan använda för att styra raketen i en önskad bana.

R0 = [0,0] #startposition
v0 = [0,0]
c = 0.05 #kg/m
Ang0 = (np.pi)/2 #startvinkel som ej får ändras innan 20m
g = 9.18 # gravitation
motortid = 10

bransletank = 1 #behövs en sådan?

tspan = [0, 10]

# ------------ Helper - functions ------------
# Kolla på de funktioner som ges i instruktionen??

#retunerar massan beroende på förbränt bränsle
def m(t): # motorn på 10 secunder förbränning, while eller bara en tillbaka?
    if t in tspan:
        return 8 - 0.4*(t), -0.4   #retunerar massan just nu vid detta tidssteg + derivatan

    return 4 , 0 #retunerar massan när 10s har gått, då är förändringshastighet 0

def uvec(t):
    u=np.zeros(2)
    u[0] = k * np.cos(rocket_moves(y_pos))
    u[1] = k * np.sin(rocket_moves(y_pos))
    return u


# hastigheten = v
# rocket_der = [x(t), y(t), Vx(t), Yx(t)]
def F(t):
    return m(t) * g - c * ((v(t))**2)


def um(t): #hastighetsvektor
    return


#------------- Get steering angle -------------

def rocket_moves(y_pos):
    if y_pos < 20:
        angle = np.pi / 2
    else:
        angle = np.pi / 4 # Change later

    return angle



# ------------ Numeric solver ----------------
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