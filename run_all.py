"""Run every program, save text output to outputs/ and figures to figures/."""
import glob, os, subprocess, sys

WRAP = '''
import sys, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
_n = [0]
def _show(*a, **k):
    _n[0] += 1
    plt.savefig(sys.argv[2] if _n[0] == 1 else sys.argv[2].replace(".png", f"_{_n[0]}.png"), dpi=110, bbox_inches="tight")
    plt.close("all")
plt.show = _show
import runpy; runpy.run_path(sys.argv[1], run_name="__main__")
'''
os.makedirs("outputs", exist_ok=True); os.makedirs("figures", exist_ok=True)
for f in sorted(glob.glob("code/Task_*.py")):
    stem = os.path.basename(f)[:-3]
    r = subprocess.run([sys.executable, "-c", WRAP, f, f"figures/{stem}.png"], capture_output=True, text=True)
    open(f"outputs/{stem}.txt", "w").write(r.stdout + (("\nERROR:\n" + r.stderr) if r.returncode else ""))
    print(("OK  " if r.returncode == 0 else "FAIL"), stem)
    if r.returncode: print(r.stderr[-400:])
