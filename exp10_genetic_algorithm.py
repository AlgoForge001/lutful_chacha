# Exp 10: Genetic Algorithm, maximise f(x) = x^2, x in 0..31 (5-bit chromosome)
import random
import matplotlib.pyplot as plt

def fit(c):
    return int(c, 2) ** 2

def mutate(c, pm):
    return "".join(b if random.random() > pm else str(1 - int(b)) for b in c)

def run(pop_size=6, pm=0.02, pc=0.8, gens=50, table=False):
    pop = ["".join(random.choice("01") for _ in range(5)) for _ in range(pop_size)]
    best_hist, avg_hist = [], []
    best_c = max(pop, key=fit)
    for g in range(gens):
        f = [fit(c) for c in pop]
        total, avg = sum(f), sum(f) / len(f)
        best_hist.append(max(f))
        avg_hist.append(avg)
        best_c = max([best_c] + pop, key=fit)
        if table and g == 0:
            print("Chromosome  x   f(x)  Prob    Expected")
            for c, fi in zip(pop, f):
                print(f"{c}      {int(c, 2):2d}  {fi:4d}  {fi / total:.3f}   {fi / avg:.2f}")
        new = []
        while len(new) < pop_size:
            p1, p2 = random.choices(pop, weights=[x + 1e-9 for x in f], k=2)  # roulette wheel
            if random.random() < pc:                                          # crossover
                cut = random.randint(1, 4)
                p1, p2 = p1[:cut] + p2[cut:], p2[:cut] + p1[cut:]
            new += [mutate(p1, pm), mutate(p2, pm)]                           # mutation
        pop = new[:pop_size]
    return best_c, best_hist, avg_hist

print("=== Run 1: pop = 6, pm = 0.02 ===")
best, b1, a1 = run(6, 0.02, table=True)
print(f"Best chromosome = {best}, x = {int(best, 2)}, f = {fit(best)}")
for g in range(0, 50, 10):
    print(f"Gen {g + 1:2d}: best = {b1[g]}, avg = {a1[g]:.1f}")

print("\n=== Run 2: pop = 20, pm = 0.02 ===")
best2, b2, a2 = run(20, 0.02)
print(f"Best chromosome = {best2}, f = {fit(best2)}, final avg = {a2[-1]:.1f}")

print("\n=== Run 3: pop = 6, pm = 0.2 ===")
best3, b3, a3 = run(6, 0.2)
print(f"Best chromosome = {best3}, f = {fit(best3)}, final avg = {a3[-1]:.1f}")

plt.plot(a1, label="avg (pop 6, pm 0.02)")
plt.plot(a2, label="avg (pop 20, pm 0.02)")
plt.plot(a3, label="avg (pop 6, pm 0.2)")
plt.plot(b1, "k--", label="best (pop 6, pm 0.02)")
plt.xlabel("Generation"); plt.ylabel("Fitness"); plt.title("Convergence curve")
plt.legend(); plt.show()
