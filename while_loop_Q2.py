def is_palindrome(number):
    num_str = str(number)
    
    if num_str == num_str[::-1]:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
