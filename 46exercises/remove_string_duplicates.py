# remove duplicates from string

def remove_duplicates(s):
	new_str = ''
	for i in s:
		if i not in new_str:
			new_str += i 
	return new_str

print remove_duplicates('assssssssssssssssssssskkkkkaaaaa')