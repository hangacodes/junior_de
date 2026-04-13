import pandas as pd

# people = [
#     {"name": "Aino", "age": 20, "city": "Helsinki"},
#     {"name": "Chris", "age": 30, "city": "Oradea"},
#     {"name": "Dennis", "age": 25, "city": "Budapest"}
# ]

# df = pd.DataFrame(people)
# print(df)



# temps = pd.Series([18.2, 21.5, 15.8], index=["Mon", "Tue", "Wed"])
# print(temps)
# # output:
# # Mon    18.2
# # Tue    21.5
# # Wed    15.8
# # dtype: float64

# print(type(temps))
# # <class 'pandas.core.series.Series'>
# print("\n")


# data = {"product": ["coffee", "tea"], "price": [4.5, 3.0]}
# df = pd.DataFrame(data, index=["sku_100", "sku_101"])
# print(df)
# # output:
# #         product  price
# # sku_100  coffee    4.5
# # sku_101     tea    3.0


# print("\n")
# print("\n")

# # Row-first: each dict = one row
# rows = [{"item": "bolt", "qty": 50, "mouse":1}, {"item":"beer", "mouse": "nut", "qty": 120}]
# df_rows = pd.DataFrame(rows)
# print(df_rows)
# # output:
# #    item  qty
# # 0  bolt   50
# # 1   nut  120

# # Column-first: each key = one column
# cols = {"item": ["bolt", "nut"], "qty": [50, 120]}
# df_cols = pd.DataFrame(cols)
# print(df_cols)
# # output:
# #    item  qty
# # 0  bolt   50
# # 1   nut  120




# df = pd.DataFrame({
#     "sensor": ["S1", "S2", "S3"],
#     "reading": [22.1, 18.7, 25.3],
#     "active": [True, False, True],
# })
# print("shape:", df.shape)       # (3, 3)
# print(df.head(2))               # first 2 rows
# print(df.dtypes)                # sensor: object, reading: float64, active: bool



# # df = pd.DataFrame({"x": [1, 2]})
# # print(df.shape())
# # # TypeError: 'tuple' object is not callable


#Step 1: You have raw Python data
peoples1 = [{"name": "Aino", "age": 29, "city":"Oradea"}, {"name": "Mikko", "age": 34}]

#Step 2: Wrap it in pd.DataFrame()
dataframe = pd.DataFrame(peoples1)

#Step 3: Inspect immediately
print(dataframe.shape)   
print(dataframe.head()) 
print(dataframe.dtypes)
        

#Step 4: Now you're safe to work with it