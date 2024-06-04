import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import integrate
import unittest

def Plot(radius: float):
    theta = np.linspace(0, 2*np.pi, 100)
    phi = np.linspace(0, np.pi, 100)

    theta, phi = np.meshgrid(theta, phi)

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    fig = plt.figure()
    axis = fig.add_subplot(projection = '3d')

    axis.plot_surface(x,y,z, color='r', alpha=0.6)

    axis.set_xlabel('X')
    axis.set_xlabel('Y')
    axis.set_xlabel('Z')
    print('in')
    
    plt.show()
    

def Volume_from_Radius(radius: float) -> float:
    V = 0

    if radius <= 0:
        return V

    f = lambda rho , theta, phi, : rho**2 * np.sin(theta) 

    V = integrate.tplquad(f, 0, 2*np.pi, 0, np.pi, 0, radius) 
    
    Plot(radius)

    V = integrate.tplquad(f, 0, 2*np.pi, 0, np.pi, 0, radius)

    return round(V[0],2)

class TestVolume_from_Radius(unittest.TestCase):
    def runTest(self):
        V1 = Volume_from_Radius(2)
        self.assertEqual(V1, 33.51, "Incorrect Volume")

        V2 = Volume_from_Radius(5)
        self.assertEqual(V2, 523.60, "Incorrect Volume")

        V_Wrong = Volume_from_Radius(-1)
        self.assertEqual(V_Wrong, 0, "Cannot Calculate Radius < 0")

unittest.main()