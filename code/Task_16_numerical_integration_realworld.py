# REAL-WORLD CASE: Water volume carried by a river
# Assumptions: flow rate (m^3/s) measured every hour for 8 hours. Volume = integral of flow dt.
import numpy as np
from scipy.integrate import simpson

hours = np.arange(0, 9, dtype=float)
flow = np.array([20, 24, 32, 45, 58, 50, 38, 28, 22], dtype=float)   # m^3/s
seconds = hours * 3600

vol_trap = np.trapezoid(flow, seconds)
vol_simp = simpson(flow, x=seconds)
print(f"Volume (trapezoid): {vol_trap/1e6:.4f} million m^3")
print(f"Volume (Simpson):   {vol_simp/1e6:.4f} million m^3")
print(f"Difference: {abs(vol_trap - vol_simp):,.0f} m^3")
print(f"Average flow rate: {vol_simp/seconds[-1]:.2f} m^3/s")
