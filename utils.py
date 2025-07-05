import re
from datetime import datetime


def validate_egyptian_phone_number(phone_number):
    """
    Validates an Egyptian phone number.
    Egyptian phone numbers start with +20 or 0020, followed by 10 digits.
    """
    pattern = r"^(?:\+20|0020|0)?1[0125][0-9]{8}$"
    return re.match(pattern, phone_number)


def validate_email(email):
    """
    Validates an email address.
    A simple regex to check the format of the email.
    """
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


def validate_date(date_str):
    """
    Validates a date string in the format YYYY-MM-DD.
    Returns a datetime object if valid, otherwise returns False.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return False
