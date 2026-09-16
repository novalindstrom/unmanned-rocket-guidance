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

#---------Skal av idé till raketens riktning

def rocket_moves(t, y):
    yder = np.zeros(4)
    x_position = y[0] # X positionen för var tidssteg
    y_position = y[1] # Y postitionen dvs höjden för var tidssteg
    x_hastighet = y[2] # derivatan av y är hastigheten
    y_hastighet = y[3]

    height = y_position # då det är y positionen i varje tidssteg i vår RK modell

    if height < 20:
        rocket_angle = np.pi / 2
    else:
        # rocket_angle = 
                # här skulle vi kunna räkna ut vinkeln från nyvarande plats till målet med arctan maybe
                # eller testa en konstant vinkel
   
   # sedan kolla hur mycket bränsle vi har 