def format_header(title):
    return "=== " + title + " ==="

def format_result(result, position):
    return "#" + str(position)+ " " + result["player"] + ": " + str(result["score"]) + " pts"

def format_summary(results):
    count = 0
    total = 0
    for result in results:
        total += result["score"]
        count += 1

    average = total / count

    return "Count: " + str(count) + " Average score: " + str(round(average, 2))

if __name__ == "__main__":
    print("idk")