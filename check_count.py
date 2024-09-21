def check_validity(text):
	l = ['[',']','{','}','<','>','(',')']
	matching_pairs = {'{':'}','(':')','<':'>','[':']'}
	stack = []
	
	if len(text) == 0:
		return 1
	
	for symbol in text:
		if symbol in l:
			if symbol in matching_pairs:
				stack.append(symbol)
				
			elif symbol in matching_pairs.values():
				if stack and matching_pairs[stack[-1]] == symbol:
					stack.pop()
					
				else: 
					return -1
					
			
				
				
	if not stack:
		return 1
	else:
		return -1
	

def check_valid_invalid_text_count(list_text):
	valid_count = 0
	invalid_count = 0 
	
	for text in list_text:	
		if check_validity(text) == 1:
			valid_count += 1
			
		else:
			invalid_count += 1
			
	return valid_count,invalid_count
		
list_text = ['[{(','()']
valid_count,invalid_count = check_valid_invalid_text_count(list_text)
print ((valid_count,invalid_count))
	 


	
