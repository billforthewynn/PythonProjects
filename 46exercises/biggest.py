def biggest(a,b,c):
	if a > b and a > c: 
		return a
	if b > a and b > c:
		return b 
	else:
		return c

print biggest(1,40000,5)