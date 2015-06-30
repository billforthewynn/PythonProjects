# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

import sys

letter = sys.argv[1]

def vowel_checker(n):
	vowels = ['a','e','i','o','u']
	if len(letter) != 1:
		return 'Must use a single character!'
	else:
		if letter in vowels:
			return True
		else:
			return False

print vowel_checker(letter)