def is_valid_user_id(text: str) -> bool:
    """True if text is exactly 6 digits after stripping."""
    text = text.strip()
    if not len(text) == 6:
        return False
    for ch in text:
        if not ch.isdigit():
            return False
    return True
    #TODO: guard clause for length != 6
    #TODO: loop through each character, reject if not a digit
    #TODO: return True


def is_email_like(email: str) -> bool:
    """True if email has basic valid structure after sanitization."""
    email = email.strip().lower()
    if email == "" or email == " ":
        return False
    if email.count("@") != 1:
        return False
    if email[0] == "@" or email[-1] == "@":
        return False
    pos = email.find("@")
    if "." not in email[pos+1:]:
        return False
    return True
    #TODO: guard for empty
    #TODO: guard for spaces
    #TODO: guard for count of @ != 1
    #TODO: guard for @ at start or end
    #TODO: guard for no dot in domain
    #TODO: return True


def is_valid_record(record: dict) -> bool:
    """True if record has 'id' and 'email' keys, and both pass validation."""
    if "id" not in record:
        return False
    if "email" not in record:
        return False    
    if is_valid_user_id(record["id"]) and is_email_like(record["email"]):
        return True
    return False
    #TODO: guard if "id" missing
    #TODO: guard if "email" missing
    #TODO: return result of validating both fields
    #TODO: return False

print(is_valid_record({"id": "000123", "email": "  Ada@Example.COM  "}))  # True
print(is_valid_record({"id": "12A123", "email": "bob@example.com"}))      # False
print(is_valid_record({"email": "missing@id.com"}))                        # False