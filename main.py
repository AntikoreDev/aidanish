# File 'main.py'
# This file will run almost all the rest of scripts.

import words, done, all, genders, jsondict

# Perform the execution of scripts
def Run():
	all.Run()
	words.Run()
	done.Run()
	genders.Run()
	jsondict.Run()

if (__name__ == '__main__'):
	Run()