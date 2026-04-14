import json
import pandas as pd

csv_text = (
    "book_id,title,genre,pages,checked_out\n"
    "0001,The Martian,sci-fi,369,yes\n"
    "0012,Dune,sci-fi,412,no\n"
    "0023,Sapiens,non-fiction,443,yes\n"
    "0034,Atomic Habits,self-help,320,?\n"
    "0045,The Road,fiction,287,no\n"
)

with open("week_9/w9d2/library_loader/books.csv", "w", encoding="utf-8") as f:
    f.write(csv_text)

members = [
    {"member_id": "M001", "name": "Ava", "books_borrowed": 3},
    {"member_id": "M002", "name": "Bo", "books_borrowed": 0},
    {"member_id": "M003", "name": "Cal", "books_borrowed": 7},
    {"member_id": "M004", "name": "Dan", "books_borrowed": 1},
]

with open("week_9/w9d2/library_loader/members.json", "w", encoding="utf-8") as f:
    json.dump(members, f, indent=2)


def load_csv_safely(path, dtype_map=None, na_tokens=None, sep=",", has_header=True, names=None):
    if has_header:

        df = pd.read_csv(
            path,
            sep=sep,
            dtype=dtype_map,
            na_values=na_tokens
        )
    else: df= pd.read_csv(
        path,
        sep=sep,
        dtype=dtype_map,
        na_values=na_tokens,
        header=None,
        names=names)
    print("---Trust report---")
    print(f"{path}")
    print("Shape:", df.shape)
    print("Head:\n")
    print(df.head())
    print(df.dtypes)
    return df

mybooks = load_csv_safely("week_9/w9d2/library_loader/books.csv", dtype_map={"book_id":str}, na_tokens=["?"])

mymembers = pd.read_json("week_9/w9d2/library_loader/members.json")
print("Members shape:", mymembers.shape)
print("Head:")
print(mymembers.head())
print(mymembers.dtypes)


#If I don't mention "N/A" in na_values, and one of my pages rows would have it,
#pages would become float64, not - str, because N/A is already built-in to be recognised as na_value
#if it would be anything else ( like ! or - ) pages would become str


