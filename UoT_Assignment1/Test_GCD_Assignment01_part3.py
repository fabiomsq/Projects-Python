import unittest
import math
from Assignment01_part3 import my_gcd

#comparing the output of function my_gcd to Python's gcd() function from math package
class TestGCD(unittest.TestCase):

	def test_gdc(self):

		self.assertEqual(my_gcd (39, 91), math.gcd (39, 90))
		self.assertEqual(my_gcd (20, 30), math.gcd (20, 30))
		self.assertEqual(my_gcd (40,40), math.gcd (40,40))

		self.assertEqual(my_gcd (8,4), math.gcd (8,4))

if __name__ == '__main__':
			unittest.main()
