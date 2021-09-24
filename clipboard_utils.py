"""
helper to get string from clipboard
and then return it to there
"""

import pyperclip

# create output string that can later on be appended
output = []


def read_clipboard() -> str:
    return pyperclip.paste()


def write_clipboard():
    global output
    # set output as clipboard data again
    pyperclip.copy('\n'.join(output))
