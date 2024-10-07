import time

def get_even_odd_count1(l):
	count_even = 0
	count_odd = 0
	for obj in l:
		if obj%2 == 0:
			count_even += 1
			
		else:
			count_odd += 1
	return count_even,count_odd
	
def get_even_odd_count2(l):
	count_even = 0
	count_odd = 0
	for obj in l:
		if obj&1 == 0:
			count_even += 1
			
		else:
			count_odd += 1
		

#print(get_even_odd_count([1,2,3,4]))

def get_even_odd_count3(l):
	count_even = 0
	count_odd = 0
	for obj in l:
		t = obj%2
		count_even = 1 - t
		count_odd = t
		
	return count_even,count_odd


def check_performance(approches):
	t = []
	avg_time = []
	for approch in approches:
		for i in range(100):
			start_time = time.time()
			approch([1,2,3,4])
			end_time = time.time()
			t.append(end_time-start_time)
		
		avg_time.append(sum(t)/100)
		
	return avg_time
		
print(check_performance([get_even_odd_count1,get_even_odd_count2,get_even_odd_count3]))
