#Using Anaconda
import numpy as np
#Virtual environment setup
def setup_virtual_environment():
    print("Create virtual environment using anaconda by running this command: ")
    print("conda create -n sortenv pythoun==3.12 ")
    print("Activate Environment: ")
    print("conda activate sortenv")
    print("Install Python library: Numpy")
    print("!pip install numpy as np")

#Sorting array
def sort_list(arr):
    return np.sort(arr)

#Taking input from user
try:
    user_input = input("Enter a list of integers seperated by space: ")
    num_list = list(map(int, user_input.split()))
    setup_virtual_environment()
    print("Sorted list: " , sort_list(num_list))
except ValueError:
    print("Invalid Input!")