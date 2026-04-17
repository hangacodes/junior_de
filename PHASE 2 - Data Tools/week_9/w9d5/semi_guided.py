import pandas as pd

tickets = pd.DataFrame({
    "Event Name": ["  CONCERT A ", "Festival B", " concert A"],
    "Ticket Price": ["$45.00", "$120.00", "$45.00"],
    "Qty Sold": ["150", "80", "200"],
    "Service Fee": ["5%", "8%", "5%"],
    "Internal Ref": ["REF001", "REF002", "REF003"],
})


#TODO 1: Print df.columns.tolist() and df.head() to see what you have.
print(tickets.columns.tolist())
#TODO 2: Rename all columns to snake_case.
tickets = tickets.rename(columns={"Event Name": "event_name", "Ticket Price":"ticket_price", "Qty Sold":"qty_sold", "Service Fee":"service_fee", "Internal Ref":"internal_ref"})
print(tickets.columns.tolist())
#TODO 3: Clean event_name: strip + lower.

tickets["event_name"] = tickets["event_name"].str.strip().str.lower()
print(tickets)
#TODO 4: Convert ticket_price to float (remove $), qty_sold to int,
#   service_fee to float fraction (remove %, divide by 100).
tickets["ticket_price"] = tickets["ticket_price"].str.replace("$", "", regex=False).astype(float)
tickets["qty_sold"] = tickets["qty_sold"].astype(int)
tickets["service_fee"] = tickets["service_fee"].str.replace("%" ,"",regex=False).astype(float) / 100
print(tickets)
#TODO 5: Add gross_revenue, fee_amount, net_revenue.

tickets["gross_revenue"] = tickets["ticket_price"] * tickets["qty_sold"]
tickets["fee_amount"] = tickets["qty_sold"] * tickets["service_fee"]
tickets["net_revenue"] = tickets["gross_revenue"] - tickets["fee_amount"]
print(tickets)


#TODO 6: Drop internal_ref. Print final columns and DataFrame.
tickets =tickets.drop(columns=["internal_ref"])
print(tickets.columns.tolist())
print(tickets)

#TODO 7: Sort by net_revenue descending (W9D4). Print top result.

sorted = tickets.sort_values(by="net_revenue", ascending=False)
print(sorted)
print(sorted.head(1))