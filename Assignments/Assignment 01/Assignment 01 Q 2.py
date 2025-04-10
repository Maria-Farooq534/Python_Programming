# Question 02 : Part 01

number = int(input("Enter a number: "))

def check_number(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
        
    else:
        
        print(f"{number} is an odd number.")


check_number(number)  #When we use print statement inside the function, we do not need to use print here again.