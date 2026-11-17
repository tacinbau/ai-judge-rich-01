[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/tacinbau/ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/tacinbau/ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

# Make the AI judge rich — round 2

A 30-day plan for an AI agent starting with $100. It only chases money
whose price is already posted and paid on-chain to the agent's wallet:
priced DevPool issues with a failing test already in the repo, make.fun
bounties, and CodeHawks contests. No cold email, no marketplaces that
need a human ID, no uncommitted guesswork.

## The plan in short

- Days 1–2: wallet wired into code, test harness running. $10 model
  credit, $10 gas, $80 untouched.
- Days 3–30: claim $200+ issues with `/start` (after checking upstream
  comments, since the mirror lists claimed work as open), reproduce,
  fix, prove with the repo's own tests, PR within 24 hours. Paid on
  merge. At most 2 open; drop anything stalled 5 days.
- While PRs wait: escrowed make.fun bounties and CodeHawks contests.
- Expected day 30: $1,680. Floor with 4 merges and nothing else: $680.

## Run

```sh
python3 main.py
```

Writes the plan to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
Python 3.13, standard library only, deterministic, no network.
