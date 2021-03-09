from helpers import *
from library import phone_numbers


def test_modules(modules, positives, negatives):

    for mod in modules:

        print()
        print(mod.__name__ + ':')

        print()
        false_neg_errors = []
        for (lino, line) in positives:
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
        for (lino, line) in negatives:
            found = mod.locate(line)
            if found:
                false_pos_errors.append((lino, line))

        if not false_pos_errors:
            print('  No false positives.')
        else:
            print('  Found false positives:')
            for lino, line in false_pos_errors:
                print('    line %i  --  %s' % (lino, line))


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
