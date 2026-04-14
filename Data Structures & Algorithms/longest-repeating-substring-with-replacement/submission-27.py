class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if(len(s)<=k):
            return len(s)

        hash_map = {}
        left,right = 0,0
        ans = 0
        maxf = 0

        while right<len(s):
            hash_map[s[right]] = 1 + hash_map.get(s[right],0)
            maxf = max(maxf,hash_map[s[right]])

            while right - left + 1 - maxf > k: 
                hash_map[s[left]] -= 1
                left += 1
            ans = max(ans,right-left+1)
            right += 1

        return ans

            


        