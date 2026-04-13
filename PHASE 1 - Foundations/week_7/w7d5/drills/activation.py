# '''**A1 (Predict):** What Python type does `json.loads('{"x": 10}')` return?'''

# #Dictionary

# '''**A2 (Predict):** What does `json.dumps({"active": True})` produce — does it say `True` or `true`?'''

# #it produces a string, and it says 'true' not True - because it became JSON

# # '''**A3 (Spot):** This code crashes. Why?'''
# import json

# with open("week+7/w7d5/drills/data.json", "r") as f:
#     data = json.loads(f)        #FileNotFoundError ...we don't have a data.json file yet
#     #but more importantly , json.loads takes a string
#     #the function should be json.load(f) without "s"


# '''**A4 (Trace):** Given `data = {"a": [10, 20, 30]}`, what does `data["a"][2]` return?'''
# data = {"a": [10, 20, 30]}      
# #returns 30

# print(data["a"][2])