""" Script: Assignment01_part1_2
   	Description: This script is responsible to generate a list of integers from 0 to 5,
    reverse the list and print it out.
   	Created by: Fábio Queiroz
   	Creation Date: 19.09.2018
   	Version: 1.0
"""
# Declaring an empty List
my_list = []

# list length
len = 6

# Generating a list of integers using the function append() (length = 6; [0-5])
for i in range(len):
	my_list.append(i)

# Reversing the list (my_list) of integers using the function reverse() (from [0-5] to [5-0])
my_list.reverse()

# Printing the reversed list
print(my_list)
