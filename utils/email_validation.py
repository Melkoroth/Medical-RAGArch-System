from email_validator import validate_email, EmailNotValidError

def validate_user_email(email: str) -> bool:
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False
