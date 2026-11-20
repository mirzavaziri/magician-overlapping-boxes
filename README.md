# The magician's trick with overlapping boxes

Verification code for the paper by **Madjid Mirzavaziri** and **Daniel Yaqubi** on a generalization of
IMO 2000 Problem 4. The central objects are partitions of `{1,...,n}` into three classes whose
*restricted sumsets* `{x+y : x != y in the class}` are pairwise disjoint.

All proofs in the paper are written by hand. The scripts are an independent check and produce the
bookkeeping tables of the appendix. They use only the Python 3 standard library.

| Script | What it checks | Example |
|---|---|---|
| `code/full_count.py` | Total number of partitions (three nonempty boxes) equals `33n^2-117n+9-3(-1)^n` | `python3 full_count.py 14 15 100` |
| `code/c1_verify.py` | The values `N_sigma(n)` for one class of size two, `sigma <= 40` | `python3 c1_verify.py` |
| `code/c0_catalog_check.py` | Explicit catalogue of configurations with all classes of size at least three equals exhaustive search | `python3 c0_catalog_check.py 14 52` |
| `code/c0_double_and_tails_check.py` | The lemmas on doubly split words and on tails | `python3 c0_double_and_tails_check.py 14 36` |
| `code/c0_identities.py` | Every symbolic identity `i+j=k+l` used in the hand proofs, over parameter ranges | `python3 c0_identities.py` |
| `code/c0_certificates.py` | Continuation tree of a fixed prefix (appendix) | `python3 c0_certificates.py ABBCA` |
| `code/c0_certificates_tex.py` | Writes the appendix tables as LaTeX | `python3 c0_certificates_tex.py` |
| `code/host_sets_check.py` | Host sets for r-1 and r-2 copies (Hall's theorem) | `python3 host_sets_check.py` |
| `code/hole_theorem_check.py` | Two-class partitions of an interval with one hole | `python3 hole_theorem_check.py 10 23` |
| `code/hole_identities.py` | Identities used in the proof of the hole theorem | `python3 hole_identities.py` |
| `code/c2_check.py` | Partitions with two classes of size two (180 ordered triples) | `python3 c2_check.py 20` |
| `code/c0_sumsets.py` | Restricted sumsets of the doubly split families (table in the paper) | `python3 c0_sumsets.py` |

Run the scripts from inside the `code` folder.

## License

MIT. See `LICENSE`.
