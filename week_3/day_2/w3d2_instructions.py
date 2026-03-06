'''**Scenario:** You’re given a list of CSV-like rows representing sensor readings. Each row should have the format `sensor_id,temp_c,status`.

**Requirements:**

1. Loop over the rows using `enumerate()` (you need both index and row)
2. Validate each row: must have exactly 3 comma-separated fields, `temp_c` must convert to `float`, `status` must be one of `"OK"`, `"WARN"`, `"FAIL"`
3. Build `valid_rows` and `invalid_rows` lists
4. Track three counters: `bad_field_count`, `bad_temp_count`, `bad_status_count`
5. Print a summary: total rows, valid count, invalid count, counts by failure reason
6. Print invalid rows with their original index'''

'''**Data:**

```python
rows = [
    "s-1,21.5,OK",
    "s-2,not_a_float,OK",
    "s-3,19.0,BAD",
    "s-4,18.2,WARN",
    "broken_row",
    "s-5,17.1,FAIL"
]
```'''