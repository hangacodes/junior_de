'''Answer each one without looking at your notes first. Mark anything you hesitated on.

**From W1D1:**
1. A script contains a print statement with a missing closing quote. Does Python print anything before stopping? Why?
-It will have a syntax error, because one quote is missing 

2. What’s the difference between source code and output?
- source code is the code i write, output is what the computer gives back 

3. Why do comments exist if Python ignores them?
- to explain what your program is doing, for other team members to know what you did.

**From W1D2:**
4. What does `=` actually do? (Don’t say “equals.”)
- '=' assigns a value to a variable name. 

5. `True` vs `true` — what happens with the lowercase version?
- the lowercase version is not recognised as boolean.

6. Why is `"42"` not the same as `42` even though they print identically?
- because it is between quotes , it mean is a string literal and you cannot use it math expressions

7. When does `int("3.50")` fail, and what should you use instead?
- you should use float , when it fails ? idk

**From W1D3:**
8. What does `/` always return, even for `10 / 2`?
- it returns a float

9. If you write `2 + 3 * 4`, what is the result and why?
- result is 14 because the multiplication is the first one done by Python - I know answer is pretty poopy, but it's how i can explain in my own words lol

10. When would you use `round()` instead of `:.2f`?
- when you want to do some math operations ? I have no clue tbh

11. What does `%` return?
- returns the remainder after // 

**From W1D4:**
12. What is the last valid index of `"Berlin"`?
- 5

13. In `s[2:5]`, is position 5 included or excluded?
- excluded

14. What does `s[::-1]` produce?
- a reversed string

15. Why does `s[0] = "X"` fail?
-because strings are immutable ? I have no idea tbh

16. What does `s[500:600]` return if `s` has only 10 characters?
- and empty line

**From W1D5:**
17. Why does `s.upper()` on its own (not stored) seem to “do nothing”?
- because strings are immutable, and you have to assign the new string to a variable to get the wanted output. or to update the variable like s = s.upper()

18. What does `.find()` return when the substring isn’t there?
-it returns -1 -- WHICH I LEARNED THAT IT CAN BE TRICKY IF THEN YOU ASK FOR THE LAST INDEX OF A STRING! Cause it will actually work heheh

19. What type does `.startswith("raw_")` return?
- bool

20. Why must `.strip()` come *before* type casting?
-because you cannot cast a string that has whitespaces ?

**From W1D6:**
21. What’s the difference between `.split(",")` and `.split()`?
- .split(",") - splits where python finds ',' and .split() splits between whitespaces?

22. After `parts = "a|b|c".split("|")`, what is `parts[-1]`?
- should be c

23. Why does `.join()` crash when a list contains an integer?
-because hmmm...idk i just know i need to transform the ints in strs 


24. What happens if you call `.split(",")` on a string that contains no commas?
- i forgot - but i checked , and it returns a list that only contains 1 string, if you are looking for index number 1, you get an error
'''
parts = "a|b|c".split(",")
print(parts[0])
