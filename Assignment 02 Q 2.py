# #Question 02 
# Question 2: Operators
# Write a Python program that:
# 1. Accepts two numbers as input from the user.
# 2.  Performs  and  prints  the  result  of  all  arithmetic  operations  (addition,  subtraction,  multiplication,  division,
# modulus, floor division) between these two numbers.
# 3. Uses comparison operators to check if the first number is greater than the second, and if they are equal.
# 4. Uses logical operators to combine two conditions (e.g., the first number is greater than the second, and the
# second number is less than 10).

# 1. Accepts two numbers as input from the user.

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

# 2.  Performs  and  prints  the  result  of  all  arithmetic  operations  (addition,  subtraction,  multiplication,  division,
# modulus, floor division) between these two numbers.

#Addition
addition = number1 + number1
print(f"{number1} + {number2} is = {addition}")
#Subtraction
subtraction = number1 - number2
print(f"{number1} - {number2} is = {subtraction}")
#Multiplication
multiplication = number1 * number2
print(f"{number1} * {number2} is = {multiplication}")
#Division
division = number1 / number2
print(f"{number1} / {number2} is = {division}")
#Modulus
modulus = number1 % number2
print(f"{number1} % {number2} is = {modulus}")
#Floor division
floor_division = number1 // number2
print(f"{number1} // {number2} is = {floor_division}")

# 3. Uses comparison operators to check if the first number is greater than the second, and if they are equal.
if number1 >= number2:
    print(f"{number1} is greater than {number2}")
elif number1 == number2:
    print(f"{number1} is equal to {number2}")
else:
    print(f"{number1} is less than {number2}")

# 4. Uses logical operators to combine two conditions (e.g., the first number is greater than the second, and the
# second number is less than 10).

if number1 > number2 and number2 < 10:
    print(f"{number1} is greater than {number2} and {number2} is less than 10.")
elif number1 > number2 and number2 > 10:
    print(f"{number1} is greater than {number2} and {number2} is greater than 10.")
elif number1 < number2 or number2 > 10:
    print(f"{number1} is greater than {number2} and {number2} is greater than 10.")
elif number1 < number2 and number2 > 10:
    print(f"{number1} is greater than {number2} and {number2} is greater than 10.")
else:
    print("Condition not met!")
