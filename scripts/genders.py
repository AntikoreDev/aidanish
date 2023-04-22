# FIle 'genders.py'
# This script will get all entries from lexicon/types, then make a list of all aidanish words not repeating any, then move it to words.txt

from scripts import parse
import sys

female = ["a", "i", "s"]
male = ["o", "u", "k"]

# Run the script
def Run():
	
	entries = parse.Parse('./lexicon/types/nouns.txt')
	entries.extend(parse.Parse("./lexicon/types/adjectives.txt"))
	words = []

	entries = entries if len(sys.argv) < 2 else [ " → " + sys.argv[1] ]
	inputted = len(sys.argv) >= 2

	for entry in entries:
		obj = entry.split(" → ")
		if (len(obj) <= 1):
			continue

		trans = obj[1].split(", ")

		for word in trans:
			word = word.lower().strip()
			if (" " in word):
				continue

			if (word.endswith('sis')):
				words.append("la {}".format(word))
			
			end = word[len(word) -1]
			if (end in male):
				words.append("ei {}".format(word))
			elif (end in female):
				words.append("la {}".format(word))
			else:
				male_pred = 0
				female_pred = 0
				special = 0
				for c in word:
					if (c in "ou"):
						male_pred += 1
					elif (c in "a"):
						female_pred += 1
					elif (c in "i"):
						special += 1
				if (male_pred > female_pred):
					words.append("ei {}".format(word))
				elif (male_pred == female_pred):
					if (end in "e"):
						if (special > male_pred and special > female_pred):
							words.append("ei {}".format(word))
						else:
							words.append("la {}".format(word))
					else:
						words.append("ei {}".format(word))
				else:
					words.append("la {}".format(word))

	if (inputted):
		print(words[0])
		return


	f = open('./lexicon/genders.txt', 'w', encoding = 'utf-8')
	f.write('\n'.join(words))
	f.close()
		
# Run the code if it was executed by console directly!
if (__name__ == '__main__'):
	Run()