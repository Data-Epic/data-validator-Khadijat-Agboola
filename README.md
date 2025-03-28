# Data Validator

## Overview
Data Validator is a Python package that provides functions to validate common data formats, including email addresses, phone numbers, dates, and URLs. It ensures data integrity and correctness in various applications.

## Features
- Validate email addresses
- Validate phone numbers
- Validate URLs
- Validate date formats

## Project Structure
```
Data-Validator/
│── Validator/
│   ├── validator.py  # Core validation functions
│   ├── setup.py      # Package setup file
│── tests/
│   ├── test_validator.py  # Unit tests for validation functions
│── README.md  # Project documentation
```

## Installation
Clone the repository and navigate to the project directory:
```sh
git clone https://github.com/your-username/data-validator.git
cd data-validator
```
Install the package using pip:
```sh
pip install .
```

## Usage
Import the `validator` module and use its functions:
```python
from Validator import validator

# Validate email
email = "example@example.com"
print(validator.validate_email(email))  # Output: example@example.com is valid

# Validate phone number
phone = "+14155552671"
print(validator.validate_phone(phone))  # Output: +14155552671 is valid

# Validate URL
url = "https://example.com"
print(validator.validate_url(url))  # Output: https://example.com is valid

# Validate date
date = "2024-03-14"
print(validator.validate_date(date))  # Output: 2024-03-14 is valid
```

## Running Tests
To run the unit tests, navigate to the project directory and execute:
```sh
pytest tests/
```

## Contributing
Contributions are welcome. Feel free to submit issues or pull requests.


## Author
[Khadijat Agboola](https://github.com/khadijah-agboola)

