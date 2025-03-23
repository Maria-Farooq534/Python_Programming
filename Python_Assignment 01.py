#Question no 01 : Part 01
#Reverse String
#Method 01 : Using Function

'''
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

'''

#Question 01 : Part 02
#Numbers of vowels in the string
user_input_string = input("Enter a string: ")
#Method 01
sum_of_vowels = ''
for vowel in user_input_string:
    if vowel.lower() in ['a','e','i','o','u']:
        print("Number of vowels: " , vowel)
        sum_of_vowels += vowel
print("Number of vowels: " , len(sum_of_vowels))
        

#Method 02 : Using a Function
print("Method 02 : Counting number of vowels using a function:")

def check_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)
print("The vowels in the string: " , check_vowels(user_input_string))