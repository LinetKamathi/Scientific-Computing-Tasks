# REAL-WORLD CASE: Reservoir water level
# Assumptions: level (m) is measured every 3 hours; the control room needs hourly estimates.
import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

t = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24], dtype=float)
level = np.array([12.0, 11.6, 11.9, 12.8, 13.9, 14.4, 14.0, 13.1, 12.5])

lin = interp1d(t, level)
cub = CubicSpline(t, level)
hourly = np.arange(0, 25)

for h in (4, 10, 16):
    print(f"t={h:2d} h  linear={float(lin(h)):.3f} m  cubic={float(cub(h)):.3f} m")

plt.scatter(t, level, label="3-hourly measurements", zorder=3)
plt.plot(hourly, lin(hourly), "--", label="Linear")
plt.plot(np.linspace(0, 24, 200), cub(np.linspace(0, 24, 200)), label="Cubic spline")
plt.xlabel("Hour"); plt.ylabel("Water level (m)"); plt.title("Reservoir level interpolation")
plt.legend(); plt.grid(True); plt.show()
