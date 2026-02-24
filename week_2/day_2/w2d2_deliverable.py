#Write a script that evaluates **three scenarios** of a “nightly data load” using these rules:

#scenario 1:
source_reachable1 = True
schema_valid1 = True
manual_override1 = False
rows_estimate1 = 900
max_rows1 = 1000
rows_processed1 = 300000
run_seconds1 = 250

#scenario 2:
source_reachable2 = False
schema_valid2 = True
manual_override2 = True
rows_estimate2 = 5000
max_rows2 = 1000
rows_processed2 = 0
run_seconds2 = 0

#scenario 3:
source_reachable3 = True
schema_valid3 = False
manual_override3 = False
rows_estimate3 = 800
max_rows3 = 1000
rows_processed3 = 120000
run_seconds3 = 90

#Rules:
#Scenario 1:
can_start_load1 = source_reachable1 and schema_valid1 and ((rows_estimate1 <= max_rows1) or manual_override1)
should_alert1 = (not source_reachable1) or (not schema_valid1)
throughput_ok1 = (run_seconds1 != 0) and (rows_processed1 / run_seconds1 >= 1000)
#Scenario 2:
can_start_load2 = source_reachable2 and schema_valid2 and ((rows_estimate2 <= max_rows2) or manual_override2)
should_alert2 = (not source_reachable2) or (not schema_valid2)
throughput_ok2 = (run_seconds2 != 0) and (rows_processed2 / run_seconds2 >= 1000)
#Scenario 3:
can_start_load3 = source_reachable3 and schema_valid3 and ((rows_estimate3 <= max_rows3) or manual_override3)
should_alert3 = (not source_reachable3) or (not schema_valid3)
throughput_ok3 = (run_seconds3 != 0) and (rows_processed3 / run_seconds3 >= 1000)

#output:
print(f"Scenario 1 -> can_start_load={can_start_load1}, should_alert={should_alert1}, throughout_ok={throughput_ok1}")
print(f"Scenario 2 -> can_start_load={can_start_load2}, should_alert={should_alert2}, throughout_ok={throughput_ok2}")
print(f"Scenario 3 -> can_start_load={can_start_load3}, should_alert={should_alert3}, throughout_ok={throughput_ok3}")

#Looks good to me, it works just like the solution in the answer key. 