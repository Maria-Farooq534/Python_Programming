#For String

user_input_string = input("Enter a string: ")

user_input_integer = int(input("Enter an Integer: "))

user_input_bool = bool(input("Enter a bool Value (True/False): "))

user_input_float = float(input("Enter a float: "))


print("Given string:" , user_input_string)
print("Given Integer Value:" , user_input_integer)
print("Given Boolean Value:" , user_input_bool)
print("Given Float Value:" , user_input_float)


#Converting it to uppercase

print("Given string in uppercase:" , user_input_string.upper())

# -------------------- For Integer -------------------------

def number_check(number):
    if number % 2 == 0:
        print(f"The number you have entered: {number} is an even number.")
    else:
        print(f"The number you have entered: {number} is an odd number.")


number_check(user_input_integer)

# ---------------------------- For Float ---------------------------

def float_multiply(num):
    return num*2


print("New float Value: " , float_multiply(user_input_float))
