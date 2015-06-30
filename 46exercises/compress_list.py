# write function to remove dupes from array (list) of sorted, signed integers

def compress_list(x):
	list_len = len(x)+1
	start = 0 
	to_remove = []
	for i in range(0,list_len):
		# if x[start] == x[start]+1:
		#  	to_remove.append(x[start])
		# print start
		# print x[start]
		# print x[start+1] 
		# start = start + 1 
		print i
	# print to_remove

compress_list([1,1,3])