"""
Verification script for the section 'Exactly one class of size two'.

A configuration is a partition of [n] into A={a<b}, P, Q with |P|,|Q|>=3,
such that the restricted sumsets A^={a+b}, P^, Q^ are pairwise disjoint.
count_sigma(n, s) counts such configurations with a+b = s (P is the class
containing min([n]\\A)).  The script checks, for 3 <= s <= 40 and every
n with max(14, s-1) <= n <= 4s-8, the values claimed in the theorem.
"""
import sys

def count_sigma(n, s):
    total = 0
    for a in range(1, (s + 1) // 2):
        b = s - a
        if b > n or b <= a:
            continue
        S = [x for x in range(1, n + 1) if x not in (a, b)]
        sums = {'P': set(), 'Q': set()}
        members = {'P': [], 'Q': []}
        res = [0]

        def rec(i):
            if i == len(S):
                if len(members['P']) >= 3 and len(members['Q']) >= 3:
                    res[0] += 1
                return
            x = S[i]
            for c in ('P', 'Q'):
                if i == 0 and c == 'Q':
                    continue
                o = 'Q' if c == 'P' else 'P'
                new = [x + y for y in members[c]]
                if any(t in sums[o] or t == s for t in new):
                    continue
                added = [t for t in new if t not in sums[c]]
                sums[c].update(added)
                members[c].append(x)
                rec(i + 1)
                members[c].pop()
                sums[c].difference_update(added)

        rec(0)
        total += res[0]
    return total

def expected(n, s):
    return {3: 2*n - 14, 4: 2*n - 14, 5: 0, 6: 3, 7: 2, 8: 5, 9: 10}.get(s, s)

if __name__ == '__main__':
    smax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    bad = 0
    for s in range(3, smax + 1):
        for n in range(max(14, s - 1), 4 * s - 7):
            v = count_sigma(n, s)
            if v != expected(n, s):
                bad += 1
                print('MISMATCH', n, s, v, expected(n, s))
    print('checked sigma <=', smax, 'mismatches:', bad)
