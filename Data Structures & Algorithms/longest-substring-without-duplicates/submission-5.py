class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=[]
        count=0
        res=0
        for i in range(len(s)):
            if s[i] not in m:
                m.append(s[i])
                count+=1
                res=max(res,count)
            else:
                m=m[m.index(s[i]) + 1:]+[s[i]]
                res=max(res,count)
                count=len(m)
        return res
            

