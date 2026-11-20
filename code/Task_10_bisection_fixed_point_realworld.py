# REAL-WORLD CASE: Break-even point of a small business
# Assumptions: a bakery sells loaves at KES 50. Costs = 2000 fixed + 20 per loaf
# + 0.02*q^2 (overtime cost rises with volume). Break-even where profit = 0.
import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def profit(q):
    return 50*q - (2000 + 20*q + 0.02*q**2)

sol = root_scalar(profit, bracket=[0, 200], method="bisect", xtol=1e-10)

# Fixed-point form: q = (2000 + 20q + 0.02q^2)/50
g = lambda q: (2000 + 20*q + 0.02*q**2) / 50
q = 100.0; hist = [q]
for _ in range(200):
    q_new = g(q); hist.append(q_new)
    if abs(q_new - q) < 1e-10: break
    q = q_new

print(f"Bisection break-even quantity: {sol.root:.4f} loaves ({sol.iterations} iterations)")
print(f"Fixed-point break-even quantity: {hist[-1]:.4f} loaves ({len(hist)-1} iterations)")

qs = np.linspace(0, 200, 300)
plt.plot(qs, profit(qs)); plt.axhline(0, lw=0.8); plt.axvline(sol.root, ls="--")
plt.xlabel("Loaves sold per day"); plt.ylabel("Profit (KES)")
plt.title("Break-even analysis"); plt.grid(True); plt.show()
