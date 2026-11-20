"""
Control for the section on configurations with all classes of size >= 3.
allC0(n): exhaustive search; catalog(n): the explicit list of block, residue and
split words from the section.  Usage: python3 c0_catalog_check.py 14 52
"""
import re, sys
from c0_core import all_c0 as allC0
def _unused_allC0(n):
    owner={}; cls=[[],[],[]]; out=[]
    def rec(x):
        if x>n:
            if all(len(c)>=3 for c in cls): out.append([list(c) for c in cls])
            return
        for c in range(3):
            if not cls[c] and any(not cls[d] for d in range(c)): continue
            new=[x+y for y in cls[c]]
            if any(owner.get(s,c)!=c for s in new): continue
            added=[s for s in new if s not in owner]
            for s in added: owner[s]=c
            cls[c].append(x); rec(x+1); cls[c].pop()
            for s in added: del owner[s]
    rec(1); return out
import re, sys
def catalog(n):
    S=set()
    def add(w):
        if len(w)==n and all(w.count(ch)>=3 for ch in 'ABC'): S.add(w)
    # blocks with transpositions
    for sa in range(3,n):
        for sb in range(3,n-sa):
            sc=n-sa-sb
            if sc<3: continue
            for t1 in (0,1):
                for t2 in (0,1):
                    w=list('A'*sa+'B'*sb+'C'*sc)
                    if t1: w[sa-1],w[sa]=w[sa],w[sa-1]
                    if t2: w[sa+sb-1],w[sa+sb]=w[sa+sb],w[sa+sb-1]
                    add(''.join(w))
    # residue
    add(('ABC'*n)[:n])
    # case 1 x-type
    for a in range(1,n):
        for e in range(1,n):
            p=a+1+e
            for tail,conds in (('BB',(-1,0)),('BBB',(-1,)),('BCB',(-1,-3))):
                c=n-p-len(tail)
                if c<1: continue
                if 2*p-(n+a) in conds:
                    if tail=='BCB' and 2*p-(n+a)==-3 and not (e==1 and c==2): continue
                    add('A'*a+'B'+'A'*e+'C'*c+tail)
    # case 2
    for b in range(1,n):
        for (a,dc) in ((2,0),(2,1),(3,1)):
            c=b+dc
            for m in range(0,n):
                add('A'*a+'B'*b+'C'*c+'A'+'C'*m)
        for c in ([b+1]+([1] if b==2 else [])):
            for m in range(0,n): add('ABA'+'B'*b+'C'*c+'A'+'C'*m)
    add('ABABCBCA'+'C'*(n-8)); add('ABBCAAB'+'C'*(n-7))
    if n%2==0:
        k=(n-4)//2; add('AA'+'B'*k+'C'*k+'AA'); add('A'+'B'*(k+1)+'C'*k+'AA')
    else:
        k=(n-3)//2; add('A'+'B'*k+'C'*(k-1)+'AAA'); add('A'+'B'*k+'C'*(k-1)+'ACA'); add('A'+'B'*k+'C'*k+'AA')
    add('A'*(n-7)+'BCCABBC'); add('A'*(n-8)+'BACACBCB')
    return S
if __name__=='__main__':
    bad=0
    for n in range(int(sys.argv[1]),int(sys.argv[2])):
        brute=set()
        for A,B,C in allC0(n):
            brute.add(''.join('A' if x in A else ('B' if x in B else 'C') for x in range(1,n+1)))
        cat=catalog(n)
        if cat!=brute:
            bad+=1; print(n,'missing',sorted(brute-cat)[:5],'extra',sorted(cat-brute)[:5])
    print('done, mismatching n:',bad)
