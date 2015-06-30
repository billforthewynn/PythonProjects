# prime_factor
# first define a function to test if number is prime

def is_prime(n):
	x = n - 1

	while x > 1:
		if n % x == 0:
			return False
			break
		x -= 1
	else: 
		return True

#print is_prime(int(raw_input("Enter number: ")))


n = int(raw_input("Enter number: "))

f = n - 1 



while f > 1:
	if is_prime(n) == True:
		print str(n)+' is a prime number.' 
		break 
	if is_prime(f) == True and n % f == 0:
		print f
	f -= 1

