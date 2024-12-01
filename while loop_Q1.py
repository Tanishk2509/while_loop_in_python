def reverse_number(num):
    reversed_num = 0
    
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num
    
    while num != 0:
        digit = num % 10              
        reversed_num = reversed_num * 10 + digit 
        num = num // 10                 
    
    if is_negative:
        reversed_num = -reversed_num
    return reversed_num

number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print(f"The reversed number is: {reversed_number}")
