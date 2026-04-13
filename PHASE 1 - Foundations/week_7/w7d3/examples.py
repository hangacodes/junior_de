# # Problem: input lines may or may not have \n already
# lines = ["apple\n", "banana", "cherry\n\n"]

# # BAD: blindly adding \n creates double newlines
# with open("week_7/w7d3/bad_nl.txt", "w", encoding="utf-8") as f:
#     for line in lines:
#         f.write(line + "\n")

# with open("week_7/w7d3/bad_nl.txt", "r", encoding="utf-8") as f:
#     print("BAD (blank lines):")
#     print(f.read())
#     print(repr(f.read()))
# # output: BAD (blank lines):
# # 'apple\n\nbanana\n\ncherry\n\n'

# # GOOD: normalize first
# with open("week_7/w7d3/good_nl.txt", "w", encoding="utf-8") as f:
#     for line in lines:
#         f.write(line.rstrip("\n") + "\n")

# with open("week_7/w7d3/good_nl.txt", "r", encoding="utf-8") as f:
#     print("GOOD (clean):")
#     print(f.read())
#     print(repr(f.read()))
# # output: GOOD (clean):
# # 'apple\nbanana\ncherry\n'

import time

with open("week_7/w7d3/buffer_demo.txt", "w", encoding="utf-8") as f:
    f.write("Step 1 complete\n")
    f.flush()          # force to disk right now
    time.sleep(3)      # pause 3 seconds — open the file during this pause
    f.write("Step 2 complete\n")
    # Step 2 is NOT flushed yet — still in buffer
# with block ends → Step 2 flushed automatically


with open("week_7/w7d3/buffer_demo.txt", "r", encoding="utf-8") as f:
    print(f.read())
# output:
# Step 1 complete
# Step 2 complete
