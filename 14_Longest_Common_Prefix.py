from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        for char_tuple in zip(*strs):
            if len(set(char_tuple)) == 1:
                prefix += char_tuple[0]
            else:
                break

        return prefix
strs = ["flower","flow","flight"]
sol = Solution()
output = sol.longestCommonPrefix(strs)
print(output)


