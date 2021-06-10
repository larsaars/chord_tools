"""
converts inline chords to outline chords (from clipboard)
example:
This [Am]is a line with [D]inline chords

     Am             D
This is a line with outline chords
"""

import re

from clipboard_utils import *

INLINE_CHORD_PATTERN = r'\[[^\[]*]'

# read all lines for inline chords and then append for every line containing inline chords outline chords
for line in read_clipboard().splitlines():
    # find all chords with matching regex pattern
    matches = re.findall(INLINE_CHORD_PATTERN, line)

    # get len of iterator
    if len(matches) == 0:
        output.append(line)
    else:
        chords_line = ''
        last_index, minus = 0, 0
        for match in matches:
            chord_raw = match.lstrip('[').rstrip(']')
            chord_raw_len = len(chord_raw)
            index = line.index(match)
            line = line.replace(match, '', 1)
            index_diff = index - last_index - minus

            chords_line += index_diff * ' ' + chord_raw

            last_index = index
            minus = chord_raw_len

        output.append(chords_line)
        output.append(line)

write_clipboard()
