# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(a):
	result_set = []
	for x in a:
		result_set.append(len(x))
	return max(result_set)

print find_longest_word(['this','is','a','sentence'])