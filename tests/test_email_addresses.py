from helpers import *
from library import email_addresses


email_addresses_positives = load_example_data(
    'example_data/email_addresses_positives.txt')
email_addresses_negatives = load_example_data(
    'example_data/email_addresses_negatives.txt')


email_addresses_modules = [
    email_addresses
]

print()
print('======== Email Addresses ========')

test_modules(email_addresses_modules, email_addresses_positives,
             email_addresses_negatives)

print()
