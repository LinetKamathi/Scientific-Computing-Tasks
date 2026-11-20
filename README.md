# BIT 2118: Scientific Computing - Group Work (Tasks 2-20)

**Student:** Linet Kamathi  **Admission No:** BSCCS/2024/50325

This repository holds my individual submission for BIT 2118. For every Part (A to S, Tasks 2 to 20) it contains:

1. the **original program** (`Task_XX_<name>.py`)
2. the **same program with a parameter changed** (`Task_XX_<name>_modified.py`)
3. a **new program for a related real-world case** (`Task_XX_<name>_realworld.py`)
4. the program output (`outputs/`) and graphs (`figures/`)

The full documentation (concept, inputs and operations, output meaning, graph interpretation, effect of the parameter change, real-world assumptions and interpretation) is in `docs/BIT2118_Documentation_Linet_Kamathi.pdf`.

## Parts and tasks

| Part | Task | Topic | Real-world case |
|---|---|---|---|
| A | 2 | NumPy arrays | Greenhouse monitoring |
| B | 3 | Vectorization | Mobile-money transactions |
| C | 4 | Floating-point errors | Savings-interest rounding |
| D | 5 | Matrix algebra | Drone map of a farm plot |
| E | 6 | Linear systems | Circuit mesh currents |
| F | 7 | Gaussian elimination / LU | Building displacements |
| G | 8 | Iterative methods | Heat in a metal rod |
| H | 9 | Eigenvalues | Website PageRank |
| I | 10 | Bisection / fixed point | Bakery break-even |
| J | 11 | Newton / secant | Loan interest rate |
| K | 12 | Nonlinear equations | Wi-Fi coverage on a road |
| L | 13 | Interpolation | Reservoir level |
| M | 14 | Curve fitting | App user growth |
| N | 15 | Numerical differentiation | Train acceleration |
| O | 16 | Numerical integration | River water volume |
| P | 17 | Euler method | Fish population (logistic) |
| Q | 18 | SciPy ODE solver | SIR epidemic |
| R | 19 | Optimization | Dairy feed mix |
| S | 20 | Monte Carlo | Project deadline risk |

## How to run

```bash
pip install -r requirements.txt
python code/Task_02_numpy_arrays.py          # run one program
python run_all.py                            # run all 57 programs, refresh outputs/ and figures/
```

Requires Python 3.9+ and NumPy 2.x (the code uses `np.trapezoid`; on NumPy 1.x replace it with `np.trapz`).
