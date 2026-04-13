import pandas as pd
# '''**A1 — Predict:** What does `pd.DataFrame({"x": [1, 2], "y": [10, 20]}).shape` return? Write your answer, then run it.'''


# print(pd.DataFrame({"x": [1, 2], "y": [10, 20]}).shape)
# #It will print (2,2)

# '''**A2 — Trace:** After running this code, what type is `result`? What values does it contain?'''

# df = pd.DataFrame({"a": [5, 10, 15], "b": ["x", "y", "z"]})
# result = df["b"]
# print(result)

# '''**A3 — Spot:** This code raises an error. What is the error type and which line causes it?'''
# data = {"name": ["Ava", "Bo", "Cal"], "score": [88, 72]}
# df = pd.DataFrame(data)
# #Value error because the lenght of the lists are not the same

'''**A4 — Predict:** What does this print? Focus on what appears on the far-left.'''
s = pd.Series([100, 200], index=["first", "second"])
print(s)