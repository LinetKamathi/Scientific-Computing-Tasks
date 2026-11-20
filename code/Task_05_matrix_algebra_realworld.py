# REAL-WORLD CASE: Mapping a rectangular farm plot with a drone
# Assumptions: plot corners in metres. The drone image is rotated by 30 degrees and
# scaled by 1.2 (east-west) and 0.8 (north-south) to match a map projection.
import numpy as np
import matplotlib.pyplot as plt

plot = np.array([[0, 0], [100, 0], [100, 60], [0, 60]], dtype=float)
theta = np.deg2rad(30)
rotation = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
scale = np.diag([1.2, 0.8])
T = rotation @ scale

mapped = plot @ T.T
print("Mapped corners:\n", np.round(mapped, 2))
print("Determinant of T:", round(np.linalg.det(T), 4))

area_before = 100 * 60
area_after = area_before * abs(np.linalg.det(T))
print(f"Area before: {area_before} m^2, after transformation: {area_after:.1f} m^2")

closed = lambda p: np.vstack([p, p[0]])
plt.plot(*closed(plot).T, label="Original plot")
plt.plot(*closed(mapped).T, label="Transformed plot")
plt.axis("equal"); plt.grid(True); plt.legend()
plt.xlabel("x (m)"); plt.ylabel("y (m)"); plt.title("Farm plot transformation")
plt.show()
