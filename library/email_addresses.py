# phone number locator


import re


def locate(text):
    res = re.search(
        r'(?<!\w)(\w+(\s*(@|\[@\]|\(@\)|at|\[at\]|\(at\))\s*)\w+(\s*(\.|\[\.\]|\(\.\)|dot|\[dot\]|\(dot\))\s*)\w+)(?!\w)', text.lower())

    if res is not None:
        return [res.span(1)]
    else:
        return []
