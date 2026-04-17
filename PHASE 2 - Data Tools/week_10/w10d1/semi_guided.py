import pandas as pd

def clean_orders(df):
    """
    Clean an orders DataFrame:
    - Compute before-snapshot (rows, null rates)
    - customer_id is required → drop missing
    - country → fill with "UNKNOWN"
    - notes → fill with ""
    - Compute after-snapshot
    - Return (cleaned_df, report_dict)
    """
    report = {}
    df = df.copy()

    #TODO: record rows_before in report
    #TODO: compute null_rate for customer_id before cleaning, store in report
    report["rows_before"] = len(df)
    
    rate = sum(df["customer_id"].isna()) / len(df)
    report["customer_id_null_rate"] = rate

    #TODO: drop rows where customer_id is missing
    #   Hint: df = df[df["customer_id"].notna()]
    df = df[df["customer_id"].notna()]
    #TODO: fill country with "UNKNOWN"
    df["country"] = df["country"].fillna("UNKNOWN")
    #TODO: fill notes with ""
    df["notes"] = df["notes"].fillna("")

    #TODO: record rows_after in report
    report["rows_after"] = len(df)
    #TODO: compute null_rate for customer_id after cleaning, store in report
    report["rate_after_cleaning"] = sum(df["customer_id"].isna()) / len(df)


    return df, report

# Test data
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "customer_id": [10, None, 12, None, 14],
    "country": ["FI", "FI", None, "SE", None],
    "notes": [None, None, "rush", None, "gift"]
})

cleaned, report = clean_orders(orders)
print(cleaned)
print(report)