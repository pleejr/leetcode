# 55. Jump Game
# MEDIUM
# https://leetcode.com/problems/jump-game/

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise. 

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index. 

# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

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