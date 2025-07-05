# #Question 3: Loops
# Write a Python program that:
# 1. Accepts a list of integers from the user.
# 2. Loops through the list and prints out each number.
# 3. If a number is greater than 10, skips it using the continue statement.
# 4. Stops the loop if the number is 20 using the break statement.
# 5. After the loop ends, prints a message that the loop ended naturally.

# # 1. Accepts a list of integers from the user.

length_of_list = int(input("Enter length of list: "))

integer_list = []

for i in range(1, length_of_list + 1):
    number = int(input(f"Enter number {i} : "))
    integer_list.append(number)

print(f"\nThe list of integers: {integer_list}")
# # 2. Loops through the list and prints out each number.
print(f"The numbers in list are:\n")
for num in integer_list:
    print(num)


    

# # 3. If a number is greater than 10, skips it using the continue statement.
print("\nSkipping numbers:")
new_list = []
for num in integer_list:
    if num > 10 and num != 20:
        print(f"Skip the number {num} as it is greater than 10.")
        continue
    new_list.append(num)
print(f"\nNew list after skipping numbers greater than 10 is : {new_list}")

# 4. Stops the loop if the number is 20 using the break statement.
for num in new_list:
    if num == 20:
        print(f"Stop the loop as the number is 20")
        break
    print(f"Number: {num}")
    # 5. After the loop ends, prints a message that the loop ended naturally.
else:
    print("The loop ended naturally without encountring 20.")



