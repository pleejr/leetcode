class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapping = {}
        diffs = []
        for i in range(len(nums)):
            diff = target - nums[i]
            diffs.append(diff)
            if nums[i] not in mapping:
                mapping[nums[i]] = {i}
            else:
                mapping[nums[i]].add(i)
        print(mapping)
        print(diffs)
        for diff in diffs:
            try:
                index_1 = mapping[diff].pop()
                index_2 = mapping[target - diff].pop()
                return [index_1, index_2]
            except KeyError:
                continue