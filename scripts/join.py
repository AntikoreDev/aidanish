# FIle 'verbs.py'
# This script will get all entries from verbs.txt, then make a list of all aidanish words not repeating any, then conjugate them into conjugated.txt

from scripts import parse

# Run the script
def Run():
	
	verbs = open('./lexicon/conjugated.txt', 'r', encoding = 'utf-8').read().splitlines()
	wordlist = open('./lexicon/words.txt', 'r', encoding = 'utf-8').read().splitlines()

	wordlist.extend(verbs)

	f = open('./lexicon/words+conjugated.txt', 'w', encoding = 'utf-8')
	f.write('\n'.join(wordlist))
	f.close()
	
# Run the code if it was executed by console directly!
if (__name__ == '__main__'):
	Run()