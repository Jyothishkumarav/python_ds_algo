class Solution:
    def hasDuplicate(self, nums: list[int]):
        if len(nums) > len(set(nums)):
            return True
        return False
    