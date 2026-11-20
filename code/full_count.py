"""Counts all partitions of [n] into three nonempty boxes (ordered) with pairwise disjoint
restricted sumsets and compares with 33n^2-117n+9-3(-1)^n.  Usage: python3 full_count.py 14 15 16 ..."""
import sys, time
def count(n):
    # ordered triples (C1,C2,C3), classes may be empty, restricted sumsets pairwise disjoint.
    owner={}; cls=[[],[],[]]; res=[0,0,0,0]  # by number of nonempty classes
    def rec(x):
        if x>n:
            res[sum(1 for c in cls if c)]+=1; return
        for c in range(3):
            if not cls[c] and any(not cls[d] for d in range(c)): continue
            new=[x+y for y in cls[c]]
            if any(owner.get(s,c)!=c for s in new): continue
            added=[s for s in new if s not in owner]
            for s in added: owner[s]=c
            cls[c].append(x); rec(x+1); cls[c].pop()
            for s in added: del owner[s]
    rec(1)
    # canonical (first-appearance) -> ordered: k nonempty classes give 3!/(3-k)! orderings
    ordered=res[1]*3+res[2]*6+res[3]*6
    return ordered-3
for n in [int(a) for a in sys.argv[1:]]:
    t=time.time(); v=count(n); f=33*n*n-117*n+9-3*(-1)**n
    print(n,v,f,v==f,round(time.time()-t,1),flush=True)
