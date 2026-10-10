class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        else:
            i = 1
            while i in nums:
                i += 1
            return i
        return max(nums)+1
        