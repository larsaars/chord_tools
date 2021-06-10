"""
remove unnecessary lines from chord strings
helpful when porting from ultimate-guitar.com to chords-and-tabs.net for example
"""

from clipboard_utils import *

# loop through every line:
# if it is one standalone empty line, remove it
# if there are multiple empty lines, keep only one
empty_lines_in_row = 0
for line in read_clipboard().splitlines():
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

# save again
write_clipboard()
