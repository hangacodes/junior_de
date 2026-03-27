def compute_rate(count_text, total_text):
    try:
        count = int(count_text)
        total = int(total_text)
        rate = count / total
    except ValueError as e:
        print(f"  Bad number:{e}")
        return None
    except ZeroDivisionError:
        print(f"  Division by zero: total={total_text}")
        return None
    else:
        return round(rate, 4)

pairs = [("25", "200"), ("10", "0"), ("abc", "50"), ("30", "300")]
for c, t in pairs:
    result = compute_rate(c, t)
    print(f"  ({c},{t}) ->{result}")


    