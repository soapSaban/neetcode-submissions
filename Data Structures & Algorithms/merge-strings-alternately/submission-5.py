class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output=''
        for i in range(len(min(word1, word2, key=len))):
            output+=(word1[i]+word2[i])
        output+=max(word1[(i+1):],word2[(i+1):], key=len)
        return output
