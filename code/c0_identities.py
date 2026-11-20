"""Checks every symbolic identity i+j=k+l used in the hand proof of Lemma (tails),
for ranges of the parameters.  Prints the number of failures (expected 0)."""
# verify every symbolic identity used in the hand part of the tails lemma
def cls(w,i): return w[i-1] if 1<=i<=len(w) else None
bad=[]
def chk(name,w,p,q):
    (i,j),(k,l)=p,q
    ok = i!=j and k!=l and i+j==k+l and cls(w,i)==cls(w,j) and cls(w,k)==cls(w,l) and cls(w,i)!=cls(w,k)
    if not ok: bad.append((name,w,p,q))
A=lambda k:'A'*k; B=lambda k:'B'*k; C=lambda k:'C'*k
# ---- P1, b>=2
for a in (1,2,3):
 for b in range(2,14):
  for c in range(max(1,a+b-2),b+2):
    L=A(a)+B(b)+C(c)+'A'; f=a+b+1; x=f+c
    small = L in ('ABBCA','ABBCCA','AABBCCA','ABBBCCA')
    if c==2: chk('P1 B@x+1',L+'B',(f-2,x+1),(f,f+1))
    if c==b+1: chk('P1 A@x+1 c=b+1',L+'A',(a,x+1),(f,f+1))
    if c<=b:
      if c==b: chk('P1 AA c=b',L+'AA',(a,x+2),(f,f+1))
      if b>=3: chk('P1 AB',L+'AB',(a+1,x+2),(f,f+c-b+2))
      if a==1 and c==b-1 and c>=2:
        chk('P1 AAA',L+'AAA',(1,x+3),(f,f+1))
        if b>=4: chk('P1 AAB',L+'AAB',(2,x+3),(f,f+2))
    if c>=2 and not small:
      if b<=c<=a+b-1: chk('P1 CA h',L+'CA',(a+b-c,x+2),(f,f+1))
      elif c==b+1 and a==1: chk('P1 CA c=b+1',L+'CA',(1,x+2),(f,f+2))
      if a==1 and c==b-1:
        chk('P1 CAA',L+'CAA',(1,x+3),(f,f+1)); chk('P1 CAB',L+'CAB',(f-1,x+3),(f+1,x+1))
# ---- P1, b=1
for a in range(1,15):
 for c in (1,2):
  if a==1: continue
  L=A(a)+'B'+C(c)+'A'; x=a+c+2
  if c==2:
    chk('b1 c2 A',L+'A',(a,x+1),(a+2,a+3)); chk('b1 c2 CA',L+'CA',(a-1,x+2),(a+2,a+3))
  else:
    chk('b1 CAA',L+'CAA',(a,x+3),(a+2,x+1)); chk('b1 CABB',L+'CABB',(a+1,x+4),(x,x+2))
  for l4 in range(1,6):
   if c==2 and l4>1: continue
   for j in range(1,6):
    for l in range(0,6):
     for tail in ('', 'A'):
      w=L+A(l4-1)+B(j)+C(l)+tail
      s=x+l4; t=s+j-1; u=t+l
      if tail and l>=2: chk('b1 R7 C',w,(a+2,u-1),(a,u+1))
      if tail and l==1: chk('b1 R7 B',w,(a+1,t),(a-1,u+1))
      if c==1 and l4==2 and j>=2: chk('b1 l4=2',w,(x,x+1),(a+1,x+3))
      if l4>=3: chk('b1 l4>=3',w,(a+1,s),(x,s-2))
      if l4==1 and j==2 and l>=2: chk('b1 j2',w,(s,s+1),(s-2,s+3))
      if l4==1 and j>=3 and l>=1: chk('b1 j3',w,(s-2,t+1),(s,t-1))
# ---- P2
for b in range(1,12):
  L='A'+B(b)+'CB'+C(b)+'A'; f=b+2; x=2*b+4
  chk('P2 A',L+'A',(1,x+1),(f,f+2))
  if b>=2: chk('P2 CA',L+'CA',(1,x+2),(f,f+3))
# ---- P3
for a in range(1,9):
 for e in range(1,7):
  L=A(a)+'B'+A(e)+'CA'; f=a+e+2; x=f+1
  for m in range(1,9):
    w=L+C(m)+'B'; s=x+m+1
    if m<=e-1: chk('P3 m<e',w,(a+1,s),(a+2+m,x))
    if m>=e+1: chk('P3 m>e',w,(a+1,s),(f,a+m+3))
  s=x+e+1
  chk('P3 BB',L+C(e)+'BB',(a+1,s+1),(f,x+1))
  if e>=2: chk('P3 BCB',L+C(e)+'BCB',(a+1,s+2),(f,x+2))
  if e==1: chk('P3 BCBB',L+'CBCBB',(a+1,s+3),(f,s+1))
# ---- P4 main
for b in range(1,12):
  L='ABA'+B(b)+C(b+1)+'A'; f=b+4; x=2*b+5
  chk('P4 A',L+'A',(3,x+1),(f,f+1))
  if b>=2: chk('P4 CA',L+'CA',(3,x+2),(f,f+2))
print('bad:',len(bad)); print(bad[:5])
bad=[]
for a in range(2,15):
  L=A(a)+'BCA'; x=a+3
  for l in range(1,6):
    w=L+'CAB'+C(l)+'A'; t=x+3; u=t+l
    if l>=2: chk('loc C',w,(a+2,u-1),(a,u+1))
    else: chk('loc B',w,(a+1,t),(a-1,u+1))
print('local bad:',len(bad))
