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
