# write function that receives string and print true if palindrome else false


def palindrome(str):
    
    return str == str[::-1]

input_string = input("Enter string: ")
result = palindrome(input_string)

if result:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
