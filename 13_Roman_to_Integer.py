class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        val = 0
        n = len(s)
        for i in range(n - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                val -= roman[s[i]]
            else:
                print(val)
                val += roman[s[i]]

        val += roman[s[n - 1]]  # Add the value of the last character
        return val

sol = Solution()
s = "MCMXCIV"
output = sol.romanToInt(s)

print(output)
