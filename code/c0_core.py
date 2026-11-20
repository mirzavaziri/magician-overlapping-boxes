"""Common helpers for the section on configurations with all classes of size >= 3.

A configuration of [n] is a partition into three classes A, B, C, each with at
least three elements, whose restricted sumsets {x+y : x != y in the class} are
pairwise disjoint.  Configurations are written as words w_1...w_n over A, B, C,
with classes named in order of first appearance.
"""
def all_c0(n):
    """Exhaustive search: all configurations of [n], as lists of three classes."""
    owner = {}; cls = [[], [], []]; out = []
    def rec(x):
        if x > n:
            if all(len(c) >= 3 for c in cls): out.append([list(c) for c in cls])
            return
        for c in range(3):
            if not cls[c] and any(not cls[d] for d in range(c)): continue
            new = [x + y for y in cls[c]]
            if any(owner.get(s, c) != c for s in new): continue
            added = [s for s in new if s not in owner]
            for s in added: owner[s] = c
            cls[c].append(x); rec(x + 1); cls[c].pop()
            for s in added: del owner[s]
    rec(1); return out

def norm(w):
    """Rename letters by order of first appearance."""
    m = {}; o = ''
    for ch in w:
        if ch not in m: m[ch] = 'ABC'[len(m)]
        o += m[ch]
    return o

def words(n):
    """All configurations of [n] as normalized words."""
    for P in all_c0(n):
        w = [''] * n
        for ci, c in enumerate(P):
            for x in c: w[x - 1] = 'ABC'[ci]
        yield norm(''.join(w))
