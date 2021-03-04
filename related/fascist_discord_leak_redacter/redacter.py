import pyap
import re
import cursor
import time
import subprocess
import sys
import os


def detect_PII(text):
    return detect_phone_number(text) or\
        detect_email_address(text) or\
        detect_ssn(text) or\
        detect_addresses_basic_state_and_zip(text) or\
        detect_addresses_pyap(text)


# An address, according to this predicate, is anything that looks
# like `, CA 90210`, that is to say, a comma, then two letters,
# then five digits of zip code. This is fairly reliable in that,
# if something looks like this, it's usually an address, at least
# in the leak content it was tested on. But it can lead to false
# negatives because it requires the comma and the zip, which often
# can be omitted. It's a good compromise as a first pass for
# detecting addresses, tho. This predicate cannot be reworked to
# proide the location of the address, it's only useful for
# detecting the presence of an address. It only detects addresses
# with zip codes and so doesn't work for UK addresses, for example.
def detect_addresses_basic_state_and_zip(text):
    res = re.search(
        r',\s+[a-zA-Z][a-zA-Z]\s+[0-9][0-9][0-9][0-9][0-9][^0-9]', text)
    return res is not None


# An address, according to this predicate, is something that pyap
# considers to be an address (either US or CA, doesn't matter).
# This is a much stricter definition of address, and more complex,
# taking more time and producing many false negatives for strange
# reasons, but seemingly few false positive. This is  a last resort
# detector for addresses because of its complexity, and because
# most if not all of the addresses caught by this are caught more
# easily by the basic state and zip detector. Unlike the basic
# state and zip detector, however, this can be reworked to provide
# locations for the addresses not just a boolean yes/no if an
# address is present. A major drawback is that this predicate
# cannot detect no US/Canada addresses.
def detect_addresses_pyap(text):
    text = re.sub(r'[^a-zA-Z0-9 ]', '', re.sub(r'\s+', ' ', text.upper()))
    addresses = pyap.parse(text, country='US') +\
        pyap.parse(text, country='CA')

    return 0 < len(addresses)

# A phone number, according to this predicate, is an area code
# optionally in parentheses, followed by a 7 digit number, with
# `.`, `-`, and ` ` as separators. This catches a number of actual
# instances in the leaks, with no false positives, but it has
# some major limitations. Firstly, it doesn't detect numbers with
# no area code. This isn't too risky because it's hard to dial
# someone without the area code, tho an especially dedicated
# person might be able to deduce what the area code ought to be
# based on surrounding context. We feel this is an acceptably low
# risk given the number of false positives we get from not
# requiring the area code. The second major limitation is that it
# doesn't handle international phone numbers. There are definitely
# some international numbers in the leak, but patterns that match
# those tend to have very high false positive rates.


def detect_phone_number(text):
    res = re.search(
        r'\D(([0-7]\d\d|\([0-7]\d\d\))[\.\-\ ]\d\d\d[\.\-\ ]\d\d\d\d)\D', text)
    return res is not None


# An email address, according to this predicate, is anything of the
# form `XXX@YYY.ZZZ`, with a few constraints to limit false
# positives. There are a handful of false posities that are URLs,
# because URLs happen to permit this pattern, but they're relatiely
# few and far between that they shouldn't cause too many problems.
def detect_email_address(text):
    res = re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+\b', text)

    return res is not None


# An SSN, according to this predicate, is anything of the form
# `###-##-####`. This is an approximation, because lots of numeric
# things could have this formatting, but it looks like in the leak,
# most or all of them are SSNs. The dashes are necessary, tho, to
# avoid large numbers of false positives. Since SSNs are almost
# always written with dashes anyway, the false negative rate should
# be fairly low. No other obivous separators are used in the leak,
# as far as we can tell.
def detect_ssn(text):
    res = re.search(r'\b\d\d\d-\d\d-\d\d\d\d\b', text)

    return res is not None


LINERE = re.compile(r'^(\t"content":\s+")(.*)(",)$')


def redact_line(line):
    global LINERE
    m = LINERE.match(line)

    if m is not None:
        prefix = m.group(1)
        message = m.group(2)
        suffix = m.group(3)

        if detect_PII(message):
            return prefix + '[[PII REDACTED BY DDOSECRETS]]' + suffix

    return None


def redact(in_path, out_path):

    print()
    print('This program may take a while. Please be patient!')
    print()

    total = int(subprocess.check_output(
        ['wc', '-l', in_path]).decode(encoding='ascii').split()[0])

    print('Total lines: {val:,}'.format(val=total))

    cursor.hide()
    with open(in_path, 'r') as in_file, open(out_path, 'w') as out_file:
        start_time = time.time()
        found = 0
        for i, line in enumerate(in_file):
            t = time.time()
            dur = t - start_time
            m = int(dur / 60)
            s = int(dur - 60 * m)
            r = i / dur
            remaining = (total - i) / (r if r != 0 else 1)
            rm = int(remaining / 60)
            print('Progress: {pct:.2%} (Running: {min}m{sec}s, ETA: {rmin}m, Found: {found})'.format(
                pct=i / total, min=m, sec=s, rmin=rm, found=found).ljust(80)[0:80], end='\r')
            new_line = redact_line(line)
            if new_line:
                found += 1
            out_file.write(new_line or line)
        print()
        print()
        print('Redaction complete.')
        print()
        print('Total time: %im%is' % (m, s))
        print('Redacted messages: %i' % found)
        print()
    cursor.show()


def main():
    if 3 != len(sys.argv):
        print()
        print('Please provide input and output filepaths.')
        print()
        print('Usage: python3 redacter.py $INPUT $OUTPUT')
        print()

    else:
        in_path = os.path.abspath(sys.argv[1])
        out_path = os.path.abspath(sys.argv[2])

        if os.path.isfile(in_path):
            print()
            print('Input path:  ' + in_path)
            print('Output path: ' + out_path)
            print()
            try:
                redact(in_path, out_path)
            except KeyboardInterrupt:
                pass
            cursor.show()
        else:
            print()
            print('The input file')
            print()
            print('  ' + in_path)
            print()
            print('does not exist.')
            print()


main()
