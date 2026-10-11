class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        res=0
        while j<len(prices):
            if prices[i]>prices[j]:
                i,j=j,j+1
            else:
                prof=prices[j]-prices[i]
                res=max(res,prof)
                j+=1
        return res