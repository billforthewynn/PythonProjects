def is_friend(x):
	if x[0] == 'D':
		return True
	if x[0] == 'N':
		return True
	else:
		return False

print is_friend('Dennis') 