class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)

        if(s1_length > s2_length):
            return False
        
        s1 = sorted(s1)

        if(s1_length == s2_length):
            return s1 == sorted(s2)

        for i in range(0,s2_length - s1_length+1):
            if s1 == sorted(s2[i:i+s1_length]):
                return True
        
        return False