# REAL-WORLD CASE: SIR epidemic model for a school of 1000 learners
# S' = -beta*S*I/N ; I' = beta*S*I/N - gamma*I ; R' = gamma*I
# beta = 0.5/day (contact rate), gamma = 0.1/day (recovery), 1 initially infected.
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

N, beta, gamma = 1000.0, 0.5, 0.1

def sir(t, y):
    S, I, R = y
    return [-beta*S*I/N, beta*S*I/N - gamma*I, gamma*I]

sol = solve_ivp(sir, (0, 120), [N-1, 1, 0], t_eval=np.linspace(0, 120, 400), rtol=1e-8)
S, I, R = sol.y
peak = I.argmax()
print(f"R0 = beta/gamma = {beta/gamma:.1f}")
print(f"Peak infections: {I[peak]:.0f} learners on day {sol.t[peak]:.1f}")
print(f"Total ever infected by day 120: {R[-1]:.0f} ({R[-1]/N:.1%})")

for name, y in zip(("Susceptible", "Infected", "Recovered"), sol.y):
    plt.plot(sol.t, y, label=name)
plt.xlabel("Day"); plt.ylabel("Learners"); plt.title("SIR epidemic model")
plt.legend(); plt.grid(True); plt.show()
