# GVR BI Report: progress log

Running log of what I've built, the skills it shows, and draft resume bullets.
Every bullet must describe work that is committed and that I can explain line by line.

## Project summary (for resume / LinkedIn)
Portfolio project on real point-of-sale data (PetPooja exports) from GVR Cashew Merchants, a dry-fruits and
festival gift-box retailer in Visakhapatnam, India. Five-week plan:
1. Monthly BI report: pandas + Streamlit
2. Analytics engineering: dbt Core on BigQuery
3. Experiment statistics
4. Festival demand forecast: BigQuery ML ARIMA_PLUS
5. Salesforce data model

Repo: https://github.com/rahulbolisetty23/gvr-bi-report

## Status
| Week | Focus | Status |
|---|---|---|
| 1 | pandas + Streamlit monthly BI report | In progress |
| 2 | dbt on BigQuery | Not started |
| 3 | Experiment statistics | Not started |
| 4 | ARIMA_PLUS festival forecast | Not started |
| 5 | Salesforce data model | Not started |

## Session log

### Day 1: Oct 23, 2026 (partial)
**Built**
- Project setup: uv, Python 3.12, pandas, Streamlit, public GitHub repo; raw data git-ignored.
- `explore.py`: loads invoice-level (~13 months) and item-level exports, skips report title rows,
  drops the TOTAL footer row, casts invoice number to integer.

**Skills shown:** Python environment management (uv), pandas `read_csv`, boolean filtering, type casting,
data-privacy hygiene (raw PII kept out of version control).

**Carries over:** profiling questions (grain, invoice-number uniqueness, date range, monthly invoices
and revenue), Streamlit hello-world.

## Draft resume bullets
_Only add a bullet once the work behind it is committed. Rewrite as the project grows._

- (Week 1, in progress) Built a Python data pipeline to ingest and clean raw POS exports from a regional
  retailer, handling report-format artifacts (title rows, total rows) and keeping customer PII out of
  version control.
