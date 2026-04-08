class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm = {}
        count = len(s1)

        if(len(s1) == 1):
            return s1 in s2

        if len(s1) > len(s2):
            return False

        if(len(s1) == len(s2)):
            return sorted(s1) == sorted(s2)

        for i in range(0,len(s1)):
            if(s1[i] in hm):
                hm[s1[i]] += 1
            else:
                hm[s1[i]] = 1
            
        for j in range(0,len(s1)):
            if(s2[j] in hm):
                if(hm[s2[j]] > 0):
                    count -= 1
                hm[s2[j]] -= 1

        for k in range(1,len(s2)-len(s1)+1):
            if(count == 0):
                return True

            lowerBound = s2[k-1]
            upperBound = s2[k+len(s1)-1]

            if(lowerBound in hm):
                if(hm[lowerBound] < 0):
                    count -= 1
                hm[lowerBound] += 1
                count += 1

            if(upperBound in hm):
                if (hm[upperBound] > 0):
                    count -= 1
                hm[upperBound] -= 1
        
        if(count == 0):
            return True

        return False




        