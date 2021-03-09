from helpers import *
from library import addresses


addresses_positives = load_example_data(
    'example_data/addresses_positives.txt')
addresses_negatives = load_example_data(
    'example_data/addresses_negatives.txt')


addresses_modules = [
    addresses
]

print()
print('======== Addresses ========')

test_modules(addresses_modules, addresses_positives,
             addresses_negatives)

print()
