# Define a function reverse() that computes the reversal of a string. 
# For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse(string):
	target_string = ''
	location = len(string) - 1
	while location >= 0:
		target_string = target_string + string[location]
		location = location - 1
	return target_string

print reverse("go hang a salami I'm a lasagna hog")	
