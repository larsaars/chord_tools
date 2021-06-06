"""
remove unnecessary lines from chord strings
helpful when porting from ultimate-guitar.com to chords-and-tabs.net for example
"""

import win32clipboard

# get clipboard data
win32clipboard.OpenClipboard()
data: str = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

# create output string
output = []
# loop through every line:
# if it is one standalone empty line, remove it
# if there are multiple empty lines, keep only one
empty_lines_in_row = 0
for line in data.splitlines():
    # trim each line
    line_trimmed = line.strip()

    if line_trimmed == '':
        empty_lines_in_row += 1
    else:
        if empty_lines_in_row > 1:
            output.append('')

        empty_lines_in_row = 0

    if empty_lines_in_row == 0:
        output.append(line)

# set output as clipboard data again
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
output = '\n'.join(output)
try:
    win32clipboard.SetClipboardText(output)
except Exception:
    print(output)

win32clipboard.CloseClipboard()
