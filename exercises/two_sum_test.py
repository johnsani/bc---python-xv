#using TDD to test our two_sum algorithm
import unittest
from two_sum import two_sum
class TwoSumTestSuite(unittest.TestCase):
	#You should always prefix your test case function with the word 'test'
	def test_list_range_4(self):
		res = two_sum([2, 5, 1, 7], 8)
		self.assertEqual(res, [2, 3])

	def test_list_range_5(self):
		result = two_sum([7, 9, 10, 8, 6], 18)
		self.assertEqual(result, [2, 3])

	def test_list_range_6(self):
		result = two_sum([2, 9, 15, 8, 6, 7], 13)
		self.assertEqual(result, [4, 5])

	def test_list_range_7(self):
		result = two_sum([1, 10, 10, 8, 6, 5, 4], 12)
		self.assertEqual(result, [3, 6])

if __name__ == '__main__':
	unittest.main()