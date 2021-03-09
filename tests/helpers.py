import re


def load_example_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().split('\n')

    return [(lino, line)
            for (lino, line) in enumerate(lines)
            if data_line(line)
            ]


def data_line(line):
    return not comment_line(line) and not blank_line(line)


def comment_line(line):
    return line[0:2] == '//'


def blank_line(line):
    return re.match('^\s*$', line) is not None


def test_modules(modules, positives, negatives):

    print()
    print('Testing %i positives, %i negatives.' %
          (len(positives), len(negatives)))

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
