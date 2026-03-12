
logs = [
    "INFO,auth,login",
    "WARN,auth,bad_password",
    "INFO,shop,view_item",
    "ERROR,shop,payment_failed",
    "INFO,auth,logout",
    "INFO,shop,view_item",
    "WARN,shop,slow_response"
]
severity = {"INFO": 1, "WARN": 2, "ERROR": 3}
level_counts = {}
by_service = {}


for log in logs:
    parts = log.split(",")
    level, service, message = parts
    sev = severity.get(level, 0)

    level_counts[level] = level_counts.get(level, 0) + 1

    by_service.setdefault(service, []).append(message)

    print(level, service, message, "->", sev)




max_word = 0
freq_word = None

for k, v in by_service.items():
    if len(v) > max_word:
        max_word = len(v)
        freq_word = k
print(max_word)
print(freq_word)