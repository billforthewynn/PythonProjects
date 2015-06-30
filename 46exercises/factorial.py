def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		x = n 
		while n >= 2:
			n = n - 1 
			x = x * n
		return x 

print factorial(1)	
