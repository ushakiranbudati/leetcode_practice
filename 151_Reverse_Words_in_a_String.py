class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        a = [ b for b in a[::-1]]
        return " ".join(a)

sol = Solution()
s = "a good   example"
output = sol.reverseWords(s)

print(output)


