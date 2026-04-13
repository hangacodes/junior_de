print("\nPIPELINE CONFIG CARD")
print("--------------------")
project_name = "Zero to Hired Data Engineer"
source_system = "junior_de_database"
first_name = "Cristian"
day = "2"
price = 20
discounted_price = 19.99
is_discounted = True

print(project_name)
print(source_system)
print(first_name)
print(int(day))
print(price)
print(discounted_price)
print(is_discounted)
print("\n")

print("TYPES CHECK")
print("-----------")
print(type(price))
print(type(first_name))
print(type(day))
print(type(is_discounted))

rows = 120
rate = "0.95"
valid = int(rows * float(rate))
print(valid)