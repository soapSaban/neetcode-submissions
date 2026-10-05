class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1=len(nums1)-1
        n2=len(nums2)-1

        for i in range(len(nums2)):
            nums1[n1]=nums2[n2]
            n2-=1
            n1-=1
        nums1.sort()
            
            

