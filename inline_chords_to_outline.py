"""
converts inline chords to outline chords (from clipboard)
example:
This [Am]is a line with [D]inline chords

     Am             D
This is a line with outline chords
"""

from clipboard_utils import *

for line in read_clipboard().splitlines():
    pass

write_clipboard()