"""Lists the partitions with two classes of size two (type C2). Usage: python3 c2_check.py 20"""
import itertools,sys
def rs(S):
    S=sorted(S); return {S[i]+S[j] for i in range(len(S)) for j in range(i+1,len(S))}
n=int(sys.argv[1]); out=[]
pairs=list(itertools.combinations(range(1,n+1),2))
for p,q in itertools.combinations(pairs,2):
    if set(p)&set(q): continue
    R=[x for x in range(1,n+1) if x not in p and x not in q]
    if p[0]+p[1]==q[0]+q[1]: continue
    r=rs(R)
    if p[0]+p[1] in r or q[0]+q[1] in r: continue
    if len(R)==2 and sum(R) in (sum(p),sum(q)): continue
    out.append((p,q))
print(len(out)); print(out)
