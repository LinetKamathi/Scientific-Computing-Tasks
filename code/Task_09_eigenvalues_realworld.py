# REAL-WORLD CASE: PageRank for a small website (4 pages)
# Assumptions: links  Home->About,Blog | About->Home | Blog->Home,About,Shop | Shop->Home
# Damping factor 0.85. The PageRank vector is the dominant eigenvector (eigenvalue 1)
# of the Google matrix.
import numpy as np

pages = ["Home", "About", "Blog", "Shop"]
# Column j = probability of moving from page j to each page i
M = np.array([[0.0, 1.0, 1/3, 1.0],
              [0.5, 0.0, 1/3, 0.0],
              [0.5, 0.0, 0.0, 0.0],
              [0.0, 0.0, 1/3, 0.0]])
d = 0.85
G = d * M + (1 - d) / 4 * np.ones((4, 4))

vals, vecs = np.linalg.eig(G)
i = np.argmax(vals.real)
rank = np.abs(vecs[:, i].real); rank /= rank.sum()

print("Dominant eigenvalue:", round(vals[i].real, 6))
for p, r in sorted(zip(pages, rank), key=lambda t: -t[1]):
    print(f"{p:6s} PageRank = {r:.4f}")

# Check with power iteration
v = np.ones(4) / 4
for _ in range(100):
    v = G @ v
print("Power-iteration result:", np.round(v, 4))
