# REAL-WORLD CASE: Least-cost dairy feed mix
# Assumptions: mix 100 kg from maize bran (KES 30/kg, 8 % protein) and soya cake
# (KES 50/kg, 40 % protein). The mix needs at least 18 kg of protein in total.
import numpy as np
from scipy.optimize import linprog

cost = [30, 50]                       # KES per kg
A_ub = [[-0.08, -0.40]]               # -(protein) <= -18
b_ub = [-18]
A_eq = [[1, 1]]; b_eq = [100]         # total 100 kg

res = linprog(cost, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * 2)
bran, soya = res.x
print("Success:", res.success)
print(f"Maize bran: {bran:.2f} kg | Soya cake: {soya:.2f} kg")
print(f"Protein supplied: {0.08*bran + 0.40*soya:.2f} kg (required 18 kg)")
print(f"Minimum cost: KES {res.fun:.2f}")
