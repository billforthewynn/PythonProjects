# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). 
# For example, is_palindrome("radar") should return True.

def reverse(string):
	target_string = ''
	location = len(string) - 1
	while location >= 0:
		target_string = target_string + string[location]
		location = location - 1
	return target_string

def is_palindrome(palindrome):
	if palindrome == reverse(palindrome):
		return True
	else: 
		return False

print is_palindrome('racecar')