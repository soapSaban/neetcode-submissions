class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        need = {}
        window = {}
        valid = True
        for i in t:
            need[i]=1+need.get(i,0)
        min_len = float('inf')
        start = 0
        for r in range(len(s)):
            if s[r] in need:
                window[s[r]]=1+window.get(s[r],0)
            valid = True

            for c in need:
                if window.get(c, 0) < need[c]:
                    valid = False
                    break
            while valid:
                curr_len=r-l+1
                if curr_len < min_len:
                    min_len = curr_len
                    start = l
                if s[l] in need:
                    window[s[l]]-=1
                l+=1
                valid = True
                for c in need:
                    if window.get(c, 0) < need[c]:
                        valid = False
                        break
        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]