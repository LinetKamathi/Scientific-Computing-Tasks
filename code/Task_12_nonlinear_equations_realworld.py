# REAL-WORLD CASE: Wi-Fi coverage along a road
# Assumptions: a router at the origin covers a circle of radius 50 m. A straight road
# follows y = 0.5x + 10. Find where the road enters and leaves the coverage area.
import numpy as np
from scipy.optimize import root

def equations(z):
    x, y = z
    return [x**2 + y**2 - 50**2,      # coverage boundary
            y - (0.5*x + 10)]         # road

for guess in ([40.0, 30.0], [-50.0, -15.0]):
    sol = root(equations, guess)
    x, y = sol.x
    print(f"Initial guess {guess} -> point ({x:.3f}, {y:.3f}) m, converged={sol.success}")
    print(f"   residuals: {np.round(equations(sol.x), 10)}")

p1, p2 = root(equations, [40, 30]).x, root(equations, [-50, -15]).x
print(f"Road length inside coverage: {np.linalg.norm(p1 - p2):.2f} m")
