class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''.join(strs)
        L=[]
        for i in strs:
            count=len(i)
            L.append(count)
        self.L = L  
        return s
             
    def decode(self, s: str) -> List[str]:
        F2 = []

        for i in range(len(self.L)):
            F = s[:self.L[i]]
            F2.append(F)
            s = s[self.L[i]:]

        return F2




        
       
