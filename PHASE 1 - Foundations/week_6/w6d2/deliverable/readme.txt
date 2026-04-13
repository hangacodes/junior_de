### 6D) Primary Deliverable (60–75 min)

**Scenario:** Build a `scorecard` package for tracking game scores —
with separate modules for parsing and formatting — plus a runner script that uses all import forms.

**Create this structure:**

```
project/
  run_scorecard.py
  scorecard/
    __init__.py
    parsing.py
    display.py
```

**Requirements:**

1. `scorecard/parsing.py` must contain:
    - `parse_result(line)` → takes `"PlayerName:score"`, returns `{"player": "...", "score": int}`. Strip and title-case the player name.
    - `filter_above(results, threshold=50)` → returns list of results with score above threshold (default parameter from W5D4).
    - `rank_results(results)` →
       returns a new list sorted by score descending.
       Use a loop to build it (manual insertion sort or build + sort with `sorted()` and a key — `sorted()` is a built-in available since W3D4).
2. `scorecard/display.py` must contain:
    - `format_header(title)` → returns `"=== " + title + " ==="`.
    - `format_result(result, position)` → returns `"#1 PlayerName: 88 pts"` format.
    - `format_summary(results)` → returns a string with count and average score.
3. `run_scorecard.py` must:
    - Use `from scorecard.parsing import parse_result` (selective import)
    - Use `import scorecard.parsing as sp` (aliased module import for other functions)
    - Use `from scorecard.display import format_header, format_result, format_summary` (multi-name import)
    - Process at least 6 raw score lines (include messy spacing)
    - Print a formatted leaderboard with rankings
4. Both module files must include `if __name__ == "__main__":` guards with test code.
5. No side effects on import — the package must be silent when imported.

**What Could Go Wrong?** What happens if a score line has no colon separator
(e.g., `"BadLine"`)? Which function breaks, and what error type? (Answer in a code comment.)