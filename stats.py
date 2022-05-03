# File 'stats.py'
# This file will check the stats for the language

import parse

def Run():
	words = parse.Parse('./lexicon/words.txt')
	langdata = {
		"longest": None,
		"shortest": None,
		"letters": {},
		"total": 0,
	}

	for w in words:
		length = len(w)

		if ((not langdata["longest"]) or (len(langdata["longest"]) < length)):
			if (not " " in w):
				langdata["longest"] = w

		if ((not langdata["shortest"]) or (len(langdata["shortest"]) > length)):
			if (not " " in w):
				langdata["shortest"] = w

		langdata["total"] += 1

		for l in w:
			if (l in " -.,ç"):
				continue
			langdata["letters"].update({
				l: langdata["letters"].get(l, 0) + 1
			})

	string = []
	for letter in langdata["letters"].keys():
		string.append("{}: {}".format(letter.upper(), langdata["letters"].get(letter, 0)))

	string.sort()

	print()
	print('Words: {}'.format(langdata["total"]))
	print()
	print(", ".join(string))
	print()
	print("Longest word: {} ({})".format(langdata["longest"], len(langdata["longest"])))
	print("Shortest word: {} ({})".format(langdata["shortest"], len(langdata["shortest"])))



if (__name__ == '__main__'):
	Run()