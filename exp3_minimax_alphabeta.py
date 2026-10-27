# Exp 3: Min-Max with Alpha-Beta pruning
# Tree = nested list. Root = MAX, level 1 = MIN, level 2 = MAX. Numbers = leaves.
INF = float("inf")

def minimax(node, is_max, count):
    if not isinstance(node, list):
        count[0] += 1
        return node
    vals = [minimax(c, not is_max, count) for c in node]
    return max(vals) if is_max else min(vals)

def alphabeta(node, is_max, alpha, beta, count, depth=0):
    pad = "    " * depth
    if not isinstance(node, list):
        count[0] += 1
        print(f"{pad}Leaf {node}")
        return node
    kind = "MAX" if is_max else "MIN"
    best = -INF if is_max else INF
    for i, child in enumerate(node):
        v = alphabeta(child, not is_max, alpha, beta, count, depth + 1)
        if is_max:
            best = max(best, v)
            alpha = max(alpha, best)
        else:
            best = min(best, v)
            beta = min(beta, best)
        if alpha >= beta:                       # cut-off
            if i < len(node) - 1:
                print(f"{pad}  >> PRUNED remaining branch(es) of this {kind} node")
            break
    print(f"{pad}{kind}: alpha={alpha}, beta={beta}, returns {best}")
    return best

def run(tree, title):
    print(f"\n===== {title}: {tree} =====")
    c1, c2 = [0], [0]
    mm = minimax(tree, True, c1)
    print("--- Alpha-Beta trace ---")
    ab = alphabeta(tree, True, -INF, INF, c2)
    # best move at root = child with the highest MIN value
    vals = [minimax(ch, False, [0]) for ch in tree]
    move = "left" if vals.index(max(vals)) == 0 else "right"
    print(f"\nMinMax root = {mm}, leaves evaluated = {c1[0]}")
    print(f"AlphaBeta root = {ab}, leaves evaluated = {c2[0]}")
    print(f"Best move for MAX: {move} branch")

def reverse(node):
    return [reverse(c) for c in reversed(node)] if isinstance(node, list) else node

tree1 = [[[3, 5], [6, 9]], [[1, 2], [0, -1]]]
run(tree1, "Tree 1")
run(reverse(tree1), "Tree 2 (leaves reversed)")
print("\nComment: good node ordering (best moves first) causes more cut-offs,")
print("so fewer leaves are evaluated. Bad ordering prunes less.")
