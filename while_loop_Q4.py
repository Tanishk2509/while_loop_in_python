total_sum = 0  

while True:  
    number = float(input("Enter a number (enter 0 to stop): "))
    
    if number == 0:  
        break
    total_sum += number  

print(f"The sum of all the numbers is: {total_sum}")
