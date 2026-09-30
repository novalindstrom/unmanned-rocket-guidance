# This file contains functions that do all calculations and logic
import numpy as np
import matplotlib.pyplot as plt

# -------------- Constants ---------------------

#k is the constant speed from the engine written in m/s
k = 700 # m/s som kraft

#c is a constant for air resistance written in kg/m
c = 0.05

#g is the constant force from gravitation written in m/(s^2)
g = 9.82

#the starting angle that will be changed
# depending on how close to target simulation is, with a starting foo-number
curr_angle = 0 

# ------------ Helper - functions -------------
def m(t): 
    """
    Calculates the mass of the rocket.

    Parameters
    ----------
    t : float
        time in certain moment
        
    Returns
    -------
    tuple (float, float)
        A tuple containing the mass for the rocket in time t, and the derivate. 
    """
    if t <= 10:
        return 8 - 0.4*(t), -0.4  

    return 4, 0 



def rocket_moves(y_pos):
    """
    Decides the steering angle of the rocket, if the rocket is beneath 20m,
    the angle will be pi/2
    
    Parameters
    ----------
    y_pos : float
       The rockets height coordinate in meters
        
    Returns
    -------
    float
        The steering angle in radians. 
    """
    if y_pos < 20:
        return np.pi / 2
    else: 
        return curr_angle 

def uvec(y):
    """
    Calculates vector for the speed of the fuel with constants. 

    Parameters
    ----------
    y : array
        The state vector
    Returns
    -------
    array 
        The vector for the speed of the fuel in meters/second. 
    """
    y_pos = y[1]
    u = np.zeros(2)
    u[0] = k * np.cos(rocket_moves(y_pos))
    u[1] = k * np.sin(rocket_moves(y_pos))
    return u

def um(t, y):
    """
    Calculates vector for air resistance. 

    Parameters
    ----------
    y : array
        The state vector
    t : float
        The current time in seconds
        
    Returns
    -------
    float
        The vector for the speed of the fuel in meters/second. 
    """
    x_pos, y_pos, vx, vy = y 
    return np.sqrt(vx** 2 + vy**2)

#------------------ Rocket ODE ------------------
def rocket_ODE(t, y):
    """
    The differential equation. 

    Parameters
    ----------
    t : float
        The current time in seconds (s).
    y : array
        The state vector.
        
    Returns
    -------
    Array
        The derivatives of the state vector 
    """
    x_pos, y_pos, vx, vy = y 
    m_val, m_der = m(t)

    u = uvec(y)
    v_t = um(t, y)

    der = np.zeros(4)
    der[0] = vx
    der[1] = vy

    der[2] = (-c * v_t * vx)/m_val - (m_der/m_val) * u[0]
    der[3] = -g + (-c * v_t * vy)/m_val - (m_der/m_val) * u[1]

    return der 

