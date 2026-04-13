newsletter_signups = ["a@x.com", "b@x.com", "b@x.com", "c@x.com", "d@x.com", "d@x.com"]
purchasers = ["c@x.com", "d@x.com", "e@x.com", "e@x.com"]
opt_out = {"b@x.com", "nobody@x.com"}

signups_set = set(newsletter_signups)
purchasers_set = set(purchasers)

total_reach = signups_set.union(purchasers)
overlap = signups_set.intersection(purchasers)
signup_only = signups_set.difference(purchasers)
purchase_only = purchasers_set.difference(signups_set)

opt_out.add("d@x.com")
opt_out.discard("nobody@x.com")

send_list = signups_set.difference(opt_out)


print("Total reach:", total_reach, "count:", len(total_reach))
print(f"Overlap: {overlap}, count: {len(overlap)}")
print(f"Signup only: {signup_only}, count: {len(signup_only)}")
print(f"Purchase only: {purchase_only}, count: {len(purchase_only)}")
print(f"Opted out: {opt_out}, count: {len(opt_out)}")
print(f"Sending to: {send_list}, count: {len(send_list)}")
