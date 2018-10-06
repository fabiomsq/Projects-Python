""" Function: my_gdc()
   	Description: This function is responsible to take parameters and returns their
	greatest common divisor.
	Created by: Fábio Queiroz
   	Creation Date: 19.09.2018
   	Version: 1.0
"""

# Defining the function my_gcd()
def my_gcd(a,b):
    # Reversing the tuple e.g (a == 39; b == 91) --> (91,39)
	my_list = a,b
	ord = sorted(my_list, reverse=True)
	# int1 will be the dividend and int2 will be the divider e.g. (91/39)
	int1 = ord[0]
	int2 = ord[1]

		# Checking the most basic scenario, remainder == 0
	remainder = (int1%int2)
	if (remainder == 0):
		gcd = int2
	""" Checking until the remainder is greater than 0. If the remainder is equal to 0 than break and
	    gcd = int2.
	"""
	while (remainder > 0):
	    int1 = int2
	    int2 = remainder
	    remainder = (int1%int2)
	    if (remainder == 0):
	        gcd = int2

	return gcd

# #Invoking the function GCDs
# gcd_result = my_gcd(1320, 1150)
# print ("The GCD is", gcd_result)
