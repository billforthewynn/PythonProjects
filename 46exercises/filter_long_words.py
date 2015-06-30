# Write a function filter_long_words() that takes a list of words 
# and an integer n and returns the list of words that are longer than n.

def filter_long_words(x,n):
	result_set = []
	for i in x:
		if len(i) > n:
			result_set.append(i)
	return result_set

print filter_long_words(['this','is','a','sentence'],1)


