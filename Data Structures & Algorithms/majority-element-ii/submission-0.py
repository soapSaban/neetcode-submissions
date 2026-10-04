class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        store=defaultdict(int)
        for num in nums:
            store[num]+=1

            if len(store)<=2:
                continue

            store2=defaultdict(int)
            for num, c in store.items():
                if c>1:
                    store2[num]=c-1
            store=store2
        res=[]

        for n in store:
            if nums.count(n)>len(nums)//3:
                res.append(n)
        return res
            