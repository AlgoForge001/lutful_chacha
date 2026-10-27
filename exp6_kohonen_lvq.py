# Exp 6: Kohonen SOM and LVQ
import numpy as np
import matplotlib.pyplot as plt

# ---------- Part 1: SOM on 4 vectors, 2 output neurons, R = 0 ----------
X = np.array([[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]], dtype=float)
W = np.array([[0.2, 0.6, 0.5, 0.9],
              [0.8, 0.4, 0.7, 0.3]])
alpha = 0.6
for epoch in range(1, 6):
    print(f"\nEpoch {epoch}, alpha = {alpha:.4f}")
    for i, x in enumerate(X, 1):
        D = ((W - x) ** 2).sum(axis=1)          # D(j) = sum (w_ij - x_i)^2
        j = D.argmin()                           # winner
        W[j] += alpha * (x - W[j])               # update only the winner
        print(f"  x{i} -> D = {np.round(D, 3)}, winner = neuron {j + 1}")
    print("  W1 =", np.round(W[0], 3))
    print("  W2 =", np.round(W[1], 3))
    alpha /= 2

clusters = {1: [], 2: []}
for i, x in enumerate(X, 1):
    clusters[((W - x) ** 2).sum(axis=1).argmin() + 1].append(f"x{i}")
print("\nFinal clusters:", clusters)

# ---------- Part 2: SOM on 2-D random points (1-D map of 4 neurons) ----------
np.random.seed(1)
pts = np.random.rand(200, 2)
n = 4
w = np.random.rand(n, 2)
alpha, R = 0.5, 1
for epoch in range(30):
    for p in pts:
        win = ((w - p) ** 2).sum(axis=1).argmin()
        for j in range(n):
            if abs(j - win) <= R:               # neighbourhood
                w[j] += alpha * (p - w[j])
    alpha *= 0.9
    if epoch == 15:
        R = 0                                    # shrink radius
plt.figure()
plt.scatter(pts[:, 0], pts[:, 1], s=8, label="data")
plt.plot(w[:, 0], w[:, 1], "ro-", label="SOM weights")
plt.title("SOM: data points and final weight vectors")
plt.legend()
plt.savefig("som_plot.png")

# ---------- Part 3: LVQ (labelled data, 2 classes) ----------
np.random.seed(2)
A = np.random.randn(50, 2) * 0.5 + [0, 0]       # class 0
B = np.random.randn(50, 2) * 0.5 + [3, 3]       # class 1
data = np.vstack([A, B])
labels = np.array([0] * 50 + [1] * 50)
proto = np.array([data[0], data[50]])           # one prototype per class
proto_cls = np.array([0, 1])
alpha = 0.3
for epoch in range(20):
    for x, c in zip(data, labels):
        j = ((proto - x) ** 2).sum(axis=1).argmin()
        if proto_cls[j] == c:
            proto[j] += alpha * (x - proto[j])   # correct -> move towards x
        else:
            proto[j] -= alpha * (x - proto[j])   # wrong   -> move away from x
    alpha *= 0.9
pred = [proto_cls[((proto - x) ** 2).sum(axis=1).argmin()] for x in data]
print("\nLVQ accuracy = %.1f %%" % (100 * np.mean(np.array(pred) == labels)))
plt.show()
