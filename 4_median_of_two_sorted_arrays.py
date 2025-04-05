# 4. Median of Two Sorted Arrays
# HARD
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)). 

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a, b = nums1, nums2
        combined_length = len(a) + len(b)
        half_length = combined_length // 2

        if len(b) < len(a):
            a, b = b, a
        
        l, r = 0, len(a) - 1

        while True:
            index_a = (l + r) // 2
            index_b = half_length - index_a - 2

            val_a_l = a[index_a] if index_a >= 0 else float("-infinity")
            val_a_r = a[index_a + 1] if (index_a + 1) < len(a) else float("infinity")
            val_b_l = b[index_b] if index_b >= 0 else float("-infinity")
            val_b_r = b[index_b + 1] if (index_b + 1) < len(b) else float("infinity")

            if val_a_l <= val_b_r and val_b_l <= val_a_r:
                if combined_length % 2:
                    return min(val_a_r, val_b_r)
                return (min(val_a_r, val_b_r) + max(val_a_l, val_b_l)) / 2
            elif val_a_l > val_b_r:
                r = index_a - 1
            else:
                l = index_a + 1