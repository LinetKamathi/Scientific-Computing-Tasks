# REAL-WORLD CASE: Growth of a mobile-app user base (exponential model)
# Assumptions: monthly active users (thousands) over 8 months; model y = a*exp(b*t).
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

months = np.arange(1, 9, dtype=float)
users_k = np.array([10.2, 12.1, 14.8, 17.5, 21.4, 25.9, 31.6, 38.0])

def model(t, a, b):
    return a * np.exp(b * t)

(a, b), cov = curve_fit(model, months, users_k, p0=[8, 0.2])
pred = model(months, a, b)
rmse = np.sqrt(np.mean((users_k - pred)**2))

print(f"Fitted model: users = {a:.3f} * exp({b:.4f} * month)")
print(f"Monthly growth rate: {np.exp(b) - 1:.2%}")
print(f"RMSE: {rmse:.3f} thousand users")
print(f"Forecast month 12: {model(12, a, b):.1f} thousand users")

tt = np.linspace(1, 12, 200)
plt.scatter(months, users_k, label="Observed")
plt.plot(tt, model(tt, a, b), label="Exponential fit")
plt.xlabel("Month"); plt.ylabel("Active users (thousands)")
plt.title("User growth curve fitting"); plt.legend(); plt.grid(True); plt.show()
