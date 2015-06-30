# Write a function translate() that will translate a text into roversprakt (Swedish for "robber's language"). 
# That is, double every consonant and place an occurrence of "o" in between. 
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".
# Try for a single letter first
# Then word
# Then sentence 

import sys

text = sys.argv[1]

def translate(word):
	translated_word = []
	vowels = ['a','e','i','o','u',' ']
	for letter in word:
		if letter in vowels:
			translated_word.append(letter)
		else:
			translated_word.append(letter+'o'+letter)
	final_word = ''.join(translated_word)
	return final_word

print translate(text)  


