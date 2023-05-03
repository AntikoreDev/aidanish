# File 'keys.py'
# This file will create 3 character long keys to be used in games.

import parse
import sys

def Run():
	words = parse.Parse('./lexicon/words.txt')
	count = 20 if not len(sys.argv) > 1 else int(sys.argv[1])
	
	# Available letters
	letters = "abcdefghijklmnopqrstuvxyz"
	vowels = "aeiou"
	keys, useful = [], []

	for i in letters:
		for j in letters:
			for k in letters:
				if (i not in vowels and j not in vowels and k not in vowels):
					continue
				keys.append(str(i + j + k))
	
	for key in keys:
		amount = 0
		for w in words:
			if (key in w):
				amount += 1
				if (amount >= count):
					break
		
		if (amount >= count):
			useful.append(key.upper())

	print('["' + '", "'.join(useful) + '"]')
	print(len(useful))
	
if (__name__ == '__main__'):
	Run()