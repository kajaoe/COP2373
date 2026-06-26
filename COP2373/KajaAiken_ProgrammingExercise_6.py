# Import regular expressions.
import re

# Define the phone number validator function.
def validate_phone(phone: str) -> bool:
    pattern = r'^(\+1[\s\.-]?)?(\(\d{3}\)|\d{3})[\s\.-]?\d{3}[\s\.-]?\d{4}$'
    return bool(re.match(pattern, phone))

# Define the social security number validator function.
def validate_ssn(ssn: str) -> bool:
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))

# Define the zip code validator function.
def validate_zip(zip: str) -> bool:
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip))

# Define a function that will test the validity of information received from the user.
def run_test():
    print('\n')
    print('-' * 50)
    print('Please wait while we verify your information...')
    print('-' * 50)
    print('\n')

    # Test scenarios for phone number, social security number, and zip code.
    phone_test = [("123-456-7890", True), ("(123) 456-7890", True), ("1234567890", True), ("123-45-67890", False)]
    ssn_test = [("000-12-3456", True), ("123456789", False), ("123-45-678", False)]
    zip_test = [("90210", True), ("90210-1234", True), ("9021", False), ("90210-123", False)]

    print('-' * 50)
    print('Phone Number Test:', 'Verified.' if all(validate_phone(i) == e for i, e in phone_test) else 'Failed to verify.')
    print('Social Security Number Test:', 'Verified.' if all(validate_ssn(i) == e for i, e in ssn_test) else 'Failed to verify.')
    print('ZIP Code Test:', 'Verified.' if all(validate_zip(i) == e for i, e in zip_test) else 'Failed to verify.')
    print('-' * 50)

# Define main.
def main():
    print('-' * 50)
    print('Phone Number    Social Security Number    ZIP Code \n'
   '                    Validator!')
    print('-' * 50)

    # Gather the user information.
    user_phone = input('Enter a phone number: ').strip()
    user_ssn = input('Enter a Social Security Number (AAA-GG-SSSS): ').strip()
    user_zip = input('Enter a ZIP code: ').strip()

    print('\n')9
    print('-' * 50)
    print('Here are your results!')
    print('-' * 50)
    print('\n')

    # Display the results based off of the information received from the user.
    if validate_phone(user_phone):
        print(f'The phone number {user_phone} is valid!')
    else:
        print(f'The phone number {user_phone} is not valid!')

    if validate_ssn(user_ssn):
        print(f'The social security number {user_ssn} is valid!')
    else:
        print(f'The social security number {user_ssn} is not valid!')

    if validate_zip(user_zip):
        print(f'The zip code {user_zip} is valid!')
    else:
        print(f'The zip code {user_zip} is not valid!')
    run_test()

# Run main to execute the script.
if __name__ == '__main__':
    main()