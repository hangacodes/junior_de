def is_valid_student_id(text: str) -> bool:
    '''True if text is exactly 8 chars , first 2 letters, last 6 digits'''
    text = text.strip().upper()
    if len(text) != 8:
        return False
    letters = text[:2]
    for ch in letters:
        if ch < 'A' or ch > 'Z':
            return False
    numbers = text[2:]
    for number in numbers:
        if not number.isdigit():
            return False
    return True


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


def is_valid_enrollment(record: dict) -> bool:
    
    if "student_id" not in record:
        return False
    if "email" not in record:
        return False
    if "course" not in record:
        return False
    course = record["course"]
    if is_valid_student_id(record["student_id"]) and is_email_like(record["email"]) and course.strip() != "":
        return True
    return False
        
    
def split_enrollments(records: list) -> tuple:
    accepted = []
    rejected = []
    for record in records:
        if is_valid_enrollment(record):
            record["email"] = record["email"].strip().lower()
            record["student_id"] = record["student_id"].strip().upper()
            accepted.append(record)
        else:   
            rejected.append(record)
    return accepted, rejected
records = [
    {"student_id": "AB123456", "email": "ada@uni.edu", "course": "DE101"},
    {"student_id": "12345678", "email": "bob@uni.edu", "course": "DE101"},
    {"student_id": "CD789012", "email": "no-at-sign", "course": "DE102"},
    {"student_id": "EF345678", "email": "  Carol@Uni.EDU  ", "course": "  "},
    {"student_id": "GH901234", "email": "dee@uni.edu", "course": "DE103"},
    {"email": "missing-id@uni.edu", "course": "DE101"}
]

accepted, rejected = split_enrollments(records)
print(len(accepted))
print(len(rejected))
print(accepted)