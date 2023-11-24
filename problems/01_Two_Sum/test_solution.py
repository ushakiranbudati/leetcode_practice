import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_twoSum_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.sol.twoSum(nums, target), [0, 1])

    def test_twoSum_example2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.sol.twoSum(nums, target), [1, 2])

    def test_twoSum_example3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.sol.twoSum(nums, target), [0, 1])

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
