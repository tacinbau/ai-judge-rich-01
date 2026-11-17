#!/usr/bin/env python3
"""ai-judge-rich-01 round 3: Merge-odds rail.

Writes the one plain-text plan to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Stdlib only, no network, deterministic.
"""

import os
from pathlib import Path

ENTRY = """With $100, a computer and internet, I take only work priced and paid to my wallet on merge: DevPool permits. DevPool lists 124 priced issues worth $40,998, median $150, 108 in a day, 793 done; lifetime 669 tasks, $178,068 paid. No cold email, Fiverr, Upwork, Stripe: they need a human ID.

Days 1-2: wallet in code, test harness, $10 model credit, $10 gas; $80 untouched. Rank by merge odds, not price: wallet-only payout, CI green, an outside PR merged there in the last 7 days, no /start claim yet. The Price label is the offer, the tests are acceptance, and the maintainer's last 7 days — not the tag — decide my pay.

Per pick: /start, reproduce with a failing test, fix, prove with the repo suite, PR in 24 hours. Max two open; drop anything stalled five days. Ship 26 PRs. 15 merged x $150 = $2,250 gross, less 30% review loss = $1,575, plus $120 make.fun bounties in spare hours = $1,695 on day 30. Floor: 8 merged = $840 after that loss plus $120 = $960, at 99.85% by the binomial.
"""


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
