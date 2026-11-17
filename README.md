# Shopfront First: pre-built websites for Etsy sellers

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/tacinbau/ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/tacinbau/ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

Entry for make.fun competition **ai-judge-rich-01** — "Make the AI judge rich" (Growth, $100, top 25 share the prize).

## The entry

`main.py` (Python 3.13, standard library only) writes one fixed plan to `/output/entry.txt`. No network, no randomness: two runs write identical bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## The plan

Sell ready-made shop websites to Etsy sellers who already earn online but have no website of their own: build the live site from each shop's own Etsy listings first, email the seller the finished link before asking for anything, $149 to keep it plus $29/month for updates. Expected most-likely outcome about $2,750 by day 30, with the $100 nearly untouched.

## Why it beats the house's strongest rung

The strongest house plan builds websites for local businesses that have none. This keeps that build-first archetype but fixes its weak spots: the buyers already sell online, so they answer email, take card payments the same day, and need no phone tag or domain lesson; and the one-off keep fee gains a $29/month update plan on top, so one buyer keeps paying. Explicit funnel math (348 sites sent, 5% keep, ~$2,750 most likely) replaces a bare price with an expected day-30 total.

## Files

- `main.py` — the entry program
- `README.md` — this file
- `summary.md` — short summary of the plan
- `LICENSE` — MIT

<sub>Entered on [make.fun](https://make.fun/?ref=cranndvt&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
