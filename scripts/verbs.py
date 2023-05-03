# FIle 'verbs.py'
# This script will get all entries from verbs.txt, then make a list of all aidanish words not repeating any, then conjugate them into conjugated.txt

from scripts import parse

# Run the script
def Run():
	
	entries = parse.Parse('./lexicon/types/verbs.txt')
	words = []

	for e in entries:
		entry = e.split('→')
		trans = entry[1] if len(entry) > 1 else None
		if (trans):
			word = trans.lower().split(', ')
			for w in word:
				if (w.strip() not in words and " " not in w.strip()):
					words.append(w.strip())
	conjugated = []

	for w in words:
		if (w.endswith("i")):
			conjugated.append(w + 'e')
			conjugated.append(w + 'o')
			conjugated.append(w + 'ki')
			conjugated.append(w + 'oto')
			conjugated.append(w + 'eon')
			conjugated.append(w + 'et')
		elif (w.endswith('e')):
			conjugated.append(w + 'ie')
			conjugated.append(w + 'io')
			conjugated.append(w + 'ki')
			conjugated.append(w + 'ioto')
			conjugated.append(w + 'ieon')
			conjugated.append(w + 't')
			
	conjugated.sort()

	f = open('./lexicon/conjugated.txt', 'w', encoding = 'utf-8')
	f.write('\n'.join(conjugated))
	f.close()
	
# Run the code if it was executed by console directly!
if (__name__ == '__main__'):
	Run()