'''**Scenario:** Normalize 4 messy field names into clean, consistent snake_case format and print a diagnostic report for each.

**Requirements:**

1. For each field: strip → lower → replace `"-"` with `"_"` → replace `" "` with `"_"` → replace `"__"` with `"_"` (run once).
2. Print the cleaned value.
3. Print diagnostics: underscore count, whether it ends with `"_id"` or `".csv"`, and the index of `"events"` (even if `1`).

**What Could Go Wrong?** Answer in comments: (1) What if a field has triple underscores `"___"`? Does one pass of `replace("__", "_")` fix it completely? (2) What would you need to do instead?

You'll write similar cleanup blocks 4 times here. In Week 3, you'll handle this with a `for` loop over a list in ~5 lines. For now, notice the repetition 
— that recognition is exactly what will make loops feel natural when you get there.'''

#Input fields:

raw1 = "   User ID   "
raw2 = "Email-Address"
raw3 = "  RAW__Events-2026.CSV  "
raw4 = "Account  Status"

clean_raw1 = raw1.strip().lower().replace("-","_").replace(" ","_").replace("__","_")
clean_raw2 = raw2.strip().lower().replace("-","_").replace(" ","_").replace("__","_")
clean_raw3 = raw3.strip().lower().replace("-","_").replace(" ","_").replace("__","_")
clean_raw4 = raw4.strip().lower().replace("-","_").replace(" ","_").replace("__","_")

print("===CLEANED===")
print(clean_raw1)
print(clean_raw2)
print(clean_raw3)
print(clean_raw4)

print("\n=== DIAGNOSTICS ===")

print("\n---Clean raw1---")
print(f"Underscore count: {clean_raw1.count("_")}")
print(f"Ends with '_id': {clean_raw1.endswith("_id")}")
print(f"Ends with '_id': {clean_raw1.endswith(".csv")}")

print("\n---Clean raw2---")
print(f"Underscore count: {clean_raw2.count("_")}")
print(f"Ends with '_id': {clean_raw2.endswith("_id")}")
print(f"Ends with '_id': {clean_raw2.endswith(".csv")}")

print("\n---Clean raw3---")
print(f"Underscore count: {clean_raw3.count("_")}")
print(f"Ends with '_id': {clean_raw3.endswith("_id")}")
print(f"Ends with '_id': {clean_raw3.endswith(".csv")}")

print("\n---Clean raw4---")
print(f"Underscore count: {clean_raw4.count("_")}")
print(f"Ends with '_id': {clean_raw4.endswith("_id")}")
print(f"Ends with '_id': {clean_raw4.endswith(".csv")}")

#Finished and I think it looks pretty good. I did not check the solution yet.

#Looks like the solution provided by the lesson is way shorter, I tried to make it look good, not sure which one is considered better or wrong.

#Attaching the solution from the lesson below.

#Is my deliverable not good enough? Is it too long? Should I adopt the other way, of writing everything very concised?
'''
raw1 = "   User ID   "
raw2 = "Email-Address"
raw3 = "  RAW__Events-2026.CSV  "
raw4 = "Account  Status"

# This repeats 4x — for loops (Week 3) will collapse this to ~6 lines.
c1 = raw1.strip().lower().replace("-", "_").replace(" ", "_").replace("__", "_")
c2 = raw2.strip().lower().replace("-", "_").replace(" ", "_").replace("__", "_")
c3 = raw3.strip().lower().replace("-", "_").replace(" ", "_").replace("__", "_")
c4 = raw4.strip().lower().replace("-", "_").replace(" ", "_").replace("__", "_")

print("---- CLEANED ----")
print(c1)
print(c2)
print(c3)
print(c4)

print("---- DIAGNOSTICS ----")
print(f"{c1}: underscores={c1.count('_')}, ends_id={c1.endswith('_id')}, events_at={c1.find('events')}")
print(f"{c2}: underscores={c2.count('_')}, ends_id={c2.endswith('_id')}, events_at={c2.find('events')}")
print(f"{c3}: underscores={c3.count('_')}, ends_csv={c3.endswith('.csv')}, events_at={c3.find('events')}")
print(f"{c4}: underscores={c4.count('_')}, ends_id={c4.endswith('_id')}, events_at={c4.find('events')}")

# What Could Go Wrong?
# 1) Triple underscores "___" become "__" after one replace("__","_") pass —
#    still not clean. You'd need to run the replace again or use a different strategy.
# 2) A second pass of replace("__","_") would fix it, but deeply nested
#    underscores (e.g., "____") might need even more passes. A loop would solve
#    this properly (coming in Week 3).
'''

