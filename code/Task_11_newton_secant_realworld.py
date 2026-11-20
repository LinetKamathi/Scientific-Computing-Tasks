# REAL-WORLD CASE: Effective monthly interest rate of a loan
# Assumptions: a KES 100,000 loan is repaid with 48 monthly instalments of KES 2,500.
# Find the monthly rate r where PV of payments = loan amount.
from scipy.optimize import root_scalar

P, pmt, n = 100_000.0, 2_500.0, 48

def f(r):
    return pmt * (1 - (1 + r)**(-n)) / r - P

def df(r):
    return pmt * (n * (1 + r)**(-n - 1) * r - (1 - (1 + r)**(-n))) / r**2

newton = root_scalar(f, fprime=df, x0=0.01, method="newton", xtol=1e-12)
secant = root_scalar(f, x0=0.01, x1=0.03, method="secant", xtol=1e-12)

print(f"Monthly rate (Newton):  {newton.root:.6%}  in {newton.iterations} iterations")
print(f"Monthly rate (Secant):  {secant.root:.6%}  in {secant.iterations} iterations")
print(f"Equivalent annual rate: {(1 + newton.root)**12 - 1:.4%}")
print(f"Residual f(r): {f(newton.root):.3e}")
