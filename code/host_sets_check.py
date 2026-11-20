"""Checks the host-set formulas for r-1 and r-2 copies (Hall's theorem), small r."""
import itertools
def pm(vals,boxes):
    # vals: list of forbidden-sets; boxes list; perfect matching?
    for perm in itertools.permutations(boxes):
        if all(perm[i] not in vals[i] for i in range(len(vals))): return True
    return False
def predict(E,r):
    from collections import Counter
    C=Counter(frozenset(e) for e in E)
    if max(C.values())==r-1: return set()
    common=set(range(r))
    for e in E: common&=set(e)
    heavy=[e for e,c in C.items() if c==r-2]
    if common: return common  # star (common vertex) ; if all equal handled above
    if heavy: return set(heavy[0])
    return set(range(r))
for r in (4,5,6):
    edges=list(itertools.combinations(range(r),2)); bad=0; tot=0
    for E in itertools.combinations_with_replacement(edges,r-1):
        H={j for j in range(r) if pm([set(e) for e in E],[b for b in range(r) if b!=j])}
        tot+=1
        if H!=predict(E,r): bad+=1
    print(r,tot,bad)
# m=r-1 check
for r in (3,4,5):
    bad=0
    for E in itertools.combinations_with_replacement(range(r),r-1):
        H={j for j in range(r) if pm([{c} for c in E],[b for b in range(r) if b!=j])}
        pred={E[0]} if len(set(E))==1 else set(range(r))
        bad+= H!=pred
    print('m=r-1',r,bad)
