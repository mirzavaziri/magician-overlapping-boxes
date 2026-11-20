"""Checks every identity used in the proof of the hole theorem (expected output: 0 [])."""
bad=[]
def chk(name,P,Q,i,j,k,l):
    ok=i!=j and k!=l and i+j==k+l and ((i in P and j in P and k in Q and l in Q) or (i in Q and j in Q and k in P and l in P))
    if not ok: bad.append((name,sorted(P),sorted(Q),(i,j,k,l)))
def mk(L,R,s):
    P=set();Q=set()
    for i,ch in enumerate(L,1): (P if ch=='P' else Q).add(i)
    for i,ch in enumerate(R,s+1): (P if ch=='P' else Q).add(i)
    return P,Q
for m in range(10,26):
  for s in range(2,m):
    nL,nR=s-1,m-s
    # Case I
    for q in range(1,nL):
      p=nL-q
      for r in range(1,nR+1):
        t=nR-r; P,Q=mk('P'*p+'Q'*q,'P'*r+'Q'*t,s)
        if q>=3: chk('Ia',P,Q,p,s+1,p+2,s-1)
        elif q==2 and s>=5: chk('Ib',P,Q,s-4,s+1,s-2,s-1)
        elif q==2 and s==4 and t>=1 and r in (2,3): chk('Ic1',P,Q,5,6,3,8)
        elif q==2 and s==4 and t>=1 and r>=4: chk('Ic2',P,Q,2,r+5,5,r+2)
        elif q==1 and t>=1 and r==2 and t>=2: chk('Id1',P,Q,s+1,s+2,s-1,s+4)
        elif q==1 and t>=1 and r>=3: chk('Id2',P,Q,s+1,s+r-1,s-1,s+r+1)
    # Case II
    L='P'*nL
    for a in range(1,nR):
      for c in range(1,nR-a):
        if a+1+c!=nR: continue
        P,Q=mk(L,'Q'*a+'P'+'Q'*c,s)
        if a>=3: chk('IIa',P,Q,s-1,s+a+1,s+1,s+a-1)
      for b in range(1,nR):
        if a+2+b!=nR: continue
        P,Q=mk(L,'Q'*a+'PQ'+'P'*b,s)
        if a==1 and b>=2: chk('IIb',P,Q,s-1,s+5,s+1,s+3)
        if a==2 and s>=3: chk('IIc',P,Q,s-2,s+5,s+1,s+2)
        if a==2 and s==2 and b>=2: chk('IId',P,Q,1,8,3,6)
        if a>=3: chk('IIe',P,Q,s-1,s+a+1,s+1,s+a-1)
print(len(bad),bad[:3])
