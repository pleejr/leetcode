# 20. Valid Parentheses
# EASY
# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true 

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        opener  = ["(", "{", "["]
        closer = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        fifo = []

        try:
            for char in s:
                if char in opener:
                    fifo.append(char)
                else:
                    if closer[char] != fifo.pop():
                        return False
        except IndexError:
            return False
        
        return True if len(fifo) == 0 else False