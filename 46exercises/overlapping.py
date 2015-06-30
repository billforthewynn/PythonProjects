# Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. 
# You may use your is_member() function, or the in operator, but for the sake of the exercise, 
# you should (also) write it using two nested for-loops.

def summing(numbers):
	running_total = 0
	for n in numbers:
		running_total = running_total + n
	return running_total	

def overlapping(a,b):
	result_set = []
	for x in a:
		for y in b:
			if y == x:
				# print 1
				result_set.append(1)
			else:
				# print 0 
				result_set.append(0)
	if summing(result_set) == 0:
		return False
	else:
		return True	

print overlapping([1,1,1],[3,4,1])