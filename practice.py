# 1. Accepts a list of integers from the user. 
length_of_list = int(input("Enter Length of the list : ")) 
 
integer_list = [] 
 
 
for i in range(length_of_list): 
    nums =int(input(f"Enter element {0 + i} : ")) 
    integer_list.append(nums) 
 
 
print(f"\nComplete Integer List is {integer_list}") 
 
# 2. Loops through the list and prints out each number. 
print("\nPrinting Each Number Of The List\n") 
for i in integer_list: 
 
# 3. number is greater than 10 will skip 
    if i > 10 and i!=20: 
        print(f"Elements of the list {i} is Skipping") 
        continue 
    
    # 4. loop stop if the number is 20 
    if i == 20: 
        print(f"Loop Breaks at {i}") 
    break 
 
print(f"Elements of the list is {i}") 
 
# 5. After the loop ends, print a message that the loop ended naturally. 
print("The Loop Ended Naturally.") 