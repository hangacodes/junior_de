raw = ["  $12 ", "FREE", " $7", "N/A", "  $100  ", "$0", " $5 "]
#Comprehension
prices_comp = [int(s.strip()[1:]) for s in raw if s.strip().startswith("$")]

#Loop
prices_loop = []

for price in raw:
    t= price.strip()
    if t.startswith("$"):
        prices_loop.append(int(t[1:]))

#Non-zero
nonzero_prices = [price for price in prices_comp if price > 0]

#Discounted:

discounted = [int(p * 0.9) for p in nonzero_prices]

print(f"Comprehension prices: {prices_comp}")
print(f"Loop prices: {prices_loop}")
print(f"Non-zero prices: {nonzero_prices}")
print(f"Discounted prices: {discounted}")

'''
Honestly here the loop prices are way more readable.
I had to peak at the answer key to see how to do the loop prices,
but using a temporary variable was useful in the loop
'''