#Question no 01 : Part 01
#Reverse String
'''
user_input_string = input("Enter a string: ")
def reversed_string(string):
    return string[::-1] # start, stop and step.. step of -1 will start from backward direction.
reversed_string(user_input_string)
'''
def reverse_string(strings):
    return strings[::-1]  # Start , stop , step
user_input = input("Enter a string: ") # Hello Python
reverse_string(user_input)