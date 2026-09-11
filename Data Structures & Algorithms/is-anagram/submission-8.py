class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS={}
        countT={}
        for i in s:
            countS[i] = 1 + countS.get(i, 0)
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        return countS==countT
            