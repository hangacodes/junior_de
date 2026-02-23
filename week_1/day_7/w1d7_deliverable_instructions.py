'''### 🚨 PIPELINE RUN AUDITOR

---

### Scenario

You’re a junior data engineer at a company that runs four nightly ETL pipelines. Every morning, you receive a raw log file with one status record per pipeline. The records are messy — inconsistent spacing, labeled fields mixed with plain values, mixed-case statuses.

Your job: parse all four records, compute key metrics, and produce:
1. A formatted **run report card** for each pipeline
2. A **CSV summary line** per pipeline suitable for loading into a database
3. A **global summary block** at the end

There are no loops, no if/else, no functions, no imports. Raw Python only — everything you know from this week.

---

### The Raw Data

```python
r1 = "  PIPE-01 | etl_customers | 2026-02-09 | 06:00:00 |  127 | rows=  8420 |   SUCCESS  "
r2 = "  PIPE-02 | etl_orders    | 2026-02-09 | 06:02:15 |  203 | rows= 12450 |   SUCCESS  "
r3 = "  PIPE-03 | etl_products  | 2026-02-09 | 06:05:38 |   45 | rows=   891 |    WARN    "
r4 = "PIPE-04|etl_events|2026-02-09|06:06:23|  3782 | rows=99103|FAILED"
```

**Field layout (pipe-delimited, 7 fields):**

```
pipe_id | job_name | run_date | start_time | duration_seconds | rows_processed_label | status
```

- `duration_seconds` is an integer (seconds the job ran)
- `rows_processed_label` has the format `rows= N` — a labeled field like W1D6’s deliverable
- `status` may have surrounding whitespace and/or inconsistent casing

---

### Phase 1 — Parse a Single Record (Warm-Up)

Before tackling all 4, get your parse logic right on `r1` only.

In `pipeline_auditor.py`:

```python
# PHASE 1: parse r1 only
r1 = "  PIPE-01 | etl_customers | 2026-02-09 | 06:00:00 |  127 | rows=  8420 |   SUCCESS  "

parts = r1.split("|")

pipe_id  = parts[0].strip()
job_name = parts[1].strip()
run_date = parts[2].strip()
start_time = parts[3].strip()
duration_seconds = int(parts[4].strip())
rows_label = parts[5].strip()              # "rows=  8420"
status_raw = parts[6].strip()

#TODO: extract the numeric part of rows_label and cast to int
# Hint: split on "=" then strip and cast

#TODO: normalize status → lowercase, stripped

#TODO: parse run_date into year, month, day using slicing
# run_date is "2026-02-09" — same format as W1D4

#TODO: compute duration_minutes (whole minutes) and leftover_seconds
# Hint: use // and %

#TODO: print r1's full parsed values to confirm they're correct
```

Once all values print correctly, commit: `git add -A && git commit -m "W1D7 phase 1: r1 parse verified"`

---

### Phase 2 — Build the Report Card

For `r1`, produce this exact output format:

```
╔══════════════════════════════════════╗
║  PIPE-01  |  etl_customers           ║
╚══════════════════════════════════════╝
  Run date   : 2026/02/09
  Start time : 06:00:00
  Duration   : 2m 7s
  Rows read  : 8,420
  Status     : SUCCESS
```

**Notes:**
- Date is reformatted to `YYYY/MM/DD` (use slicing on `run_date`) ??????????
- Duration uses `//` and `%` for minutes and seconds
- `8,420` — the thousands separator. Use `f"{rows:,}"` (this is a format specifier you weren't taught — figure it out)
- Status is uppercased for display

The box characters `╔ ║ ╚` are just text strings — copy them or type them.

Once working for r1, commit: `git add -A && git commit -m "W1D7 phase 2: r1 report card"`

---

### Phase 3 — CSV Output Line

After the report card, produce a strict CSV line for r1 that a database could ingest:

```
PIPE-01,etl_customers,2026-02-09,06:00:00,127,8420,success
```

**Rules:**
- `pipe_id`, `job_name`, `run_date`, `start_time` — as parsed (stripped, original format)
- `duration_seconds` — integer, no label
- `rows_processed` — integer, no label
- `status` — lowercase, stripped

Use `.join()` to assemble the line. Remember `str()` for integers.

Commit: `git add -A && git commit -m "W1D7 phase 3: r1 csv output"`

---

### Phase 4 — All Four Records

Repeat the full parse + report card + CSV output for all 4 records.

**r4 is the hardest** — it has no spaces around delimiters. Your strip calls handle it, but verify.

Print a separator between records:

```
──────────────────────────────────────────
```

Commit after each record passes: `git add -A && git commit -m "W1D7 phase 4: all 4 records parsed"`

---

### Phase 5 — Global Summary Block

After all 4 report cards and CSV lines, print this summary:

```
══════════════════════════════════════════
  NIGHTLY RUN SUMMARY — 2026-02-09
══════════════════════════════════════════
  Total pipelines : 4
  Total rows read : 120,864
  Total duration  : 4,157s  (69m 17s)
  Statuses        : SUCCESS SUCCESS WARN FAILED
══════════════════════════════════════════
```

**How to compute:**
- `total_rows` = sum of all 4 `rows_processed` values (just add them: `r1_rows + r2_rows + ...`)
- `total_duration` = sum of all 4 `duration_seconds` values
- `total_minutes` and `total_leftover_seconds` from total_duration using `//` and `%`
- The `Statuses` line = uppercased statuses joined by spaces — use `.join()`
- Date is taken from any record’s `run_date` (all are the same)

Commit: `git add -A && git commit -m "W1D7 phase 5: global summary complete"`

---

### Phase 6 — Hardening (Challenge)

Answer the following questions **in code comments** in your script. Don’t just guess — think through each one carefully based on what you know:

1. **r4’s `job_name`** — after splitting and stripping, is there a risk of extra internal spaces? How would you check?
2. **The `rows_label` double-split** — what happens if someone sends `rows_processed=8420` instead of `rows=8420`? Does your code still work? What breaks?
3. **Silent failure** — if r1’s duration field was `" abc "` instead of `" 127 "`, at what exact point does your script crash, and what error do you get?
4. **The `.find()` trap** — if you had used `s.find("rows=")` to extract the row count instead of splitting, what would happen if the field had no `"="` at all?
5. **`.join()` rebuild** — your CSV line uses `.join()`. What’s one thing that would cause it to produce wrong output without crashing?

Final commit: `git add -A && git commit -m "W1D7 mini project complete + hardening comments"`'''