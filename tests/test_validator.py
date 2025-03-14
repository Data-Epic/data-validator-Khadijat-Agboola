import pytest
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  #This adds parent directory to sys.path
from Validator.validator import *

validator = DataValidator()    # Instantiating the DataValidator class

"""
Testing email validator function with a valid email.
Expects a success message that email is valid.
"""
def test_validate_email():
    validator= DataValidator()
    email = "khadijahagboola12@gmail.com"
    result = validator.validate_email(email)
    assert f"{email} is valid" in result

"""
Testing email validator function with an invalid email.
Expects an error message that email is not valid.
"""
def test_validate_invalid_email():
    validator = DataValidator()
    email = "khadijahagboola12@gmail"  # the email doesn't include .com/.net etc
    result = validator.validate_email(email)
    assert f"{email} is not valid" in result

"""
Testing phone validator function with a valid phone number.
Expects a success message that phone number is valid.
"""
def test_validate_phone():
    phone = "+14155552671"  #a valid phone number with + and country code "1"
    result = validator.validate_phone(phone)
    assert f"{phone} is valid" in result

"""
Testing email validator function with an invalid phone number.
Expects an error message that phone number is not valid.
"""
def test_invalid_validate_phone():
    invalid_phone = "+1415555"  # Shorter than expected phone number
    result = validator.validate_phone(invalid_phone)
    assert f"{invalid_phone} is not valid" in result

"""
Testing date validator function with a valid date.
Expects a success message that date is valid.
"""
def test_validate_date():
    date = "2025-03-13"     #a valid date
    result = validator.validate_date(date)
    assert f"{date} is valid" in result

"""
Testing date validator function with an invalid date.
Expects an error message that date is not valid.
"""
def test_invalid_validate_date():
    invalid_date = "2025-02-30"  # Invalid date (February 30th does not exist)
    result = validator.validate_date(invalid_date)
    assert f"{invalid_date} is not valid" in result

"""
Testing url validator function with a valid url.
Expects a success message that url is valid.
"""
def test_validate_url():
    url = "https://discord.com/channels/1159077758962503762/1246459768357523527"    #Data Epic discord URL
    result = validator.validate_url(url)
    assert f"{url} is valid" in result

"""
Testing url validator function with an invalid url.
Expects an error message that url is not valid.
"""
def test_invalid_validate_url():
    invalid_url = "htp://discord.com/channels/1159077758962503762/1246459768357523527"  # Invalid protocol (htp instead of http)
    result = validator.validate_url(invalid_url)
    assert f"{invalid_url} is not valid" in result
