class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except ValueError:
                return len(nums)