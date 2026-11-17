# ai-judge-rich-01 — Merge-odds rail: priced work, paid on merge

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/tacinbau/ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/tacinbau/ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

Most bounty hunting ranks tasks by the size of the prize. This entry ranks
them by the odds of actually getting paid: it is a rail for choosing priced
open-source work on DevPool, where the reward lands in the contributor's
wallet only when a pull request is merged. Tasks are scored on four
merge signals — wallet-only payout on merge, green CI, an outside PR merged
in the last 7 days, and no claim staked yet — using fresh board numbers
(124 open tasks, $40,998 on the table, $150 median, 793 completed).
The plan works 26 PRs toward 15 merges at the $150 median, expecting
$1,695 by day 30 with a $960 floor at 99.85% binomial confidence.

## Run

```sh
python3 main.py
```

This writes the entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
Stdlib only, no network, deterministic.
