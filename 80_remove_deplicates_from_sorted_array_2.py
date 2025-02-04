class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if i < 2:
                return len(nums)
            if nums[i] == nums[i - 1] == nums[i - 2]:
                del nums[i]