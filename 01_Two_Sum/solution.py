from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for l in range(len(nums)):
            complement = target - nums[l]
            if complement in nums[l + 1:]:
                return [l, nums.index(complement, l + 1)]
sol = Solution()
nums = [3, 2, 4]
target = 6
output = sol.twoSum(nums,target)
print(output)
            