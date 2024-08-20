# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
Country = set()
for i in range(n):
    Country.add(input())
print(len(Country))
