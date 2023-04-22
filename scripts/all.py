# File 'all.py'
# This file will extract all entries from lexicon/types and put it all together into 'all.txt'

from scripts import parse
import os

# Run the script
def Run():
	
	entries = []
	directory = r"./lexicon/types"

	for root, directories, files in os.walk(directory):
		for file in files:
			if (file.endswith(".txt")):
				entries.extend(parse.Parse(os.path.join(root, file), False))

	entries.sort()
	
	file = open('./lexicon/all.txt', 'w', encoding = 'utf-8')
	file.write('\n'.join(entries))
	file.close()
	
# Run the code if it was executed by console directly!
if (__name__ == '__main__'):
	Run()