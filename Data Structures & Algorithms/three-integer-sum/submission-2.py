class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        result=[]
        for i in range(len(nums)-2):
            L=i+1
            R=len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                    continue
            while L<R:
                total=nums[i]+nums[L]+nums[R]
                if total==0:
                    result.append([nums[i],nums[L],nums[R]])
                    L+=1
                    R-=1
                    while nums[R] == nums[R + 1] and L < R:
                        R -= 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
                elif total<0:
                    L+=1
                else:
                    R-=1
        return result