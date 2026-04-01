# def total_positive(nums):
#     total = 0
#     for n in nums:
#         print(f"  DEBUG: n={n}, total_before={total}")   # ← decision point: loop body
#         if n > 0:
#             total = total + n
#     print(f"  DEBUG: final total={total}")                # ← before return
#     return total

# result = total_positive([5, -2, 10, -1, 3])
# print("Result:", result)

# def get_domain(email):
#     parts = email.split("@")
#     breakpoint()                    # program pauses HERE
#     return parts[1].lower()         # this is the suspicious line

# get_domain("no-at-sign")

import logging
logging.basicConfig(level=logging.INFO)

def load_records(rows):
    logging.info("Starting load. Input count:%s", len(rows))
    kept = []
    for row in rows:
        if row.get("id", "") != "":
            kept.append(row)
    logging.info("Load complete. Kept:%s of%s", len(kept), len(rows))
    return kept

data = [{"id": "A1"}, {"id": ""}, {"name": "no_id"} ]
load_records(data)
# output: INFO:root:Starting load. Input count: 3
# output: INFO:root:Load complete. Kept: 1 of 3

