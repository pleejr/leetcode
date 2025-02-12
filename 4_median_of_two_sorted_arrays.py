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