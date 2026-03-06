'''#List comprehensions

#transform only
nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [n * n for n in nums]
print(squares)

#Filter only: keep evens
evens = [n for n in nums if n % 2 ==0]
print(evens)

#Transform + filter:  square the evens

even_squares = [n * n for n in nums if n % 2 == 0]
print(even_squares)'''

'''words = [" a ",  "b ", "    c", "d"]
clean = [ w.strip() for w in words ]
print(words)
print(clean)


bad = [print(n) for n in [1,2,3]]
print(bad)


'''

#Classic map pattern
'''nums = [ 1, 2, 3, 4]
squares = [ n * n for n in nums]
print(squares)
'''

#Filter + transform with string methods
'''raw = ["  $12 ", "FREE", " $7", "N/A", "  $100  ", "$0"]

prices = [int(s.strip()[1:]) for s in raw if s.strip().startswith("$")]
print(prices)       #SHOULDN't THIS BE A LOOP RATHER THAN THAT ?'''

#Using enumerate() in a comprehension
'''names = ["Ada", "Linus", "Grace"]

labeled= [f"{pair[0]}:{pair[1]}" for pair in enumerate(names)]
print(labeled)
'''

#The side-effect trap
'''nums = [10, 20, 30]
result = [print(n) for n in nums]
print("result =", result)'''

#Drill ladder:
#**A1 — Predict:** What does this comprehension produce?

'''nums = [1, 2, 3, 4]
out = [n + 10 for n in nums]
print(out)      # 11, 12, 13, 14 - good'''

#**A2 — Convert:** Turn this loop into a comprehension:
'''words = [" a ", " b  ", "c"]
clean = []
for w in words:
    clean.append(w.strip())
print(clean)'''

'''words = [" a ", " b  ", "c"]
clean = [w.strip() for w in words]
print(clean)'''

#**A3 — Predict:** What does this produce?
'''nums = [1, 2, 3, 4, 5]
result = [n for n in nums if n > 3]
print(result)   #should produce [4, 5]'''


#Guided Practice
'''
**B1) Lengths:** Build a list of word lengths from `words = ["data", "engineer", "etl"]`. Expected: `[4, 8, 3]`.

*Hint:* Expression is `len(w)`.

'''
'''words = ["data", "engineer", "etl"]

lenghts = [len(w) for w in words]
print(lenghts)
'''

'''
**B2) Filter big numbers:** Keep only numbers > 5 from `nums = [2, 7, 1, 9, 5, 6]`. Expected: `[7, 9, 6]`.

*Hint:* Predicate is `n > 5`.'''
'''nums = [2, 7, 1, 9, 5, 6]

big_numbers = [ n for n in nums if n > 5]
print(big_numbers)'''


'''**B3) Hash tags:** From `tags = ["#sql", "python", "#etl", "data"]`, keep only strings starting with `"#"`. Expected: `["#sql", "#etl"]`.

*Hint:* Use `.startswith("#")`.'''
'''
tags = ["#sql", "python", "#etl", "data"]

hashtags = [w for w in tags if w.startswith("#")]
print(hashtags)'''

#Semi-guided
#**C1) Even squares:** Replace the placeholder with a comprehension that squares only the even numbers.

'''nums = [1, 2, 3, 4, 5, 6]
even_squares = [n * n for n in nums if n % 2 ==0 ]  #TODO: replace with comprehension
print(even_squares)  # expected: [4, 16, 36]'''

#**C2) Price extraction:** Replace the placeholder to extract integer prices from dollar-sign strings.

raw = ["  $12 ", "FREE", " $7", "  $100  ", "N/A"]
prices = [i.strip()[1:] for i in raw if i.strip().startswith("$")]  #TODO: replace with comprehension using strip(), startswith("$"), slicing
print(prices)  # expected: [12, 7, 100]

