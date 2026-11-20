# REAL-WORLD CASE: Structural analysis of a 3-storey building (spring-mass model)
# Assumptions: stiffness matrix K (kN/mm) is fixed; wind-load vectors (kN) vary by day.
# K u = F gives floor displacements u (mm). K is factorised once and reused.
import numpy as np
from scipy.linalg import lu_factor, lu_solve

K = np.array([[ 30.0, -10.0,   0.0],
              [-10.0,  20.0, -10.0],
              [  0.0, -10.0,  10.0]])

loads = {"Calm day": [1.0, 1.0, 1.0],
         "Windy day": [5.0, 8.0, 12.0],
         "Storm": [15.0, 25.0, 40.0]}

lu, piv = lu_factor(K)
for name, F in loads.items():
    u = lu_solve((lu, piv), np.array(F))
    print(f"{name:10s} displacements (mm): {np.round(u, 3)}  | max = {u.max():.3f} mm")
    print(f"{'':10s} residual norm = {np.linalg.norm(np.array(F) - K @ u):.2e}")
