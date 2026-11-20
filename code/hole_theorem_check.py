"""Checks the theorem on intervals with one hole: all two-class partitions of [m] minus {s}
with classes of size >= 2 and disjoint restricted sumsets, against the stated list.
Usage: python3 hole_theorem_check.py 10 23"""
import itertools
def rs(S): 
    S=sorted(S); return {S[i]+S[j] for i in range(len(S)) for j in range(i+1,len(S))}
def parts(S,minsize=2):
    S=sorted(S); out=[]
    first=S[0]; rest=S[1:]
    for mask in range(1<<len(rest)):
        P=[first]+[rest[i] for i in range(len(rest)) if mask>>i&1]
        Q=[x for x in S if x not in P]
        if len(P)>=minsize and len(Q)>=minsize and not (rs(P)&rs(Q)): out.append((P,Q))
    return out
def inorder(S):
    S=sorted(S); m=len(S); res=set()
    for k in range(1,m):
        res.add(tuple(S[:k]))
        if k+1<m: res.add(tuple(S[:k-1]+[S[k]]))  # transpose S[k-1],S[k]
    return res
def predicted(m,s):
    S=[x for x in range(1,m+1) if x!=s]; N=len(S); res=set()
    for k in range(2,N-1): res.add(tuple(S[:k]))
    for k in range(2,N-1): res.add(tuple(sorted(S[:k-1]+[S[k]])))
    def add(P):
        P=sorted(P); Q=[x for x in S if x not in P]
        if 1 not in P and P: P,Q=Q,P  # normalize: class of min S
        if min(S) not in P: P,Q=Q,P
        res.add(tuple(sorted(P)))
    if 2<=s<=m-3: add(list(range(1,s))+[s+3])
    if 4<=s<=m-1: add([x for x in range(1,s) if x!=s-3])
    if s==4: add([1,5])
    if s==m-3: add(list(range(1,s-1))+[s+1,s+2])
    if s==5: add([1,3]+list(range(6,m+1)))
    if s==m-4: add(list(range(1,s))+[s+2,s+4])
    return res
import sys
bad=0
lo,hi=(int(sys.argv[1]),int(sys.argv[2])) if len(sys.argv)>2 else (10,23)
for m in range(lo,hi):
    for s in range(1,m+1):
        S=[x for x in range(1,m+1) if x!=s]
        got={tuple(P) for P,Q in parts(S)}
        if got!=predicted(m,s): bad+=1; print(m,s,got^predicted(m,s))
print('bad',bad)
