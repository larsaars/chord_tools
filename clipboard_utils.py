"""
helper to get string from clipboard
and then return it to there
"""

import win32clipboard

# create output string that can later on be appended
output = []


def read_clipboard() -> str:
    win32clipboard.OpenClipboard()
    data: str = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data


def write_clipboard():
    global output
    # set output as clipboard data again
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    output = '\n'.join(output)
    try:
        win32clipboard.SetClipboardText(output)
    except Exception:
        print(output)
        input("waiting...")

    win32clipboard.CloseClipboard()
