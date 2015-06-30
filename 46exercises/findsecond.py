# Find the second occurence 

string = "Funny, this is a funny funny string."

def find_second(target_string, search):
	target_string = target_string.lower()
	first_occurence = target_string.find(search)
	return target_string.find(search,first_occurence +1)

print find_second(string, 'funny')
