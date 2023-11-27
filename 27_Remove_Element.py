# Top Interview 150
# 27. Remove Element
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current_position = 0
        for i in range(len(nums)):
            # If the current element is not equal to val, update the list in-place
            if nums[i] != val:
                print(nums[current_position],nums[i])
                nums[current_position] = nums[i]
                current_position += 1

        # The length of the modified list is equal to the current position
        return current_position

sol = Solution()
nums =[3,2,2,3]
val = 3
output = sol.removeElement(nums,val)
print(output)