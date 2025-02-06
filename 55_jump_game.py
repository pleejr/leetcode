# recursive solution
class Solution:
    def canJump(self, nums: list[int], index=0) -> bool:
        # base case 1: last index reached
        if index == len(nums) - 1:
            return True
        # base case 2: last index exceeded
        elif index > len(nums) - 1:
            return False
        # index < len(nums) - 1:
        else:
            max_jumps = nums[index]
            # base case 3: 0-jump index
            if max_jumps == 0:
                return False
            # recursive case
            else:
                for i in range(max_jumps, 0, -1):
                    if self.canJump(nums, index + i):
                        return True
                return False
            
# simple solution
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        path_exists = True
        nearest_jump = 0
        for i in range(len(nums)-1, -1, -1):
            max_jump = nums[i]
            if nearest_jump > max_jump:
                nearest_jump += 1
                path_exists = False
            else:
                nearest_jump = 1
                path_exists = True
        return path_exists