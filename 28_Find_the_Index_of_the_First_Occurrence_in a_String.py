class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
sol = Solution()
haystack = "leetcode"
needle = "leeto"
output = sol.strStr(haystack,needle)
print(output)



