

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| `eval()` on user promo input (B307, W0123) | Security (Medium) | 27 | Arbitrary code execution via the promo prompt | Replace with a `PROMO_CODES` dict and safe arithmetic |
| `random` for receipt IDs (B311) | Security (Low) | 21 | PRNG flagged by Bandit | Use a sequential counter (IDs needn't be random) |
| `try/except/pass` (B110, W0718) | Security/Quality | 33-34 | Silently swallows errors; also catches too-broad `Exception` | Catch `KeyError`, handle or raise |
| Bare `except:` (E722, W0702) | Bug | 16 | Hides unknown items, string qty, etc. (Bill 2 and 4 charged 0) | Catch `KeyError, TypeError` and raise `ValueError` |
| Mutable default `receipts=[]` (W0102) | Bug | 10 | List shared across calls | Default `None`, create the list inside |
| `open()` never closed (W1514, R1732) | Resource leak | 37 | File handle leaks, no encoding | `with open(file, "a", encoding="utf-8")` |
| Unused imports `json`, `logging` (F401, W0611) | Style | 1, 3 | Dead code | Remove |
| Unused variable `total` (F841, W0612) | Quality | 26 | `eval` uses it implicitly, so tools can't see it | Gone once `eval` is replaced |
| `global sales_total` (W0603) + non-UPPER constant name (C0103) | Design | 7, 11 | Global mutable state | Keep it with a comment, or wrap in a class and rename |
| `printSales` naming (C0103) | Style | 41 | Not snake_case | Rename `print_sales` |
| Missing docstrings (C0114, C0116) | Style | 1, 10, 24, 29, 36, 41, 44 | No documentation | Add docstrings |
| `%` formatting (C0209) | Style | 21 | Old style | Use an f-string |
| Blank lines and long line (E302, E305, E501) | Formatting | 10, 21, 24, 29, 36, 41, 44, 56 | PEP 8 | Fix spacing and wrap line 21 |
| Negative qty (-4) gives negative bill | Logic (manual) | Bill 3 | Total of -630 | Validate qty > 0 |
| Negative tax rate (-1) accepted | Logic (manual) | Bill 4 | Invalid input | Validate 0 ≤ tax ≤ 1 |
| Promo doesn't update `sales_total` | Logic (manual) | `apply_promo_code` | "Sales so far" is unchanged by the promo | Update the total, or apply per bill |
| `update_stock` is a no-op | Logic (manual) | `update_stock` | Does nothing useful | Implement real stock, or remove it |
| Float noise (`301.4550000004`) | Logic (manual) | outputs | Floating-point display | `round(x, 2)` |
