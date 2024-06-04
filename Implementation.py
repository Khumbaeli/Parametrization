import numpy as np
from scipy import integrate


def Volume_from_Radius(radius: float) -> float:
    V = 0

    f = lambda rho , theta, phi, : rho**2 * np.sin(theta) 

    V = integrate.tplquad(f, 0, 2*np.pi, 0, np.pi, 0, radius)

    return V

print(Volume_from_Radius(2))