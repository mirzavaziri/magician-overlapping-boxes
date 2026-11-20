"""Certificate trees for fixed prefixes.  For every valid prefix w (pairwise disjoint
restricted sumsets) and every letter X such that wX is not valid, print one identity
i+j=k+l that kills wX.  A branch stops as an infinite run when the word ends with a
maximal run Y^r on [s,t] and every other letter has an element in [s-r+1,s-1]
(run lemma): then Y fills the rest of the word."""
import sys
def collision(w):
    n=len(w); pos={}
    for i,ch in enumerate(w,1): pos.setdefault(ch,[]).append(i)
    own={}
    for X,P in pos.items():
        for i in range(len(P)):
            for j in range(i+1,len(P)):
                own.setdefault(P[i]+P[j],[]).append((X,P[i],P[j]))
    for s,L in sorted(own.items()):
        for p in L:
            for q in L:
                if p[0]<q[0] and n in (p[1],p[2],q[1],q[2]):
                    return f"{p[1]}+{p[2]}={q[1]}+{q[2]}"
    for s,L in own.items():
        if len({p[0] for p in L})>1: return 'earlier'
    return None
def runstop(w):
    Y=w[-1]; t=len(w); s=t
    while s>1 and w[s-2]==Y: s-=1
    r=t-s+1
    if r<2: return None
    wit={}
    for Z in 'ABC':
        if Z==Y: continue
        els=[i for i,ch in enumerate(w,1) if ch==Z and s-r+1<=i<=s-1]
        if not els: return None
        wit[Z]=els[-1]
    return wit
def sizes(w): return {c:w.count(c) for c in 'ABC'}
out=[]
def rec(w,P,depth=0):
    if STOP and w==STOP:
        out.append((w,'STOP','residue induction')); return
    rs=runstop(w) if len(w)>len(P) else None
    if rs is not None:
        Y=w[-1]; sz=sizes(w); ok=all(sz[c]>=3 for c in 'ABC' if c!=Y)
        out.append((w,'RUN',f"{Y} to the end (witnesses {rs}); sizes {sz} -> {'family' if ok else 'class too small'}"))
        return
    kills=[]
    for X in 'ABC':
        c=collision(w+X)
        if c is None: rec(w+X,P,depth+1)
        else: kills.append(f"{X}:{c}")
    sz=sizes(w)
    full=all(v>=3 for v in sz.values())
    out.append((w,'NODE',f"len {len(w)}{' COMPLETE' if full else ''}; killed {', '.join(kills)}"))
P=sys.argv[1]
STOP=sys.argv[2] if len(sys.argv)>2 else None
rec(P,P)
for w,k,msg in sorted(out,key=lambda t:t[0]):
    print(f"{w[len(P):] or '.':16s} {k:4s} {msg}")
