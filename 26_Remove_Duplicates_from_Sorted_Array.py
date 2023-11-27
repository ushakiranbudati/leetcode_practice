from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current_position = 1

        for i in range(1, len(nums)):
            print(nums[i] != nums[i - 1],nums[i],nums[i - 1],i)
            if nums[i] != nums[i - 1]:
                nums[current_position] = nums[i]
                current_position += 1

        return current_position


sol = Solution()
nums =[3,2,2,3]
output = sol.removeDuplicates(nums)
print(output)



