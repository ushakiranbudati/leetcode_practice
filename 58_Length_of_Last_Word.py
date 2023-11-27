from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = " ".join(s.split())
        return len(s.split()[-1])
s =  "luffy is still joyboy"
sol = Solution()
output = sol.lengthOfLastWord(s)
print(output)