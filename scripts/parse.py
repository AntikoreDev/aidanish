# This file should open a file and return its lines
# From the content, it must delete any comment, marked with a # at the start of the line
# It will also remove any empty lines
# It will also optionally remove any stuff in parenthesis
# The file will be opened for reading and return a list with all the lines parsed, using utf-8 encoding

import re

# Execute the parsing
def Parse(filename, parenthesis = True) -> list:
    file = open(filename, 'r', encoding = 'utf-8')
    lines = file.read().split('\n')
    parsed = []

    for l in lines:
        line = l.strip()
        if (line == '' or line.startswith('#')):
            continue

		# Remove parenthesis if there are some, and it's enabled
        cleaned = line if not parenthesis else re.sub(r"\((.+)\)", "", line)
        cleaned = re.sub(r'\s+', ' ', cleaned) # Remove any extra spaces within the entries

        parsed.append(cleaned.lower())

    return parsed