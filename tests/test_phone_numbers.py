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

for mod in phone_modules:

    print()
    print(mod.__name__ + ':')

    print()
    false_neg_errors = []
    for (lino, line) in phone_numbers_positives:
        found = mod.locate(line)
        if not found:
            false_neg_errors.append((lino, line))

    if not false_neg_errors:
        print('  No false negatives.')
    else:
        print('  Found false negatives:')
        for lino, line in false_neg_errors:
            print('    line %i  --  %s' % (lino, line))

    print()
    false_pos_errors = []
    for (lino, line) in phone_numbers_negatives:
        found = mod.locate(line)
        if found:
            false_pos_errors.append((lino, line))

    if not false_pos_errors:
        print('  No false positives.')
    else:
        print('  Found false positives:')
        for lino, line in false_pos_errors:
            print('    line %i  --  %s' % (lino, line))

print()
