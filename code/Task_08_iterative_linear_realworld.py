# REAL-WORLD CASE: Heat conduction along a metal rod
# Assumptions: rod divided into 8 interior points; left end held at 80 C, right end at 30 C.
# Each interior point is the average of its neighbours: -T[i-1] + 2T[i] - T[i+1] = 0.
import numpy as np
import matplotlib.pyplot as plt

n = 8
A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
b = np.zeros(n); b[0] = 80.0; b[-1] = 30.0

def gauss_seidel(A, b, tol=1e-8, max_iter=2000):
    x = np.zeros_like(b); errs = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        e = np.linalg.norm(x - old, ord=np.inf); errs.append(e)
        if e < tol: break
    return x, errs

x, errs = gauss_seidel(A, b)
exact = np.linalg.solve(A, b)
print("Gauss-Seidel temperatures:", np.round(x, 3))
print("Direct solution:         ", np.round(exact, 3))
print("Iterations:", len(errs), "| max difference:", np.abs(x - exact).max())

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(np.arange(1, n+1), x, "o-"); ax[0].set_title("Rod temperature profile")
ax[0].set_xlabel("Position along rod"); ax[0].set_ylabel("Temperature (C)"); ax[0].grid(True)
ax[1].semilogy(errs); ax[1].set_title("Convergence"); ax[1].set_xlabel("Iteration")
ax[1].set_ylabel("Maximum change"); ax[1].grid(True)
plt.tight_layout(); plt.show()
