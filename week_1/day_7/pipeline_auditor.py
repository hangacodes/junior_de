#pipe_id | job_name | run_date | start_time | duration_seconds | rows_processed_label | status

r1 = "  PIPE-01 | etl_customers | 2026-02-09 | 06:00:00 |  127 | rows=  8420 |   SUCCESS  "
r2 = "  PIPE-02 | etl_orders    | 2026-02-09 | 06:02:15 |  203 | rows= 12450 |   SUCCESS  "
r3 = "  PIPE-03 | etl_products  | 2026-02-09 | 06:05:38 |   45 | rows=   891 |    WARN    "
r4 = "PIPE-04|etl_events|2026-02-09|06:06:23|  3782 | rows=99103|FAILED"

parts = r1.split("|")

pipe_id  = parts[0].strip()
job_name = parts[1].strip()
run_date = parts[2].strip()
start_time = parts[3].strip()
duration_seconds = int(parts[4].strip())
rows_label = parts[5].strip()              # "rows=  8420"
status_raw = parts[6].strip()

#Extracting the numeric part of rows_laber and casting it to int
numeric_rows = rows_label.split("=")
r1_rows = int(numeric_rows[1].strip())

#Normalizing status to lowercase and stripped
r1_status = status_raw.lower().strip()

#parsing run_date into year month and day
r1_year = run_date[:4]
r1_month = run_date[5:7]
r1_day = run_date[8:10]

#computing duration minutes and leftover seconds
duration_minutes = duration_seconds // 60
leftover_seconds = duration_seconds % 60

#printing r1's full parsed values to confirm they're correct
print(r1_rows)
print(type(r1_rows))

print(r1_status)

print(r1_year)
print(r1_month)
print(r1_day)

print(duration_minutes)
print(leftover_seconds)
