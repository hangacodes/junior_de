# #predict
# s = set([1, 2, 2, 3, 3, 3])
# print(len(s))   #3

# #What is wrong ?
# # my_set = {}  #this is a dict
# my_set = set()  
# my_set.add("hello")
# print(my_set)
# print(type(my_set))

# #predict
# a = {"Ava", "Bo"}
# b = {"Bo", "Cy"}
# print(a.intersection(b))    #Bo
# print(a.difference(b))      #Cy     - opps

# #Trace seen and result ? 
# data = ["x", "y", "x", "z", "y"]
# seen = set()
# result = []
# for d in data:
#     if d not in seen:
#         result.append(d)
#         seen.add(d)

# #seen will be x y z in random order
# #result will be x y z in a fixed order as they were seen the first time
# print(seen)
# print(result)

# #predict
# s = {"a", "b"}
# s.add("b")
# s.discard("c")
# print(len(s))       #2 , basically nothing happens

#Guided
'''### 6B) Guided Drills

**B1 — Deduplicate names + count** (`dedup_names.py`)
Given `names = ["Ava", "Ava", "Mika", "Noah", "Mika", "Zuri"]`, create a set of unique names and print the unique count.
**Hint:** `unique = set(names)` then `len(unique)`.'''

# names = ["Ava", "Ava", "Mika", "Noah", "Mika", "Zuri"]

# unique = (set(names))
# print(len(unique))

'''**B2 — Membership guard** (`membership_check.py`)
Given `allowed_ids = {101, 102, 103}` and `incoming = [101, 104, 102, 105]`, loop through incoming and print whether each id is allowed or blocked.
Then add `104` to `allowed_ids` and verify it's now allowed.
**Hint:** `if id in allowed_ids:` for the check, `.add(104)` to update.'''

# allowed_ids = {101, 102, 103}
# incoming = [101, 104, 102, 105]

# for nr in incoming:
#     if nr in allowed_ids:
#         print(f"{nr} -> allowed")
#     else:
#         print(f"{nr} -> not allowed")

# allowed_ids.add(104)
# print(104 in allowed_ids)

# '''**B3 — Set operations on real data** (`source_compare.py`)
# Given:'''
# source_a = ["a@x.com", "b@x.com", "c@x.com"]
# source_b = ["b@x.com", "d@x.com", "e@x.com"]
# '''Convert to sets, then compute and print: total reach (union), overlap (intersection), only-in-A (difference), only-in-B (difference).
# **Hint:** Remember difference is directional — compute both `a.difference(b)` and `b.difference(a)`.'''

# set_source_a = set(source_a)
# set_source_b = set(source_b)

# total_reach = set_source_a.union(set_source_b)
# overlap = set_source_a.intersection(set_source_b)
# only_a = set_source_a.difference(set_source_b)
# only_b = set_source_b.difference(set_source_a)

# print(total_reach)
# print(overlap)
# print(only_a)
# print(only_b)

'''**B4 — Dedup before counting** (`dedup_counter.py`)
Given `events = ["click", "click", "view", "click", "purchase", "view"]`, first deduplicate into a set,
then print how many unique event types exist. Then build a counter dict (W4D3 pattern) on the original list and print each event with its count.
**Hint:** The set answers “how many types?” and the counter answers “how many of each?”'''

# events = ["click", "click", "view", "click", "purchase", "view"]

# unique_events = set(events)
# print(len(unique_events))

# counter = {}

# for e in events:
#     counter[e] = counter.get(e, 0) + 1
# for count, event in counter.items():
#     print(event, "->", count)

#Semi-Guided


newsletter_signups = ["a@x.com", "b@x.com", "b@x.com", "c@x.com", "d@x.com", "d@x.com"]
purchasers = ["c@x.com", "d@x.com", "e@x.com", "e@x.com"]

set_newsletter_signups = set(newsletter_signups)
set_purchases = set(purchasers)

total_reach = set_newsletter_signups.union(set_purchases)
overlap = set_newsletter_signups.intersection(set_purchases)
singup_only = set_newsletter_signups.difference(set_purchases)
purchase_only = set_purchases.difference(set_newsletter_signups)

print(len(total_reach), total_reach)
print(len(overlap), overlap)
print(len(singup_only), singup_only)
print(len(purchase_only), purchase_only)
#TODO 1: Convert both to sets
#TODO 2: Compute total_reach (union), overlap (intersection),
#          signup_only (difference), purchase_only (difference)
#TODO 3: Print each result with its count (len)

opt_out = {"b@x.com", "nobody@x.com"}
opt_out.add("d@x.com")
opt_out.discard("nobody@x.com")
send_list = set_newsletter_signups.difference(opt_out)
print("Send list:",len(send_list), send_list)
#TODO 4: Add "d@x.com" to opt_out using .add()
#TODO 5: Remove "nobody@x.com" from opt_out using .discard()
#TODO 6: Compute send_list = signups who did NOT opt out (difference)
#TODO 7: Print send_list and its count
