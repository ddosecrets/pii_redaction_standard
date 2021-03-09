from helpers import *
from library import social_security_numbers


ssn_positives = load_example_data(
    'example_data/social_security_numbers_positives.txt')
ssn_negatives = load_example_data(
    'example_data/social_security_numbers_negatives.txt')


ssn_modules = [
    social_security_numbers
]

print()
print('======== Social Security Numbers ========')

test_modules(ssn_modules, ssn_positives, ssn_negatives)

print()
