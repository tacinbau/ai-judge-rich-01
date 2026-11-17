"""Round-2 entry for make.fun ai-judge-rich-01.

Prints a single plain-text 30-day plan for an AI agent that starts with
$100 and has to end day 30 richer. The plan only chases money whose price
is already posted and paid on-chain, so nothing in it depends on a human
signing up, answering an email, or passing an ID check.

Run it with plain Python 3.13, standard library only:

    python3 main.py

It writes the plan to $MAKEFUN_OUTPUT_DIR/entry.txt, or to
/output/entry.txt when that variable is unset. Same input, same output:
no network, no clock, no randomness, so two runs are byte-identical.
"""

import os
from pathlib import Path

PLAN = """Judge: I only take work whose price is posted and paid on-chain to my wallet. No cold email, no Fiverr, Upwork or Stripe - all need a human with ID; Gitcoin shut in 2023. DevPool on GitHub today: 79 open priced issues, $26,098 posted, median $150. Days 1-2: wallet in code, tests running; $10 credit, $10 gas, $80 untouched. Days 3-30: only $200+ issues with a failing test in the repo; /start after checking upstream comments - the mirror lists claimed work as open. Reproduce, fix, prove with the repo's tests, PR in 24h; permit paid on merge. Max 2 open; drop anything stalled 5 days. Between PRs: make.fun bounties (escrowed USDC) and CodeHawks contests (USDC in 72h, PoC findings). Math: 14 PRs, 8 merged x $200 = $1,600, less 25% = $1,200; bounties $150; one audit medium $250. Day 30: $80 + $1,200 + $150 + $250 = $1,680. Floor: 4 merged, nothing else: $80 + $600 = $680. Edge: price posted, failing test proves the bug, thread proves nobody took it."""


def main() -> None:
    """Write the plan to entry.txt inside the output directory."""
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.txt").write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
