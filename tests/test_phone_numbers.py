from helpers import *
from library import phone_numbers


phone_numbers_positives = load_example_data(
    'example_data/phone_numbers_positives.txt')
phone_numbers_negatives = load_example_data(
    'example_data/phone_numbers_negatives.txt')


phone_modules = [
    phone_numbers
]

print()
print('======== Phone Numbers ========')

test_modules(phone_modules, phone_numbers_positives, phone_numbers_negatives)

print()
