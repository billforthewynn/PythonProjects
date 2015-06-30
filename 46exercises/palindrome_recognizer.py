# Write a version of a palindrome recognizer that also accepts phrase palindromes 
# such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", 
# "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", 
# "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", 
# "Rise to vote sir", or the exclamation "Dammit, I'm mad!". 
# Note that punctuation, capitalization, and spacing are usually ignored.

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def remove_punctuation(s):
	cleaned_string = ""
	for letter in s:
		if letter not in punctuation:
			cleaned_string += letter
	return cleaned_string

def palindrome_recognizer(s):
	staged_s = remove_punctuation(s).lower()
	reversed_s = ''
	loc = len(staged_s) - 1 
	while loc >= 0:
		reversed_s += staged_s[loc]
		loc = loc - 1 
	# return (staged_s.replace(" ",""), reversed_s.replace(" ",""))
	if reversed_s.replace(" ","") == staged_s.replace(" ",""):
		return True
	else:
		return False

print palindrome_recognizer("Dammit, I'm mad!")

