class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        i = 0
        j = l - 1

        for i in range(l):
            j = l - i - 1
            if i == j:
                return True
            elif i > j:
                return True
            elif s[i] != s[j]:
                return False
            else:
                i, j = i + 1, j - 1

    def longestPalindrome(self, s: str) -> str:
        for size in range(len(s), -1, -1):
            leftover = len(s) - size
            for i in range(leftover + 1):
                substring = s[i:i + size]
                if self.isPalindrome(substring):
                    return substring