# Parametrization of a Sphere's Radius 

This program finds the volume of a sphere through the parametrization of regular cartesian coordiantes into the spherical coordinates with the radius. This is expressed through the following triple integral:

$$
\int_0^{2\pi}\int_0^\pi\int_0^\rho \rho^2\sin\theta\;\mathrm{d}\rho\mathrm{d}\theta\mathrm{d}\phi.
$$

This triple integral is implemented in the Volume_from_Radius function found within Implementation file. This function uses the tplquad function found in the scipy integrate package.

In addition when the program is run a three dimensional representation of the parameterized sphere is generated using the matplot library.