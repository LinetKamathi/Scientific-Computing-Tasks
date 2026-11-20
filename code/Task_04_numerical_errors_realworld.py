# REAL-WORLD CASE: Accumulated rounding error in a banking system
# Assumptions: a savings app adds a KES 0.10 interest credit 1,000,000 times.
# The exact total is KES 100,000. Naive float summation drifts from this.
import math
import numpy as np

n = 1_000_000
naive = 0.0
for _ in range(n):
    naive += 0.1

exact = 100_000.0
numpy_sum = np.sum(np.full(n, 0.1))   # pairwise summation
fsum = math.fsum([0.1] * n)           # error-compensated summation

for name, val in [("Naive loop", naive), ("np.sum", numpy_sum), ("math.fsum", fsum)]:
    err = abs(val - exact)
    print(f"{name:11s}: {val:.10f}  abs error={err:.3e}  rel error={err/exact:.3e}")

# Money should be compared with tolerance, never ==
print("naive == 100000.0 ?", naive == exact)
print("np.isclose(naive, 100000.0) ?", np.isclose(naive, exact))

# Integer cents avoid the problem entirely
cents = 10 * n
print("Integer-cents total: KES", cents / 100)
