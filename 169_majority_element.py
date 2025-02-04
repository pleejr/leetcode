class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        majority = len(nums) / 2
        for i in nums:
            if i not in elements:
                elements[i] = 1
            else:
                elements[i] += 1
            if elements[i] > majority:
                return i