# social security number locator


import re


def locate(text):
    res = re.search(
        r'(?<!\d)(\d\d\d[\.\-\ /]?\d\d[\.\-\ /]?\d\d\d\d)(?!\d)', text)

    if res is not None:
        return [res.span(1)]
    else:
        return []
