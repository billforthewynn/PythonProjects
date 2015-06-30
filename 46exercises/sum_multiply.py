# Define a function sum() and a function multiply() that sums and multiplies (respectively) 
# all the numbers in a list of numbers. 
# For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

input_list = [1,2,3,4]

def sum(numbers):
	running_total = 0
	for n in numbers:
		running_total = running_total + n
	return running_total	

print sum(input_list)

def multiply(numbers):
	multiplying_total = 1
	for n in numbers:
		multiplying_total = multiplying_total * n
	return multiplying_total

print multiply(input_list)