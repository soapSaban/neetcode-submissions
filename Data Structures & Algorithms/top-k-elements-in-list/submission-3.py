class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count={}
       for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
       L=sorted(count, key=count.get, reverse=True)
       return L[:k]
       
        

        