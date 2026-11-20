import subprocess, re
prefixes=[('ABCA','ABCABCA'),('ABCCA',None),('ABBCA',None),('ABBCCA',None),('AABBCCA',None),('ABBBCCA',None),
          ('ABCBCA',None),('ABABCA',None),('ABABCCA',None),('AABABCCA',None),('ABABBCA',None),('ABABCBCA',None)]
out=[r"""\section*{Appendix: continuations of twelve prefixes}
For each prefix $L$ we list every word $Lv$ with pairwise disjoint restricted sumsets that is reached, by its continuation $v$ (a dot is the empty continuation). For each such word and each letter $X$ for which $LvX$ fails, one identity $i+j=k+l$ is given, with $i,j$ in one class and $k,l$ in another. A line marked \emph{run} ends with a run $Y^r$ on $[s,t]$ such that every other letter has an element in $[s-r+1,s-1]$; the witnesses are given, and by Lemma~\ref{lem:run} the letter $Y$ fills the rest of the word. Words of length at most $12$ are irrelevant for $n\ge14$; the lengths are given so that this can be read off.

{\footnotesize
"""]
for P,stop in prefixes:
    args=['python3','c0_certificates.py',P]+([stop] if stop else [])
    lines=subprocess.run(args,capture_output=True,text=True).stdout.strip().split('\n')
    out.append(r"\paragraph{$L=%s$.}"%P+"\n"+r"\begin{longtable}{@{}l@{\quad}l@{}}"+"\n")
    for ln in lines:
        v=ln[:16].strip(); rest=ln[16:].strip()
        kind,msg=rest.split(' ',1); msg=msg.strip()
        vv='$\\cdot$' if v=='.' else '$'+v+'$'
        if kind=='NODE':
            m=re.match(r'len (\d+)( COMPLETE)?; killed ?(.*)',msg)
            L,comp,k=m.group(1),m.group(2),m.group(3)
            ks=', '.join(f"${x.split(':')[0]}$: ${x.split(':')[1]}$" for x in k.split(', ') if x)
            out.append(f"{vv} & length {L}; " + (ks if ks else 'all letters possible')+r"\\"+"\n")
        elif kind=='RUN':
            m=re.match(r"(\w) to the end \(witnesses (\{.*?\})\); sizes (\{.*?\}) -> (.*)",msg)
            Y,wit,sz,verdict=m.groups()
            wit=eval(wit); sz=eval(sz)
            ws=', '.join(f"${k}\\ni {v}$" for k,v in wit.items())
            ss=', '.join(f"$|{k}|={v}$" for k,v in sz.items() if k!=Y)
            ver='a class is too small' if 'small' in verdict else r'gives $%s%s^{n-%d}$'%(P+v[:-1].rstrip(Y) if False else (P+v).rstrip(Y),Y,len((P+v).rstrip(Y)))
            out.append(f"{vv} & run of ${Y}$ ({ws}); {ss}: {ver}"+r"\\"+"\n")
        else:
            out.append(f"{vv} & residue induction"+r"\\"+"\n")
    out.append(r"\end{longtable}"+"\n")
out.append("}\n")
open('appendix_cert.tex','w').write(''.join(out))
