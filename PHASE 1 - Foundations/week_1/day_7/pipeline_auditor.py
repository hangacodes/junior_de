#pipe_id | job_name | run_date | start_time | duration_seconds | rows_processed_label | status

#r1 = "  PIPE-01 | etl_customers | 2026-02-09 | 06:00:00 |  127 | rows=  8420 |   SUCCESS  "
#r2 = "  PIPE-02 | etl_orders    | 2026-02-09 | 06:02:15 |  203 | rows= 12450 |   SUCCESS  "
#r3 = "  PIPE-03 | etl_products  | 2026-02-09 | 06:05:38 |   45 | rows=   891 |    WARN    "
#r4 = "PIPE-04|etl_events|2026-02-09|06:06:23|  3782 | rows=99103|FAILED"

r1 = "  PIPE-01 | etl_customers | 2026-02-09 | 06:00:00 |  127 | rows=  8420 |   SUCCESS  "
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


print("\n╔══════════════════════════════════════╗")
print(f"║ {pipe_id}  |  {job_name}            ║")
print("╚══════════════════════════════════════╝")
print(f"  Run date   : {r1_year}/{r1_month}/{r1_day} ")
print(f"  Start time : {start_time}")
print(f"  Duration   : {duration_minutes}m {leftover_seconds}s")
print(f"  Rows read  : {r1_rows:,}")
print(f"  Status     : {r1_status.upper()}")

#Took me 28 minutes so far with the instructions

csv_r1 = ",".join([pipe_id, job_name, run_date, start_time, str(duration_seconds), str(r1_rows), r1_status])
print(csv_r1)

#starting Phase 4 after 32 minutes
r2 = "  PIPE-02 | etl_orders    | 2026-02-09 | 06:02:15 |  203 | rows= 12450 |   SUCCESS  "
parts2 = r2.split("|")

pipe_id2  = parts2[0].strip()
job_name2 = parts2[1].strip()
run_date2 = parts2[2].strip()
start_time2 = parts2[3].strip()
duration_seconds2 = int(parts2[4].strip())
rows_label2 = parts2[5].strip()              
status_raw2 = parts2[6].strip()

#Extracting the numeric part of rows_laber and casting it to int
numeric_rows2 = rows_label2.split("=")
r2_rows = int(numeric_rows2[1].strip())

#Normalizing status to lowercase and stripped
r2_status = status_raw2.lower().strip()

#parsing run_date into year month and day
r2_year = run_date2[:4]
r2_month = run_date2[5:7]
r2_day = run_date2[8:10]

#computing duration minutes and leftover seconds
duration_minutes2 = duration_seconds2 // 60
leftover_seconds2 = duration_seconds2 % 60
print("──────────────────────────────────────────")
print("\n╔══════════════════════════════════════╗")
print(f"║ {pipe_id2}  |  {job_name2}               ║")
print("╚══════════════════════════════════════╝")
print(f"  Run date   : {r2_year}/{r2_month}/{r2_day} ")
print(f"  Start time : {start_time2}")
print(f"  Duration   : {duration_minutes2}m {leftover_seconds2}s")
print(f"  Rows read  : {r2_rows:,}")
print(f"  Status     : {r2_status.upper()}")
csv_r2 = ",".join([pipe_id2, job_name2, run_date2, start_time2, str(duration_seconds2), str(r2_rows), r2_status])
print(csv_r2)

#Record number 3 - 40 minutes in 
r3 = "  PIPE-03 | etl_products  | 2026-02-09 | 06:05:38 |   45 | rows=   891 |    WARN    "

parts3 = r3.split("|")

pipe_id3  = parts3[0].strip()
job_name3 = parts3[1].strip()
run_date3 = parts3[2].strip()
start_time3 = parts3[3].strip()
duration_seconds3 = int(parts3[4].strip())
rows_label3 = parts3[5].strip()              
status_raw3 = parts3[6].strip()

#Extracting the numeric part of rows_laber and casting it to int
numeric_rows3 = rows_label3.split("=")
r3_rows = int(numeric_rows3[1].strip())

#Normalizing status to lowercase and stripped
r3_status = status_raw3.lower().strip()

#parsing run_date into year month and day
r3_year = run_date3[:4]
r3_month = run_date3[5:7]
r3_day = run_date3[8:10]

#computing duration minutes and leftover seconds
duration_minutes3 = duration_seconds3 // 60
leftover_seconds3 = duration_seconds3 % 60
print("──────────────────────────────────────────")
print("\n╔══════════════════════════════════════╗")
print(f"║ {pipe_id3}  |  {job_name3}             ║")
print("╚══════════════════════════════════════╝")
print(f"  Run date   : {r3_year}/{r3_month}/{r3_day} ")
print(f"  Start time : {start_time3}")
print(f"  Duration   : {duration_minutes3}m {leftover_seconds3}s")
print(f"  Rows read  : {r3_rows:,}")
print(f"  Status     : {r3_status.upper()}")
csv_r3 = ",".join([pipe_id3, job_name3, run_date3, start_time3, str(duration_seconds3), str(r3_rows), r3_status])
print(csv_r3)

r4 = "PIPE-04|etl_events|2026-02-09|06:06:23|  3782 | rows=99103|FAILED"

parts4 = r4.split("|")

pipe_id4  = parts4[0].strip()
job_name4 = parts4[1].strip()
run_date4 = parts4[2].strip()
start_time4 = parts4[3].strip()
duration_seconds4 = int(parts4[4].strip())
rows_label4 = parts4[5].strip()              
status_raw4 = parts4[6].strip()

#Extracting the numeric part of rows_laber and casting it to int
numeric_rows4 = rows_label4.split("=")
r4_rows = int(numeric_rows4[1].strip())

#Normalizing status to lowercase and stripped
r4_status = status_raw4.lower().strip()

#parsing run_date into year month and day
r4_year = run_date4[:4]
r4_month = run_date4[5:7]
r4_day = run_date4[8:10]

#computing duration minutes and leftover seconds
duration_minutes4 = duration_seconds4 // 60
leftover_seconds4 = duration_seconds4 % 60
print("──────────────────────────────────────────")
print("\n╔══════════════════════════════════════╗")
print(f"║ {pipe_id4}  |  {job_name4}               ║")
print("╚══════════════════════════════════════╝")
print(f"  Run date   : {r4_year}/{r4_month}/{r4_day} ")
print(f"  Start time : {start_time4}")
print(f"  Duration   : {duration_minutes4}m {leftover_seconds4}s")
print(f"  Rows read  : {r4_rows:,}")
print(f"  Status     : {r4_status.upper()}")
csv_r4 = ",".join([pipe_id4, job_name4, run_date4, start_time4, str(duration_seconds4), str(r4_rows), r4_status])
print(csv_r4)

#starting phase 5 after 47 minutes
total_rows = r1_rows + r2_rows + r3_rows + r4_rows
total_duration = duration_seconds + duration_seconds2 + duration_seconds3 + duration_seconds4
total_minutes =total_duration // 60
total_leftover_seconds = total_duration % 60
statuses = " ".join([r1_status.upper(), r2_status.upper(), r3_status.upper(), r4_status.upper()])

print("──────────────────────────────────────────")
print("\n══════════════════════════════════════════")
print("NIGHTLY RUN SUMMARY — 2026-02-09")
print("══════════════════════════════════════════")
print(f"Total pipelines : 4")
print(f"Total rows read : {total_rows:,}")
print(f"Total duration  : {total_duration:,}s  ({total_minutes}m {total_leftover_seconds}s)")
print(f"Statuses        : {statuses}")
print("══════════════════════════════════════════")
print("\n")
count = parts4[1].find("  ")
print(count)
'''Answer the following questions **in code comments** in your script. Don’t just guess — think through each one carefully based on what you know:

1. **r4's `job_name`** — after splitting and stripping, is there a risk of extra internal spaces? How would you check?
- I'm not sure if there is a risk of extra internal spaces, but you can check with: print(len(parts4[1])). Looks like the len is 10 but there are only 9 indexes hm ?
- So appearantly i can use parts4[1].find("  ") or parts4[1].count(" "). Why not len() ?

2. **The `rows_label` double-split** — what happens if someone sends `rows_processed=8420` instead of `rows=8420`? Does your code still work? What breaks?
- i think it should still work no? Cause I only split("=") i didn't split("_") too.
- I GOT THIS ONE RIGHT

3. **Silent failure** — if r1’s duration field was `" abc "` instead of `" 127 "`, at what exact point does your script crash, and what error do you get?
- the script would crash when i try to transform the duration field from str to int. 7th row of the code would crash, error is ValueError
- I GOT THIS ONE RIGHT

4. **The `.find()` trap** — if you had used `s.find("rows=")` to extract the row count instead of splitting, what would happen if the field had no `"="` at all?
- i would receive -1 after find
-I GOT THIS ONE RIGHT


5. **`.join()` rebuild** — your CSV line uses `.join()`. What’s one thing that would cause it to produce wrong output without crashing?
- i have no ideea....
- I didn't know that - If any element is not a str (e.g., an int left un-converted), .join() raises TypeError. 
- If an element has embedded commas, the CSV structure breaks silently — extra columns appear downstream.'''

# I finished everything in 1 hour in 10 minutes
