# Exp 1: Water Jug Problem using DFID
# State = (x, y): x = litres in jug A, y = litres in jug B. Goal: x == target

def successors(state, a, b):
    x, y = state
    p = min(x, b - y)   # amount poured A -> B
    q = min(y, a - x)   # amount poured B -> A
    return [("Fill A", (a, y)),
            ("Fill B", (x, b)),
            ("Empty A", (0, y)),
            ("Empty B", (x, 0)),
            ("Pour A->B", (x - p, y + p)),
            ("Pour B->A", (x + q, y - q))]

nodes = 0

def dls(path, limit, a, b, target):
    """Depth limited search. path = list of (operator, state)."""
    global nodes
    state = path[-1][1]
    if state[0] == target:
        return path
    if limit == 0:
        return None
    for op, nxt in successors(state, a, b):
        if nxt not in [s for _, s in path]:      # don't revisit state on current path
            nodes += 1
            result = dls(path + [(op, nxt)], limit - 1, a, b, target)
            if result:
                return result
    return None

def dfid(a, b, target):
    global nodes
    nodes = 0
    max_depth = (a + 1) * (b + 1)
    print(f"\nJugs {a}L and {b}L, target = {target}L in the {a}L jug")
    for limit in range(max_depth + 1):          # limits 0, 1, 2, ...
        result = dls([("Start", (0, 0))], limit, a, b, target)
        if result:
            for op, s in result:
                print(f"  {op:10s} -> {s}")
            print(f"Goal reached at depth {len(result) - 1}, nodes generated = {nodes}")
            return
    print(f"No solution (searched up to depth {max_depth}, nodes generated = {nodes})")

dfid(4, 3, 2)   # main problem
dfid(5, 3, 4)   # second combination
dfid(4, 2, 3)   # unsolvable case
