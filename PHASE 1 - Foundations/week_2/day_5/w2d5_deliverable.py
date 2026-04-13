'''**Deliverable:** `order_calculator.py`

Create a robust order calculator that **never crashes** on bad input.

**Prompts (in order):**
1. **Item name** (string) — must not be empty after `.strip()`
2. **Unit price** (float) — must be a valid number >= 0
3. **Quantity** (int) — must be a whole number >= 1
4. **Coupon code** (string) — if normalized to `"save10"`, apply 10% discount

**Output:** Print a receipt with item name, unit price, quantity, subtotal, discount, and final total.

**Requirements:**
- If any required input fails validation, print a specific error and stop (guard-clause style)
- Use `try`/`except` for numeric conversions
- Normalize coupon with `.strip().lower()` before comparing

**Constraints:**
- No loops (Week 3)
- For money output, raw floats are fine today (formatting comes later)

**What Could Go Wrong?**
- What if user types `-5` for price?
- What if user types `two` for quantity?
- What if user just presses Enter for item name?

Git checkpoint: `git add -A && git commit -m "W2D5 deliverable: robust order calculator"`'''