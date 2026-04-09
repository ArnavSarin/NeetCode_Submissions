class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if(len(s)<=1):
            return len(s)

        left, right = 0, 1
        max_length = 1
        while right < len(s):
            if s[right] not in s[left:right]:
                right += 1
                max_length = max(max_length, len(s[left:right]))
            else:
                left += 1
                right = left + 1 
        return max_length


        

