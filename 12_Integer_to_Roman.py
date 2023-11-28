class Solution:
    def get_roman(self, num: int) -> tuple:
        roman = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
        for r in list(roman.keys())[::-1]:
            if roman[r] <= num:
                return roman[r], r

    def intToRoman(self, num: int) -> str:
        out = ""
        count = num
        while count > 0:
            c, r = self.get_roman(count)
            count = count - c
            out = out + r
        return out

sol = Solution()
s = 1994
output = sol.intToRoman(s)

print(output)
