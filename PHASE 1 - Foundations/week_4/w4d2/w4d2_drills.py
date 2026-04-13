# d = {"red": 1, "green": 2, "blue": 3}

# for k in d:
#     print(k)

# for v in d.values():
#     print(v)

# for k, v in d.items():
#     print(f"{k}={v}")

# votes = {"A": 12, "B": 5, "C": 19}
'''# #compute and print total votes.'''
# # *Hint:* `total = 0`, then `for v in votes.values(): total = total + v`

# total = 0

# for v in votes.values():
#     total += v

# print(total)

'''# Given `scores = {"Ada": 98, "Linus": 88, "Grace": 100}`, print one line per person: `Ada scored 98`.'''
# *Hint:* Use `for name, score in scores.items():`.

# scores = {"Ada": 98, "Linus": 88, "Grace": 100}

# for k, v in scores.items():
#     print(f"{k} scored {v}")

'''# **B3) Find key with largest value**'''

# Given `temps = {"Mon": 2, "Tue": 5, "Wed": 1, "Thu": 4}`, print the day with the highest temperature.

# *Hint:* Track `best_day` and `best_temp`. Update when `t > best_temp`.


'''#RUNNING MAX ON DICT'''
# temps = {"Mon": 2, "Tue": 5, "Wed": 1, "Thu": 4}

# best_day = None
# best_temp = None

# for d, t in temps.items():
#     if best_temp is None or t > best_temp:
#         best_temp = t
#         best_day = d
# print(best_day)
# print(best_temp)

'''**C1) Receipt subtotal**

Compute subtotal = sum(price × qty) using `.items()` and unpacking.
'''

# price_by_item = {"bread": 2.5, "milk": 1.8, "eggs": 3.2}
# qty_by_item = {"bread": 2, "milk": 1, "eggs": 1}

# subtotal = 0.0
# #TODO: loop qty_by_item.items(), look up price, add price * qty to subtotal
# for item, qty in qty_by_item.items():
#     price = price_by_item[item]
#     subtotal = subtotal + price * qty

# print(f"Subtotal:{subtotal:.2f}")  # expected: 10.00

'''Print errors alphabetically by service name.'''


errors_by_service = {"api": 3, "db": 1, "worker": 7}

for k, c in sorted(errors_by_service.items()):
    print(f"{k}: {c}")
#TODO: loop sorted keys, print "service: count" for each
# expected output:
# api: 3
# db: 1
# worker: 7
