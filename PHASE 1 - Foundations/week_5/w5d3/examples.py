# x = "global"

# def outer():
#     x = "enclosing"
#     def inner():
#         x = "local"
#         print("inner sees:", x)     # L: finds local
#     inner()
#     print("outer sees:", x)         # L: finds its own local x = "enclosing"

# outer()
# print("module sees:", x)            # G: finds global
# print("len is:", len)               # B: finds built-in

# count = 10

# def bad_increment():
#     count = 0 
#     count = count + 1  # assignment
#     print(count)       # just reading, right?
#     return count

# bad_increment()

# def shadow_demo():
#     list = [1, 2, 3]             # shadows the built-in `list`
#     print("my list:", list)

#     try:
#         result = list("abc")     # tries to call YOUR variable, not built-in
#         print(result)
#     except TypeError as e:
#         print("TypeError:", e)

# shadow_demo()

#Safe version: rename the variable
# def no_shadow():
#     items = [1, 2, 3]
#     result = list((4, 5, 6))         # built-in `list` works fine
#     print("items:", items, "result:", result)

# no_shadow()

# counter = 0

# def increment():
#     global counter
#     counter = counter + 1

# increment()
# increment()
# print("counter:", counter)

# Without global: UnboundLocalError
# def bad_increment():
#     counter = counter + 1        # Python thinks counter is local
#     return counter


# try:
#     bad_increment()
# except UnboundLocalError as e:
#     print("Error:", e)
# bad_increment()

# counter = 0

# def increment(counter):
    
#     counter += 1
#     return counter                            
# counter = 0
# for nr in range(4):
#     counter = increment(counter)
# print(counter)