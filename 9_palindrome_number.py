# 9. Palindrome Number
# EASY
# https://leetcode.com/problems/palindrome-number/

# Given an integer x, return true if x is a palindrome, and false otherwise. 

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome. 

# Constraints:
# -231 <= x <= 231 - 1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        elements = []

        if abs(x) != x:
            return False

        while x != 0:
            mod = x % 10
            elements.append(mod)
            x = x // 10

        for i in range(len(elements)//2):
            if elements[i] != elements[len(elements)-1-i]:
                return False

        return True
    
x = -121
tmp = Solution()
print(tmp.isPalindrome(x))