def counter(string,substring,key):
	count = 0
	if key==True:
		for i in range(len(string)- len(substring) + 1):
			if string[i:i + len(substring)] == substring:
				count = count + 1
		return count
		
	else:
		r = string.count(substring)
		
		return r
		
print(counter("sgggs","gg",False))
