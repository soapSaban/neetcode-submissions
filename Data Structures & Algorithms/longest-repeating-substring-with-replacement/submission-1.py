class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m={}
        maxfreq=0
        l=0
        count=0
        res=0
        for i in range(len(s)):
            m[s[i]]=1+m.get(s[i],0)
            maxfreq=max(maxfreq,m[s[i]])

            while (i-l+1)-maxfreq>k:
                m[s[l]]-=1
                l+=1
                
            count=i-l+1
            res=max(count,res)
        return res


        
