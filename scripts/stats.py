# File 'stats.py'
# This file will check the stats for the language

from scripts import parse

def Run():
	words = parse.Parse('./lexicon/words.txt')
	langdata = {
		"longest": None,
		"shortest": None,
		"letters": {},
		"ends": {},
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

		lastletter = None
		for l in w:
			if (l in " -.,ç"):
				continue
			lastletter = l
			langdata["letters"].update({
				l: langdata["letters"].get(l, 0) + 1
			})

		if (lastletter):
			langdata["ends"].update({
				lastletter: langdata["ends"].get(lastletter, 0) + 1
			})


	string = []
	for letter in langdata["letters"].keys():
		string.append("{}: {}".format(letter.upper(), langdata["letters"].get(letter, 0)))

	ends = []
	for letter in langdata["ends"].keys():
		if (langdata["ends"][letter] > 25):
			ends.append(letter.upper())

	string.sort()

	print()
	print('Words: {}'.format(langdata["total"]))
	print()
	print(", ".join(string))
	print()
	print("Longest word: {} ({})".format(langdata["longest"], len(langdata["longest"])))
	print("Shortest word: {} ({})".format(langdata["shortest"], len(langdata["shortest"])))
	print()
	print("Ends: [\"{}".format("\", \"".join(ends)) + "\"]")
	print(("Letters: [\"{}".format("\", \"".join(langdata["letters"].keys())) + "\"]").upper())



if (__name__ == '__main__'):
	Run()