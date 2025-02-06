class Solution:
    def jump(self, nums: List[int], jumps=0) -> int:
        for i in range(len(nums)):
            max_jump = nums[i]
            score = len(nums) - 1 - i - max_jump
            if score <= 0:
                if len(nums) == 1:
                    return jumps
                else:
                    return self.jump(nums[:i+1], jumps+1)