# REAL-WORLD CASE: Acceleration of a train from speed readings, and step-size error
# Assumptions: speed (m/s) logged every 2 s. Acceleration = d(speed)/dt.
# Part 2 shows forward vs central difference error for f(x)=sin(x) at x=1.
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 21, 2, dtype=float)
v = np.array([0, 2.5, 5.4, 8.6, 12.0, 15.2, 18.0, 20.1, 21.5, 22.2, 22.5])
acc = np.gradient(v, t)       # central inside, one-sided at ends
for ti, vi, ai in zip(t, v, acc):
    print(f"t={ti:4.0f}s  speed={vi:5.1f} m/s  acceleration={ai:6.3f} m/s^2")

print("\nStep-size study for d/dx sin(x) at x=1 (true value cos(1) = %.8f)" % np.cos(1))
for h in (0.1, 0.01, 0.001):
    fwd = (np.sin(1 + h) - np.sin(1)) / h
    cen = (np.sin(1 + h) - np.sin(1 - h)) / (2 * h)
    print(f"h={h:<6} forward error={abs(fwd-np.cos(1)):.2e}  central error={abs(cen-np.cos(1)):.2e}")

plt.plot(t, acc, "o-"); plt.xlabel("Time (s)"); plt.ylabel("Acceleration (m/s^2)")
plt.title("Train acceleration from speed data"); plt.grid(True); plt.show()
