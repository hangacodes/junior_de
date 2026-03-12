'''words = ["dog", "cat", "dog", "bird", "cat", "dog"]
# Build freq: word -> count. Print the most frequent animal.'''

# words = ["dog", "cat", "dog", "bird", "cat", "dog"]

# freq = {}

# for word in words:
#     freq[word] = freq.get(word, 0)+1

# max = 0
# word_freq = None

# for k, v in freq.items():
#     if v > max:
#         max = v
#         word_freq = k
# print(freq)
# print(max)
# print(word_freq)

'''scores = ["Alice,85", "Bob,90", "Alice,78", "Bob,95", "Carol,88"]
# Build by_student: student -> list of scores. Print each student's average.'''

# scores = ["Alice,85", "Bob,90", "Alice,78", "Bob,95", "Carol,88"]

# by_student = {}

# for row in scores:
#     name , score = row.split(",")
#     score = int(score)
#     by_student.setdefault(name, []).append(score)


# for name, scores in by_student.items():
#     average = sum(scores) / len(scores)
#     print(f"{name}:{average}")
# print(by_student)

'''orders = ["pizza,12.5", "burger,8.0", "pizza,11.0", "sushi,15.0", "burger,9.5"]
# Build totals: item -> total spend. Print the most expensive item category.'''

# orders = ["pizza,12.5", "burger,8.0", "pizza,11.0", "sushi,15.0", "burger,9.5"]
# spent_by_item = {}

# for order in orders:
#     item, spent = order.split(",")
#     spent = float(spent)
#     spent_by_item[item] = spent_by_item.get(item, 0) + spent

# max_spent = 0
# max_item = None

# for k, v in spent_by_item.items():
#     if v > max_spent:
#         max_spent = v
#         max_item = k
# print(spent_by_item)
# print(f"Winner is: {max_item} with a total spending of - ${max_spent}")


'''logs = ["ERROR", "INFO", "ERROR", "WARN", "INFO", "ERROR", "INFO"]
# Build counts: level -> count. Print only levels that appear more than twice.'''


# logs = ["ERROR", "INFO", "ERROR", "WARN", "INFO", "ERROR", "INFO"]

# counts = {}

# for log in logs:
#     counts[log] = counts.get(log, 0) + 1

# for log, count in counts.items():
#     if count > 2:
#         print(f"{log}:{count}")




'''students = ["math,Alice", "science,Bob", "math,Carol", "science,Alice", "art,Bob"]
# Build by_subject: subject -> list of students. Print subject with most students.'''


# students = ["math,Alice", "science,Bob", "math,Carol", "science,Alice", "art,Bob"]

# by_subject = {}

# for row in students:
#     subject, student = row.split(",")
#     by_subject.setdefault(subject, []).append(student)

# print(by_subject)

# max_subject = 0
# subject_freq = None

# for subject, names in by_subject.items():
#     if len(names) > max_subject:
#         max_subject = len(names)
#         subject_freq = subject

# print(f"Subject with most students: {subject_freq} - with {max_subject} nr of students")



'''transactions = ["food,15.0", "travel,200.0", "food,22.5", "tech,999.0", "travel,150.0"]
category_limit = {"food": 100, "travel": 500, "tech": 800}
# Build totals. Then print each category and whether it's OVER or UNDER its limit.'''


# transactions = ["food,15.0", "travel,200.0", "food,22.5", "tech,999.0", "travel,150.0"]
# category_limit = {"food": 100, "travel": 500, "tech": 800}

# totals = {}

# for transaction in transactions:
#     category, num = transaction.split(",")
#     number = float(num)
#     totals[category] = totals.get(category, 0) + number

# for category, total in totals.items():
#         if total < category_limit[category]:
#             print(f"{category} under the limit")
#         elif total > category_limit[category]:
#             print(f"{category} over the limit")
#         else:
#              print("Good to go")
# print(totals)

'''votes = ["Alice", "Bob", "Alice", "Carol", "Bob", "Alice", "Carol", "Carol", "Bob", "Alice"]
# Build vote_counts. Print winner (most votes) and loser (fewest votes).'''


# votes = ["Alice", "Bob", "Alice", "Carol", "Bob", "Alice", "Carol", "Carol", "Bob", "Alice"]

# vote_counts = {}

# for name in votes:
#      vote_counts[name] = vote_counts.get(name, 0) + 1

# print(vote_counts)

# most_votes = 0
# winner = None


# for name, counts in vote_counts.items():
#     if counts > most_votes:
#         most_votes = counts
#         winner = name

# print(winner, most_votes)

# fewest_votes = most_votes
# loser = None

# for names, count in vote_counts.items():
#     if count < fewest_votes:
#         fewest_votes = count
#         loser = names
# print(loser, fewest_votes)



'''checkins = ["gym,Alice", "gym,Bob", "cafe,Alice", "gym,Carol", "cafe,Bob", "gym,Alice"]
# Build by_place: place -> list of visitors.
# Build visit_counts: person -> number of total visits across all places.'''

# checkins = ["gym,Alice", "gym,Bob", "cafe,Alice", "gym,Carol", "cafe,Bob", "gym,Alice"]

# by_place = {}

# visit_counts = {}

# for checkin in checkins:
#     place, name = checkin.split(",")

#     by_place.setdefault(place, []).append(name)

#     visit_counts[name] = visit_counts.get(name, 0) + 1
# print(by_place) 
# print(visit_counts)


'''products = ["laptop,999", "phone,699", "laptop,1099", "tablet,499", "phone,799"]
price_tier = {"laptop": "premium", "phone": "mid", "tablet": "budget"}
# Build totals: product -> total revenue.
# Print each product with its total revenue and price tier (unknown -> "unclassified")'''

# products = ["laptop,999", "phone,699", "laptop,1099", "tablet,499", "phone,799"]
# price_tier = {"laptop": "premium", "phone": "mid", "tablet": "budget"}

# totals = {}

# for product in products:
#     item, price = product.split(",")
#     price = float(price)
#     totals[item] = totals.get(item, 0) + price

# for item , total in totals.items():
#     tier = price_tier.get(item, "unclassified")
#     print(f"{item} : total of ${totals[item]} - tier: {tier}")


'''events = ["click,homepage", "click,shop", "view,homepage", "click,homepage", 
          "purchase,shop", "view,shop", "click,shop", "purchase,homepage"]
# Build by_page: page -> list of event types.
# Build event_counts: event_type -> count.
# Print the page with the most total events.
# Print the most common event type.'''

events = ["click,homepage", "click,shop", "view,homepage", "click,homepage", 
          "purchase,shop", "view,shop", "click,shop", "purchase,homepage"]

by_page = {}
event_counts = {}

for row in events:
    event, page = row.split(",")
    by_page.setdefault(page, []).append(event)

    event_counts[event] = event_counts.get(event, 0) + 1
print(by_page)
print(event_counts)

most_events = 0
top_page = None

for page, events in by_page.items():
    if len(events) > most_events:
        most_events = len(events)
        top_page = page
print(f"Most common event:{top_page} with: {most_events} in total")

winner = None
top_event = 0

for k ,v in event_counts.items():
    if v > top_event:
        top_event = v
        winner = k

print(winner)
print(top_event)