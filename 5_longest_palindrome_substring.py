# 5. Longest Palindromic Substring
# MEDIUM
# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s. 

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb" 

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

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