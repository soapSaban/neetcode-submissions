class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        summ = 0
        prefix = {0: 1}

        for n in nums:
            summ += n
            diff = summ - k

            if diff in prefix:
                res += prefix[diff]

            if summ in prefix:
                prefix[summ] += 1
            else:
                prefix[summ] = 1

        return res



        

        