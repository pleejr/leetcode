# 2. Add Two Numbers
# MEDIUM
# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        val1 = 0
        val2 = 0

        i = 0
        while l1:
            multiplier = 10 ** i
            val1 += l1.val * multiplier
            l1 = l1.next
            i += 1

        i = 0
        while l2:
            multiplier = 10 ** i
            val2 += l2.val * multiplier
            l2 = l2.next
            i += 1
        
        sum = val1 + val2

        if sum == 0:
            return ListNode(0)
        while sum > 0:
            remainder = sum % 10
            result.append(remainder)
            sum //= 10

        result.reverse()
        nextNode = ListNode(result[0])
        for digit in result[1:]:
            node = ListNode(digit, nextNode)
            nextNode = node

        return nextNode