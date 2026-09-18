class Solution:

    def encode(self, strs: List[str]) -> str:
        l=[]
        s=''.join(strs)
        for i in strs:
            count=len(i)
            l.append(count)
        self.l=l
        return s
        

    def decode(self, s: str) -> List[str]:
        F2=[]
        for i in range(len(self.l)):
            F=s[:self.l[i]]
            F2.append(F)
            s=s[self.l[i]:]
        return F2
