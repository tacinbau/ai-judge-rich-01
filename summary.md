# ai-judge-rich-01 — round 2 summary

## What changed from round 1

Round 1 ("Shopfront First") sold ready-made shop sites to Etsy sellers
by cold email, with payment "by card" and a guessed 5% conversion rate.
It ranked 69/117 and lost because no money was committed anywhere and
every step needed a human to answer an email or pass an ID check.

Round 2 is a different plan, written from scratch: the agent only takes
work whose price is already posted and paid on-chain to its own wallet.

## The plan

- **Source:** the DevPool directory on GitHub — 79 open priced issues,
  $26,098 posted, median $150, checked the day the plan was written.
- **Setup (days 1–2):** wallet in code, test harness running. $10 model
  credit, $10 gas, $80 untouched.
- **Execution (days 3–30):** only $200+ issues that already carry a
  failing test in the repo. Claim with `/start`, after reading the
  upstream comments first — the mirror still lists claimed work as open.
  Reproduce, fix, prove with the repo's own tests, PR within 24 hours.
  The permit pays on merge. Max 2 issues open; drop anything stalled
  5 days.
- **While PRs wait:** make.fun bounties (escrowed USDC to the wallet)
  and CodeHawks contests (USDC in 72 hours, findings with a PoC).

## The numbers (rechecked)

- 14 PRs, 8 merged × $200 = $1,600, less 25% review loss = $1,200.
- Bounties ≈ $150; one audit medium ≈ $250.
- Day 30: $80 + $1,200 + $150 + $250 = **$1,680**.
- Floor: 4 merged × $200 = $800, less 25% = $600; $80 + $600 = **$680**.

## Why it should win

The price is posted before any work starts, the failing test proves the
bug is real, and the issue thread proves nobody has taken it — three
checks a judge can verify without trusting a conversion guess.

## Files

- `main.py` — Python 3.13, stdlib only; writes the plan to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). Deterministic,
  no network, no randomness.
- `README.md` — badges, plan summary, run instructions.
- `LICENSE` — MIT.
