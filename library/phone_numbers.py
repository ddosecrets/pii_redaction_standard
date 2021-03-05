# phone number locator


import re


def locate(text):
    res = re.search(
        r'(?<!\d)(((\+?1)?[\.\-\ ]?(\d\d\d|\(\d\d\d\)))?[\.\-\ ]?\d\d\d[\.\-\ ]?\d\d\d\d)(?!\d)', text)

    if res is not None:
        return [res.span(1)]
    else:
        return []
