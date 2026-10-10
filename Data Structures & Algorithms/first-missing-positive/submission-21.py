class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num={}
        for n in nums:
            if n > 0:
                if n in num:
                    num[n] += 1
                else:
                    num[n] = 1
        if 1 not in num:
            return 1
        else:
            i = 1
            while i in num:
                i += 1
            return i
        
