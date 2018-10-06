""" Script: Assignment01_part1_1
   	Description: This script is responsible to read a list of any kind and print out each
	item in a list on a separate line.
   	Created by: Fábio Queiroz
   	Creation Date: 19.09.2018
   	Version: 1.0
"""
# Declaring an empty List
my_list = []

# Different type of List

# String List
my_list = ['apples', 'oranges', 'bananas', 'watermelons']

# Integer List
#my_list = [2,4,6,8,10]

# Float List
#my_list = [1.5,2.5,3.5,4.5]

# List length
len = len(my_list)

# Print each item of the List
for i in range(len):
    print("The item", i, "is:", my_list[i])
