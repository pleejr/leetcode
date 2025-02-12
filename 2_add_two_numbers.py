# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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