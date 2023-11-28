from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        # nums[:k].extend(nums[:k])
        # print(nums[:k].extend(nums[:k]))
        return nums

sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3

output = sol.rotate(nums,k)
print(output)