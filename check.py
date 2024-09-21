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
		
t = '{[('
print(check_validity(t))	
