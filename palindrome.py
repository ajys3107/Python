def check_count(l):
	count = 0
	s = [list,tuple,set]
	for obj in l:
		if type(obj) in s:
			for item in obj:
				if type(item) == str:
					count += palindrome(item)
	
	
	for obj in l:
		if type(obj) == str:
			count += palindrome(obj)
			
	return count
	
	
def palindrome(obj):

	if len(obj)%6 == 3:
			if obj == obj[::-1]:
				return 1
					
	return 0
	
print(check_count(['aaa']))
