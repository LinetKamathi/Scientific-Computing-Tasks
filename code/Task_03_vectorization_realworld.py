# REAL-WORLD CASE: Mobile-money transactions
# Assumptions: 1,000,000 transaction amounts (KES). Convert to USD at 1 USD = 129 KES
# and apply a 1.5 % levy. Compare a Python loop with vectorized NumPy.
import numpy as np
import timeit

rng = np.random.default_rng(7)
amount_kes = rng.lognormal(mean=6.5, sigma=1.0, size=1_000_000)
RATE, LEVY = 129.0, 0.015

def loop_version():
    out = []
    for a in amount_kes:
        out.append(a * (1 - LEVY) / RATE)
    return out

def vectorized_version():
    return amount_kes * (1 - LEVY) / RATE

t_loop = timeit.timeit(loop_version, number=1)
t_vec = timeit.timeit(vectorized_version, number=3) / 3
usd = vectorized_version()

print(f"Mean transaction: KES {amount_kes.mean():.2f}  = USD {usd.mean():.2f} after levy")
print(f"Total levy collected: KES {(amount_kes * LEVY).sum():,.0f}")
print(f"Loop time: {t_loop:.4f} s | Vectorized: {t_vec:.5f} s | Speed-up: {t_loop/t_vec:.0f}x")
