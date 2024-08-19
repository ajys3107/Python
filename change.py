def change_case(text,style):

	if(style=='C' or style=='c'):
		list_string = list(text)
		for i in range(len(text)):
			list_string[i] = list_string[i].capitalize()
			
			result_capital = ''.join(list_string)
		return result_capital
		
	if(style=='S' or style=='s'):
		list_string = list(text)
		for i in range(len(text)):
			list_string[i] = list_string[i].casefold()
			
			result_small = ''.join(list_string)
		return result_small
		
	if(style=='R' or style=='r'):
		list_string = list(text)
		for i in range(len(text)):
		
			if(list_string[i] == list_string[i].capitalize()):
				
				list_string[i] = list_string[i].casefold()
				
				result_random=''.join(list_string)
				
			else:
			
				list_string[i] = list_string[i].capitalize()
				
				result_random=''.join(list_string)
		return result_random
		
		
	if(style=='Z' or style=='z'):
		list_string = list(text)
		for i in range(len(text)):
			if(list_string[0] == list_string[0].capitalize()):
					
				list_string[i] = list_string[i].casefold()
				
				result_random=''.join(list_string)
					
			elif(list_string[0] == list_string[0].casefold()):
					
				list_string[i] = list_string[i].casefold()
				
				result_random=''.join(list_string)
					
		return result_random
				
				
		
	
			
print(change_case('SgGs','R'))
