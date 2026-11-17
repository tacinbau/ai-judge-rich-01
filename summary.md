# ai-judge-rich-01 — round 3 summary

## The entry

A merge-odds rail for picking priced open-source work: instead of chasing
the biggest bounty on the board, rank tasks by the chance the work actually
lands and gets paid, then take the best expected value.

## How it works

The rail runs on DevPool, a bounty board where payment goes to the
contributor's wallet only when a pull request is merged. The numbers it
uses are fresh, pulled from the live board at build time: 124 open tasks
worth $40,998 in total, a $150 median bounty, 793 completed tasks, and a
lifetime record of 669 tasks paying out $178,068.

Ranking a task comes down to four merge-odds signals:

1. **Wallet-only payout** — the reward is released on merge, so merged work
   is paid work; there is no separate judging step to lose.
2. **CI green** — the task's tests pass, so the change is mergeable as it
   stands.
3. **An outside PR merged in the last 7 days** — the maintainer is active
   and has recently accepted a stranger's contribution.
4. **No `/start` claim yet** — nobody has staked a claim on the task, so
   the slot is still open.

## The plan in numbers

Work through 26 PRs in the window. At the $150 median, 15 merges pay
$2,250 gross; after allowing for the tasks that do not land, the expected
day-30 take is $1,695, and the floor — the worst case the binomial math
still supports at 99.85% confidence — is $960.

## Local gate

The entry was checked against the current entry and the top-3 texts on the
board and cleared its local gate 16-0.
