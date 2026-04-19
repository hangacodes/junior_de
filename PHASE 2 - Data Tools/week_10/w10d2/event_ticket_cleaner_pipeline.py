import pandas as pd

tickets = pd.DataFrame({
    "event_id": [201, 201, 202, 203, 203, 204],
    "venue": [" Madison Sq.  Garden ", "madison sq. garden", " MSG ", "  The   Forum  ", "the forum", " Wembley "],
    "ticket_price": ["$150", "$155", "COMP", "$75", "$80", "$2,500"],
    "updated_at": ["2026-03-01", "2026-03-05", "2026-03-02", "2026-03-01", "2026-03-04", "2026-03-01"]
})
def validation_report(df):
    report = {}
    df = df.copy()
    #reporting rows and venue before doing any changes
    report["rows_before"] = len(df)
    report["unique_venues_raw"] = df["venue"].nunique()

    #adding creating vanue_canon and adding it to the new length to the report
    df["venue_canon"] = df["venue"].str.strip().str.lower().str.replace(".", " ", regex=False).str.replace(r"\s+", " ", regex=True)
    

    #deduplicating event_id after sorting
    df = df.sort_values(["updated_at"]).drop_duplicates(subset=["event_id"], keep="last")
    report["unique_venues_canon"] = df["venue_canon"].nunique()
    #converting to int and tracking failures
    df["ticket_price"] = df["ticket_price"].str.replace("$", "", regex=False).str.replace(",", "", regex=False)
    nums = []
    failures = 0
    for n in df["ticket_price"]:
        try:
            nums.append(int(n))
        except ValueError:
            nums.append(None)
            failures += 1
    df["ticket_price"] = nums

    #recording rows after changes
    report["rows_after"] = len(df)
    report["price_null_rate"] = (f"{sum(df['ticket_price'].isna()) / len(df) * 100:.1f}%")
    report["price_failures"] = failures
    return df, report

df , report = validation_report(tickets)

print(df)
print(report)

'''**What Could Go Wrong:** 
A new vendor sends prices in euros (`"€80"`) — your `str.replace("$", ...)` won't catch it.
What validation would detect this? How would you modify the pipeline?'''

#I would check for non-digit chars after cleaning and then add the € replacement
# - so this answer was not ok appearantly 
'''What Ai said it should look like : '''

# What Could Go Wrong:
# If a vendor sends "€80", str.replace("$", ...) won't catch the euro sign.
# Detection: after cleaning, check for any non-digit characters remaining:
#   bad_chars = cleaned_price.str.contains(r"[^0-9]", regex=True, na=False)
#   if bad_chars.any(): print("WARNING: unexpected characters in price")
# Fix: extend the replace chain to handle multiple currency symbols,
# or flag the new symbol in the failure count and investigate.

'''What the answer key was in the lesson:'''
# What Could Go Wrong:
# If a vendor sends "€80", str.replace("$", ...) won't catch the euro sign.
# Detection: after cleaning, check for any non-digit characters remaining:
#   bad_chars = cleaned_price.str.contains(r"[^0-9]", regex=True, na=False)
#   if bad_chars.any(): print("WARNING: unexpected characters in price")
# Fix: extend the replace chain to handle multiple currency symbols,
# or flag the new symbol in the failure count and investigate.

#I will come back and check more on this in the future