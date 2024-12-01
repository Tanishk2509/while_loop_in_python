def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1  
    i = 1 
    while i <= n:
        result *= i 
        i += 1  
    
    return result

num = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {num} is {factorial(num)}.")



 