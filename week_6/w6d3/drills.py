#**A1 — Predict:** What prints?
try:
    x = int("9")
except ValueError:
    print("bad")
else:
    print("ok")
finally:
    print("done")

# ok 
#done

#**A2 — Predict:** What prints?
try:
    x = int("nine")
except ValueError:
    print("bad")
else:
    print("ok")
finally:
    print("done")

    #bad, done

#**A3 — Predict:** What prints?
try:
    print("A")
    result = 10 / 0
    print("B")
except ZeroDivisionError:
    print("C")
finally:
    print("D")

#A, C , B , D

#**A4 — Spot:** This code catches an error but has a subtle problem. What is it?

def safe_parse(text):
    try:
        return int(text)
    except Exception:
        return 0        # you don't know what the error is


#**A5 — Predict:** What prints? (Tests `as e` and tuple syntax)

values = ["10", "bad", "99"]
for v in values:
    try:
        result = int(v) / (int(v) - 10)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error on{v!r}:{e}")
    else:
        print(f"Result:{result:.2f}")

