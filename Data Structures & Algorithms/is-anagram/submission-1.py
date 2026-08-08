class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False
        res = {}
        for i in range(0,len(s)):
            res[s[i]] = res.get(s[i],0)+1
            res[t[i]] = res.get(t[i],0)-1
        
        for value in res.values():
            if value != 0:
                return False
        return True
