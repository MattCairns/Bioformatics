def txtToString(filename):
	'''
	Takes a text file and returns a string version of that file
	Returns: string
	'''
	text_file = open(filename, 'r')
	return text_file.read()