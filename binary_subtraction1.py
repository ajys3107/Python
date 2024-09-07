def binary_subtract(num1, num2):
    

    result = []
    borrow = 0

    while num1 or num2:
        if num1 != '':
               digit1 = int(num1[-1])
               
        else:
               digit1 = 0
        
        if num2 != '':
               digit2 = int(num2[-1])
               
        else:
               digit2 = 0

        difference = (digit1 - digit2 - borrow) % 2
        borrow = (digit1 - digit2 - borrow) // 2

        result.append(str(difference))

        num1 = num1[:-1] if num1 else ""
        num2 = num2[:-1] if num2 else ""

    if borrow:
        result.append(str(1 - borrow))

    result.reverse()
    return "".join(result)


num1 = "01"
num2 = "01"
result = binary_subtract(num1, num2)
print(result)  
