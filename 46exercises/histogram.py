# Define a procedure histogram() that takes a list of integers and 
# prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def generate_n_chars(n,c):
	result = []
	x = 0 
	while x < n:
		result.append(c)
		x = x + 1
	print ''.join(result)	

def histogram(x):
	for i in x:
		generate_n_chars(i,'*')
		# print i 

histogram([4,9,700])