class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        strMap = {}
        strMap2 = {}
        for i in range (0,len(s)):
            if(s[i] in strMap):
                strMap[s[i]] = strMap[s[i]] + 1
            else:
                strMap[s[i]] = 1
            
            if(t[i] in strMap2):
                strMap2[t[i]] = strMap2[t[i]] + 1
            else:
                strMap2[t[i]] = 1
        
        return strMap == strMap2