import numpy as np
from scipy import integrate
import unittest

def Volume_from_Radius(radius: float) -> float:
    V = 0

    if radius <= 0:
        return V

    f = lambda rho , theta, phi, : rho**2 * np.sin(theta) 

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



 
# run the test
unittest.main()

