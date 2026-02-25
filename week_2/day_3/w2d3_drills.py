#Guided drills 

print("\nDrill 1: Temperature labeler")
temp_c = 18

if temp_c <= 0:
    print("freezing")
elif temp_c <= 10:
    print("cold")
else:
    print("warm")

print("\nDrill 2: Range checker")
value = 100

if value >= 10 and value <= 100:
    print("IN RANGE")
else:
    print("OUT OF RANGE")

print("\nDrill 3: Basic record check")

raw_name = "   Ada.  "
raw_age = 200
clean_name = raw_name.strip()
if clean_name == "":
    print("BAD NAME")
elif raw_age < 0 or raw_age > 120:
    print("BAD AGE")
else:
    print("OK")

#Semi Guided Drills:

print("\nSemi-guided 1: Status normalizer")
#Fill the ??? 

status = "  OK  "

clean = status.strip().lower()

if clean == "ok":
    print("ok")
elif clean == "fail":
    print("fail")
else:
    print("unknown")


print("\nSemi-guided 2: Shipping rule")
#Fill in the condition for free shipping:

country = "DE"
order_total = 49

if country == "DE" and order_total >=50:
    print("FREE SHIPPING")
else:
    print("PAID SHIPPING")
