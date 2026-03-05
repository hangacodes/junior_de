'''**Scenario:** You receive a CSV header row as text and need to ensure required columns exist,
 remove unwanted columns safely, and optionally pop a column by index.

**Requirements:**

1. Ask the user for a comma-separated header row (e.g., `email,created_at`)
2. Turn it into a list using `.split(",")` — also strip whitespace with `.replace(" ", "")`
3. Handle the edge case where the user enters an empty string 
(`.split(",")` on `""` gives `[""]` — correct to `[]`)
4. Ensure `"id"` exists at the front — if missing, insert at index 0
5. Ensure `"email"` exists somewhere — if missing, append it
6. Ask the user for a column name to remove — if present, remove it; otherwise print a message
7. Ask the user for an index to pop (or blank to skip) 
— handle `ValueError` for non-integer input and out-of-range indexes with friendly messages
8. Print the final header list and its length

**Constraint:** No loops yet — handle each requirement with direct list operations and `if` statements.

**What Could Go Wrong?** 
What happens if the user enters only spaces? 
What if they try to pop index 0 after all elements have been removed?

Git checkpoint: `git add -A && git commit -m "W3D1: header_manager deliverable"`

> You'll write similar guard-and-modify code for each column here. 
In Week 3 Day 2, you'll handle this with a `for` loop over a list of columns in a few lines.
For now, notice the pattern — that recognition is exactly what will make loops feel natural when you get there.
>'''