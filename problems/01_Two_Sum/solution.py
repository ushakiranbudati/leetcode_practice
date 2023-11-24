from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for l in range(len(nums)):
            sub_values = target - nums[l]
            if sub_values in nums[l + 1:]:
                return [l, nums.index(sub_values, l + 1)]
sol = Solution()
nums = [3, 2, 4]
target = 6
output = sol.twoSum(nums,target)
print(output)
            