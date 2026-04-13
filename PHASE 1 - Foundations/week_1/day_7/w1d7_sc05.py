'''**SC-05 — Time decomposer (no hints)**

Given `total_seconds = 9847`:

1. Compute `hours`, `remaining_after_hours`, `minutes`, `seconds` using `//` and `%` **only** — no division `/`, no subtraction for this part.
2. Print: `2h 44m 7s`
3. Print the total as a formatted string: `02:44:07` (zero-padded — look up `{x:02d}` format specifier on your own and figure out how to use it)

*This one requires you to find something you weren’t explicitly taught. That’s intentional — in real engineering you’ll constantly hit format specifiers you need to look up.*
'''
total_seconds = 9847

minutes = total_seconds // 60
print(minutes)

hours = minutes // 60
print(hours)

remaining_minutes = minutes % 60
print(remaining_minutes)

remaining_seconds = total_seconds % 60
print(remaining_seconds)

# TOOK ME SOME TRIES ! But i got it i guess, but i wouldn't have known how to do it if it wasn't for the second task : Prin(2h 44m 7 s) so i knew what numbers to look for.

total = (f"{hours:02d}:{remaining_minutes:02d}:{remaining_seconds:02d}")
print(total)