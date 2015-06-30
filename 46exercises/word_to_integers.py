# Write a program that maps a list of words into a list of integers 
# representing the lengths of the correponding words.
# Example ['bad','fart','butthead'] => [3,4,8]

def word_to_integer(a):
	result_set = []
	for x in a:
		result_set.append(len(x))
	return result_set

print word_to_integer(['bad','fart','buttheadddddddddds'])
