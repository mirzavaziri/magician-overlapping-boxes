"""Restricted sumsets of the doubly split families, written as functions of k (Table in the paper)."""
def intervals(S):
    S=sorted(S); out=[]; 
    for s in S:
        if out and s==out[-1][1]+1: out[-1][1]=s
        else: out.append([s,s])
    return out
def rs(w):
    pos={}
    for i,ch in enumerate(w,1): pos.setdefault(ch,[]).append(i)
    return {X:intervals({P[i]+P[j] for i in range(len(P)) for j in range(i+1,len(P))}) for X,P in sorted(pos.items())}
fam={
 'A2BkCkA2 (n=2k+4)':lambda k:'AA'+'B'*k+'C'*k+'AA',
 'ABk+1CkA2 (n=2k+4)':lambda k:'A'+'B'*(k+1)+'C'*k+'AA',
 'A2BkCk+1A (n=2k+4)':lambda k:'AA'+'B'*k+'C'*(k+1)+'A',
 'ABkCkA2 (n=2k+3)':lambda k:'A'+'B'*k+'C'*k+'AA',
 'ABkCk-1A3':lambda k:'A'+'B'*k+'C'*(k-1)+'AAA',
 'ABkCk-1ACA':lambda k:'A'+'B'*k+'C'*(k-1)+'ACA',
 'A2BkCkA':lambda k:'AA'+'B'*k+'C'*k+'A',
 'A3Bk-1CkA':lambda k:'AAA'+'B'*(k-1)+'C'*k+'A',
 'ABABk-1CkA':lambda k:'ABA'+'B'*(k-1)+'C'*k+'A',
 'H1 A^aBCCABBC':lambda k:'A'*k+'BCCABBC',
 'H2 A^aBACACBCB':lambda k:'A'*k+'BACACBCB',
 'ABBCAABC^m':lambda k:'ABBCAAB'+'C'*k,
 'ABABCBCAC^m':lambda k:'ABABCBCA'+'C'*k,
}
for name,F in fam.items():
    r1,r2=rs(F(20)),rs(F(21))
    print(name)
    for X in r1:
        segs=[]
        for (p,q),(p2,q2) in zip(r1[X],r2[X]):
            def fm(u,v):
                d=v-u; c=u-20*d
                return (f"{d}k" if d>1 else ('k' if d==1 else ''))+(f"{c:+d}" if d else str(c)) if True else ''
            segs.append(f"[{fm(p,p2)},{fm(q,q2)}]" if (p,p2)!=(q,q2) else f"{{{fm(p,p2)}}}")
        print('  ',X,' '.join(segs))
