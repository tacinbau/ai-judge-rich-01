"""ai-judge-rich-01 entry: a Python 3.13 program (standard library only).

It writes one fixed plan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR):
the plan an AI agent with $100, a computer, internet and 30 days would
follow to end with the most money. Deterministic: no network, no randomness, no time or environment
dependence -- two runs write the same bytes. The funnel math in the
plan checks out: 12 x 29 = 348 sites sent, 5% of 348 is 17.4 (17 kept),
17 x $149 = $2,533, and half of 17 is about 8 x $29 = $232.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = (
    "Sell ready-made shop websites to Etsy sellers who already earn online "
    "but have no website of their own. "
    "Day 1: build one reusable one-page shop template on free hosting and "
    "list 400 Etsy shops with 100+ sales, no own site and a public shop email. "
    "Days 2-30: build 12 live sites a day from each shop's own Etsy listings "
    "\u2014 photos, prices, bestsellers \u2014 and email the seller the finished "
    "link before asking for anything. "
    "Price: $149 to keep the site on their own domain, plus $29 a "
    "month for new products and updates, paid by card. "
    "An own site keeps the ~10% Etsy takes on every sale, so sellers have "
    "a reason to pay; they already take card payments and answer email, "
    "with no phone tag. "
    "Funnel: 12 sites a day for 29 days is 348 sent; if 5% keep one, that is "
    "17 \u00d7 $149 = $2,533, and if half of those take the monthly plan, $232 "
    "more \u2014 about $2,750 most likely by day 30. "
    "The $100 stays nearly untouched: hosting is free and sellers buy "
    "their own domains."
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
