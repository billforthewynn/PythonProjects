# A pangram is a sentence that contains all the letters of the English alphabet at least once, 
# for example: The quick brown fox jumps over the lazy dog. 
# Your task here is to write a function to check a sentence to see if it is a pangram or not.

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def clean_string(s):
	preclean_string = s.lower()
	deduped_string = ""
	for letter in preclean_string:
		if letter not in punctuation and letter not in deduped_string:
			deduped_string += letter
	return ''.join(sorted(deduped_string.replace(" ","")))

def check_pangram(s):
	reference_string = 'abcdefghijklmnopqrstuvwxyz'
	if clean_string(s) == reference_string:
		return True
	else:
		return False


print check_pangram('The quick brown fox jumps over the lazy dog.')
