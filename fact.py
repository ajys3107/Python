import time

def factorial(num):
		
		
	if num<0:
		return "Error"
	
	if num<2:
		return 1
		
	else:
		a = 1
		for i in range(1,num +1):
			a *= i
		
	return a	
		
def factorial1(num):
	
	
	if num<0:
		return "Error"
	
	
	if num<2:
		a = 1
		for i in range(1,num +1):
			a *= i
		
		
	else:
		return 1
		
	return a
	
def fun1():
	for i in range(1,1500,2):
		
		a1 = factorial(i)
		
def fun2():

	for i in range(1,1500,2):
	
		a2 = factorial1(i)
		
def check_performance(app):
	l1 = []
	avg_time = []
	for ap in app:
		for i in range(100):
			
			start_time = time.time()
			ap()
			end_time = time.time()
			l1.append(end_time - start_time)
			
		
		avg_time.append(sum(l1)/100)
		
		
	return avg_time
			
print(check_performance([fun1,fun2]))








		
