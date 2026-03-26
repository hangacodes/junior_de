def is_non_empty(text):
    if text.strip() != "":
        return True
    return False

    #TODO: return True if text is not blank after stripping
    # Hint: predicate pattern from W5D5
    pass

def is_int_like(text):
    text = text.strip().lstrip("-")
    if text.isdigit():
        return True
    return False
    #TODO: return True if text converts to int safely
    # Hint: .strip().lstrip("-") removes sign, then .isdigit() checks digits
    # Note: .isdigit() alone rejects negatives — this workaround handles "-5"
    