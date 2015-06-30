# Write a function is_member() that takes a value (i.e. a number, string, etc) x 
# and a list of values a, and returns True if x is a member of a, False otherwise. 
# (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)

def summing(numbers):
	running_total = 0
	for n in numbers:
		running_total = running_total + n
	return running_total	

def is_member(x,a):
	result = []
	for i in a:
		if x == i:
			result.append(1)
		else:
			result.append(0)
	if summing(result) == 0:
		return False
	else:
		return True

print is_member('a',[0,0,0,'a',1])

		