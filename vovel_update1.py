def vovels(l):
	
	count = 0
	
	list_ = [list,tuple,set]
	
	for item in l:
		if type(item) in list_:
			for char in item:
				if type(char) == str:
					count += valid_vovel(char)
					
		
	
	for item in l:
		if type(item) == str:
			count += valid_vovel(item)
			
	return count
	
def valid_vovel(obj):
	vovel = ['a','e','i','o','u']
	counter = {}
	d = {}
	
	count = 0
	for char in obj:
		if char not in counter:
			counter[char] = 0
					
		counter[char] += 1
				
	for char in counter:
		if char in vovel:
			d[char] = counter[char]
					
	values = list(d.values())
			
	if values and len(set(values)) == 1:
	
		count += 1
		
	elif values:
		count += 1
		
	return count
	
	
print(vovels(['aauu','abcde','d',['au']]))





