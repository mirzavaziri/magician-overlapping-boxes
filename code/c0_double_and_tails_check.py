"""Checks Lemma (tails) and Lemma (doubly split words) against exhaustive search.
Usage: python3 c0_double_and_tails_check.py 14 36"""
import sys
from c0_core import words, norm

def case2(w): return w.rfind('A') > w.find('C')
def block(w):
    import re; return re.fullmatch(r'A+B+C+', w) is not None

def doubly_split(n):
    L = {'ABABCBCA' + 'C'*(n-8), 'ABBCAAB' + 'C'*(n-7), 'A'*(n-8) + 'BACACBCB', 'A'*(n-7) + 'BCCABBC', ('ABC'*n)[:n]}
    if n % 2 == 0:
        k = (n-4)//2; L |= {'AA'+'B'*k+'C'*k+'AA', 'AA'+'B'*k+'C'*(k+1)+'A', 'A'+'B'*(k+1)+'C'*k+'AA'}
    else:
        k = (n-3)//2; L |= {'AA'+'B'*k+'C'*k+'A', 'AAA'+'B'*(k-1)+'C'*k+'A', 'ABA'+'B'*(k-1)+'C'*k+'A',
                            'A'+'B'*k+'C'*(k-1)+'AAA', 'A'+'B'*k+'C'*(k-1)+'ACA', 'A'+'B'*k+'C'*k+'AA'}
    return L

def tails(n):
    S = {('ABC'*n)[:n], 'A'*(n-7)+'BCCABBC', 'A'*(n-8)+'BACACBCB', 'ABBCAAB'+'C'*(n-7)}
    if n % 2 == 0:
        k = (n-4)//2; S |= {'AA'+'B'*k+'C'*k+'AA', 'A'+'B'*(k+1)+'C'*k+'AA'}
    else:
        k = (n-3)//2; S |= {'A'+'B'*k+'C'*k+'AA', 'A'+'B'*k+'C'*(k-1)+'AAA', 'A'+'B'*k+'C'*(k-1)+'ACA'}
    return S

if __name__ == '__main__':
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    for n in range(lo, hi):
        W = list(words(n))
        D = {w for w in W if not block(w) and case2(w) and case2(norm(w[::-1]))}
        T = set()
        for w in W:
            f = w.find('C'); l = w.rfind('A')
            if l < f: continue
            x = w.find('A', f); y = x + 1
            while y < n and w[y] == 'C': y += 1
            if y < n: T.add(w)
        print(n, 'doubly split ok' if D == doubly_split(n) else 'DOUBLY SPLIT MISMATCH',
              'tails ok' if T == tails(n) else 'TAILS MISMATCH', len(D), flush=True)
