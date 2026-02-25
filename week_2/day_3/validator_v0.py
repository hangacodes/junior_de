name = "  "
age = -5
country = "XX"

clean_name = name.strip()


if clean_name == "":
    print("INVALID: missing name")
elif country != "DE" and country != "FR" and country != "US":
    print("INVALID: unsupported country")
elif age <0 or age >120:
    print("INVALID: age out of range")
else:
    print("VALID")