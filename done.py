# FIle 'words.py'
# This script will get all entries from lexicon/types, then make a list of all aidanish words not repeating any, then move it to words.txt

import parse

# Run the script
def Run():
	
	entries = parse.Parse('./lexicon/all.txt')
	words = []

	for e in entries:
		entry = e.split('→')
		trans = entry[0] if len(entry) > 1 else None
		if (trans):
			word = trans.lower().split(', ')
			for w in word:
				if (w.strip() not in words):
					words.append(w.strip())

	words.sort()

	f = open('./lexicon/done.txt', 'w', encoding = 'utf-8')
	f.write('\n'.join(words))
	f.close()
	
# Run the code if it was executed by console directly!
if (__name__ == '__main__'):
	Run()