#activation
'''x = [10,20,30]
x.append(40)
print(x[0])
print(len(x))'''

'''items = ["a", "b", "c"]
result = items.pop(1)
print(result)'''

'''cols = ["id", "email"]
cols = cols.append("created_at") 
print(cols) # .append() returns none'''


#Guided
#B1)

'''cols = ["id", "email"]
cols.append("country")
print(cols)
'''
#b2
'''cols = ["email", "created_at"]
cols.insert(0, "id")
print(cols)'''

#b3
'''items = ["raw","staging","final"]
removed = items.pop(1)
print(removed)
print(items)'''

#b4
'''flags = ["fast", "verbose", "debug"]
if "debug" in flags:
    flags.remove("debug")
    print("Flag found: 'debug' removed")
else:
    print("'debug' flag not found")
print(flags)'''


#Semi Guided drills
'''cols = ["id", "emailAddress", "created_at"]

#TODO: change the second element to "email"
#TODO: print cols
cols[1] = "email"

print(cols)'''

'''actions = ["start"]

#TODO: append "added_column"
#TODO: pop the last action into last_action
#TODO: print last_action and actions

actions.append("added_column")
last_action = actions.pop()

print(actions)
print(last_action)'''