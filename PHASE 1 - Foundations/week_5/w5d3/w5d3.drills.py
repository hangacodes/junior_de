#**A1 — Predict:** For each name, write L (local), G (global), or B (built-in):
price = 100                    # G

def total_with_tax(price):     # price here is L
    return price * 1.2

print(total_with_tax(50))      # print is B

#predict
x = 1
def f():
    x = 2
    return x
print(f(), x)       #2 1

#**A3 — Spot the bug:** Why does this crash?
total = 0
def add_to_total(n):
    global total
    total = total + n   #because is missing the global keywork and cannot use total
    return total
add_to_total(5)
print(total)

'''**B2 — Predict LEGB resolution**

Write the output before running:'''
x = "G"     #global "G"
def outer():
    x = "E"     #enclosing
    def inner():
        x = "L"     #local 
        print("inner:", x)      #when inner() is called it prints L 
    inner()     #this prints L
    print("outer:", x)      #outer prints E
outer() #prints E
print("global:", x) #global: G

#output should be G - wrong - it actually prints all of them

'''**B3 — Shadowing cleanup**

Rename the variable so the built-in `list` works again:'''
#changed the list variable to lst
lst = [1, 2, 3]
print(lst)
print(list("abc"))    # crashes!


'''### 6C) Semi-guided drill

**Nested helper with `nonlocal` — row summarizer**

Complete `mark_bad(msg)` so it updates `bad_count` and `last_error`. Count good rows too.'''
def summarize_rows(rows):
    good_count = 0
    bad_count = 0
    last_error = None

    def mark_bad(msg):
        #TODO: use nonlocal to update bad_count and last_error
        nonlocal bad_count, last_error
        bad_count += 1
        last_error = msg

    for row in rows:
        parts = row.split(",")
        if len(parts) != 2:
            mark_bad("wrong field count")
            continue

        name = parts[0].strip()
        age_str = parts[1].strip()

        try:
            age = int(age_str)
        except ValueError:
            mark_bad("age not an int")
            continue

        #TODO: count this as good
        good_count += 1
        # Hint: good_count is updated directly here in summarize_rows — you do NOT need nonlocal for it
        # Only names updated inside mark_bad (a nested function) need nonlocal

    return {"good": good_count, "bad": bad_count, "last_error": last_error}


rows = ["Ada, 36", "BadRow", "Linus, not_a_number", "Grace, 50"]
print(summarize_rows(rows))
# {'good': 2, 'bad': 2, 'last_error': 'age not an int'}