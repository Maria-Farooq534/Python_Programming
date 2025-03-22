#Question no 01 : Part 01
#Reverse String
#Method 01 : Using Function

user_input_string = input("Enter a string: ")
def reversed_string(string):
    return string[::-1] # start, stop and step.. step of -1 will start from backward direction.
print("The reversed string is : " ,reversed_string(user_input_string))

#Method 02 : Using For loop
print("Reverse string using for loop: ")
reverse_user_string = ''
for char in user_input_string:
    reverse_user_string = char + reverse_user_string
print(f"User reversed string is: {reverse_user_string}")
#nn
