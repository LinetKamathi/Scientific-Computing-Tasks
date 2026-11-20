# REAL-WORLD CASE: Electrical circuit analysis (Kirchhoff's mesh-current law)
# Assumptions: two loops share a 4-ohm resistor. Loop 1 has a 12 V source and
# 6 + 4 ohm resistors; loop 2 has a 6 V source and 5 + 4 ohm resistors.
#   10*I1 - 4*I2 = 12
#   -4*I1 + 9*I2 = 6
import numpy as np

A = np.array([[10.0, -4.0], [-4.0, 9.0]])
b = np.array([12.0, 6.0])

I = np.linalg.solve(A, b)
print(f"Loop current I1 = {I[0]:.4f} A")
print(f"Loop current I2 = {I[1]:.4f} A")
print(f"Current through shared resistor = {I[0]-I[1]:.4f} A")
print(f"Power in shared 4-ohm resistor = {4*(I[0]-I[1])**2:.4f} W")
print("Residual norm:", np.linalg.norm(b - A @ I))
