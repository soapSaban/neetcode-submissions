class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        L=sorted(count, key=count.get, reverse=True)
        return L[0:k]