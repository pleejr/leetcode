class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                return len(nums)
            if nums[i] == nums[i - 1]:
                del nums[i]