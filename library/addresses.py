# address locator


import re


def locate(text):
    res = re.search(
        r'(?<!\d)(\d+[\w,\s]+\d+)(?!\d)', text.lower())

    if res is not None:
        return [res.span(1)]
    else:
        return []
