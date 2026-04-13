#drill 1 module
def strip_and_lower(s):
    text = s.strip().lower()

    return text

def clean_tag(s):
    text = s.strip().lower().replace(" ", "_")

    return text

def is_blank(s):
    if s.strip() != "":
        return True
    return False
if __name__ == "__main__":
    print("CINEMATIC")