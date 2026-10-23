# GVR BI Report: instructions for Claude

## Who I am
Rahul: Senior BI Analyst, 8+ years, strong SQL (BigQuery, Snowflake), Looker/LookML, ThoughtSpot.
New to Python. Learning 1–2 hours a day alongside a job search.

## What this repo is
A portfolio project on real data from GVR Cashew Merchants (dry fruits and festival gift boxes, Visakhapatnam).
5-week plan: (1) pandas + Streamlit monthly BI report, (2) dbt on BigQuery, (3) experiment statistics,
(4) ARIMA_PLUS festival forecast, (5) Salesforce data model. Plan doc: https://claude.ai/artifact/BE9oqh6GmPn7MzBUQaRR49

## How to teach me (most important)
- I write the code. Do NOT write or edit the day's build files (explore.py, clean.py, metrics.py, app.py, dbt models) unless I explicitly say "write it for me".
- Explain each concept briefly through a SQL or BI comparison first.
- Hints before answers. Put full answers behind a clear "answer" label so I can choose to look.
- When I hit an error, make me read the last line of the traceback first and tell you my guess.
- Tell me directly when my code or reasoning is wrong. Don't patronize.
- Keep each session to 1–2 hours. At the end, summarize what I finished and what carries over.
- I must be able to explain every line I commit. At the end of each week, ask me 3–5 interview-style questions.
- At the end of each session, update PROGRESS.md (session log, skills shown, status table, draft resume
  bullets) and the Progress section below. Only claim work that is committed. PROGRESS.md is synced to my
  Claude app project for resume updates, so keep it accurate and free of customer data.

## What you CAN do without asking
- Explain errors, code, and concepts.
- Fix environment, Git, and setup problems (and explain the fix).
- Review my code and point out bugs.

## Data rules
- Raw PetPooja exports live in data/raw/ and are git-ignored. Never commit them, never print customer names or phone numbers.
- invoices.csv: 1 row per invoice, Sep 22, 2025 – Oct 23, 2026. invoice_items.csv: 1 row per item line, Jan 1 – Oct 23, 2026.
- Both files have 3 title rows (skiprows=3) and a final TOTAL row to drop.
- PetPooja was in a testing phase Aug 2025 – ~Feb 2026; treat Feb 2026 onward as complete.

## Setup
- Mac, VS Code, uv (run everything with `uv run ...` from the project root), Python 3.12, GitHub repo rahulbolisetty23/gvr-bi-report (public).
- Free tools only: BigQuery sandbox, dbt Core, Streamlit Community Cloud.

## Progress
- Day 1 (partial, Oct 23, 2026): setup done; explore.py loads both files, drops TOTAL rows, casts voucherNumber.
- Next: answer the 4 profiling questions (grain, voucherNumber uniqueness, date range, monthly invoices and revenue), Streamlit hello-world, commit.
