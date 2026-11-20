# REAL-WORLD CASE: Risk of a construction project missing its deadline
# Assumptions: three sequential tasks with triangular durations (min, most likely, max) days:
# Foundation (8,10,16), Walls (12,15,24), Roof (6,8,14). Deadline = 38 days.
# Second part: estimating pi from random points.
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
N, deadline = 100_000, 38
total = (rng.triangular(8, 10, 16, N) + rng.triangular(12, 15, 24, N) + rng.triangular(6, 8, 14, N))

print(f"Mean duration: {total.mean():.2f} days, std: {total.std():.2f}")
print(f"Probability of finishing after {deadline} days: {(total > deadline).mean():.2%}")
print(f"90th percentile duration: {np.percentile(total, 90):.1f} days")

pts = rng.random((N, 2))
pi_est = 4 * np.mean((pts**2).sum(axis=1) <= 1)
print(f"Monte Carlo estimate of pi: {pi_est:.4f} (error {abs(pi_est-np.pi):.4f})")

plt.hist(total, bins=60); plt.axvline(deadline, color="r", ls="--", label="Deadline")
plt.xlabel("Project duration (days)"); plt.ylabel("Frequency")
plt.title("Monte Carlo project duration"); plt.legend(); plt.show()
