class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # [1,1,1,1]
        answer = [1] * len(nums)
        # [1,2,3,4] -> [1,2,6,24]
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]            
        # [1,2,3, 4]
        # [1,2,6,24][0] -> 
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer