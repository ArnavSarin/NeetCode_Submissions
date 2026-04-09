class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if(len(s)<=1):
            return len(s)

        left, right = 0, 1
        # seen = [s[left]]
        max_length = 1
        # print(seen)
        while right < len(s):
            if s[right] not in s[left:right]:
                # seen.append(s[right])
                right += 1
                max_length = max(max_length, len(s[left:right]))
            else:
                left += 1
                right = left + 1 
                # seen.pop(0)
            # print(seen)
        return max_length


        

