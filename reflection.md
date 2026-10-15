# Reflection

## 1. Which tool did you find most useful, and why?
Pylint was the most useful. It found the most issues (score went from
5.65 to 10.00) and covered bugs, style and design, such as the mutable
default argument, the bare except and the unclosed file. Bandit was the
most important for security, since it caught the dangerous `eval()`.

## 2. Did the tools report anything that wasn't a real problem (false positives)?
Mostly no. Bandit's B311 on `random` was low severity, since receipt IDs
aren't security-sensitive, but I replaced it with a counter anyway. The
Pylint warning about the global variable was a design preference rather
than a bug.

## 3. What problems did the tools miss?
They did not catch logic bugs: negative quantities giving a negative
bill, a negative tax rate being accepted, unknown items being charged 0,
and the promo code not updating the sales total. I only found these by
running the program and reading the output.

## 4. How would you use static analysis in future projects?
I would run Flake8, Pylint and Bandit before every commit, and also in
CI (e.g. GitHub Actions) so bad code can't be merged. Static analysis
catches style and security problems early, but it needs to be combined
with testing and code review.