#DFA

alpha = {'a','b'}

def q0(text):
	if len(text)>0:
		symbol = text[0]
		if symbol in alpha:
			if symbol == 'a':
				return q0(text[1:])
			
			else:
				return q1(text[1:])
				
		else:
			return "Rejected"
			
	else:
		return q0
		
def q1(text):
	if len(text)>0:
		symbol = text[0]
		if symbol in alpha:
			
			if symbol == 'b':
				return q1(text[1:])
				
			else:
				return q0(text[1:])
				
		else:
			return "Rejected"
			
	else:
		return q1
		
		
def dfa(text):
	
	result = q0(text)
	if result == q1:
		return "Accepted"
		
	else:
		return "Rejected"
		
print(dfa('abab'))


#--------------------------------------------------------------------------------------

# int to rome 

def intToRoman(num: int):
        Result = ""
        Values = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        Symbols = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        Number = len(Values) - 1
        while num:
            quotient = num // Values[Number]
            num %= Values[Number]

            while quotient:
                Result += Symbols[Number]
                quotient -= 1

            Number -= 1

        return Result

print(intToRoman(123))

#----------------------------------------------------------------------------------------

#slice

def slice_string(object,start,end,step):
	text=""
	for i in range(start,end,step):
		text+=object[i]
	return text
	
def con1(object,slicing_parameter):
	step =1
	fist = 0
	last =len(object)
	return slice_string(object,fist,last,step)
	
def con2(object,slicing_parameter):
	step = slicing_parameter[2]
	first = slicing_parameter[0]
	last = slicing_parameter[1]
	return slice_string(object,first,last,step)
	
	
	

		

print(con2("chaitanya",[len("chaitanya")-1,-1,-1]))

#-------------------------------------------------------------------------------------------

#base

def base(text, text_base, output_base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    if not (2 <= text_base <= 36) and (2 <= output_base <= 36):
        print('Base must be between 2 and 36')

    dec = int(text, text_base)

    while dec > 0:
        rem = dec % output_base
        res = digits[rem] + res
        dec //= output_base

    return res


print(base('1100', 2, 16))
	
	
	
			
		
