# REAL-WORLD CASE: Logistic growth of a fish population in a pond
# dP/dt = r*P*(1 - P/K), r = 0.4 per month, carrying capacity K = 1000, P(0) = 50.
import numpy as np
import matplotlib.pyplot as plt

r, K, P0 = 0.4, 1000.0, 50.0

def euler(h, end=24.0):
    t = np.arange(0, end + h, h)
    P = np.zeros_like(t); P[0] = P0
    for i in range(len(t) - 1):
        P[i+1] = P[i] + h * r * P[i] * (1 - P[i] / K)
    return t, P

exact = lambda t: K / (1 + (K/P0 - 1) * np.exp(-r * t))

for h in (2.0, 1.0, 0.25):
    t, P = euler(h)
    print(f"h={h:<5} Euler P(24)={P[-1]:8.2f}  exact={exact(24):8.2f}  error={abs(P[-1]-exact(24)):.3f}")

tt = np.linspace(0, 24, 200)
plt.plot(tt, exact(tt), label="Exact")
for h in (2.0, 1.0):
    t, P = euler(h); plt.plot(t, P, "o-", ms=3, label=f"Euler h={h}")
plt.xlabel("Time (months)"); plt.ylabel("Fish population"); plt.title("Logistic growth")
plt.legend(); plt.grid(True); plt.show()
