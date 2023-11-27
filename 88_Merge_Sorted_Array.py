# 88. Merge Sorted Array
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = sorted(nums1[0:m].extend(nums2[0:n]))
        # return sorted(nums1[:m]+nums2[:n])
        nums1[m:] = nums2[:n]
        nums1.sort()
        return nums1

sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3
output = sol.merge(nums1, m, nums2, n)
print(output)
