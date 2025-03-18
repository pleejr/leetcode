class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        specials = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        i = 0
        while i < len(s):
            if i+1 < len(s):
                tmp = s[i] + s[i+1]
                if tmp in specials:
                    result += specials[tmp]
                    i += 2
                    continue
            result += symbols[s[i]]
            i += 1
        return result

tmp = Solution()
print(tmp.romanToInt("IV"))