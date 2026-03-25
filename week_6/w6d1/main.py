#drill 1
import text_utils


print(text_utils.strip_and_lower("  HELLO WORLD  "))
print(text_utils.strip_and_lower("  Data Engineering  "))

print(text_utils.clean_tag("  Python Basics  "))
print(text_utils.clean_tag("data pipeline"))

print(text_utils.is_blank("    "))
print(text_utils.is_blank("  hello "))
