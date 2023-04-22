from scripts import parse
import json, re

def Run():
	entries = parse.Parse('./lexicon/all.txt', parenthesis = False)
	dictionary = {}

	for e in entries:
		entry = e.split('→')
		origin = entry[0] if len(entry) > 0 else None

		if (not origin): continue

		specification = ''
		try:
			specification = re.search(r'\((.+?)\)', origin).group(1)
		except AttributeError:
			pass

		origin = origin.replace('(' + specification + ')', '')

		trans = entry[1] if len(entry) > 1 else None
		orign = origin if len(entry) > 0 else None

		if (trans and orign):
			origwords = orign.lower().split(',')
			word = trans.lower().split(',')
			for o in origwords:
				words = []
				for w in word:
					words.append(w.strip())
				AddToDict(dictionary, o.strip(), words, specification)

	file = open('./lexicon/dictionary.json', 'w', encoding = 'utf-8')
	json.dump(dictionary, file, indent = 4, ensure_ascii = False)
	file.close()



def AddToDict(dic, word, translations, specification):
	if (not dic.get(word)):
		dic.update({
			word: {
				'entries': [],
			}
		})

	conjoined = ', '.join(translations)
	if (not conjoined in dic[word]['entries'] and not conjoined == ""):
		dic[word]['entries'].append({
			'meaning': conjoined,
			'specification': specification
		})

		
if (__name__ == '__main__'):
	
	Run()