class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower().replace(' ','')
        pointer_a = 0
        pointer_b = len(t) - 1

        while pointer_a != pointer_b and pointer_a < len(t) and pointer_b >= 0:
            while not t[pointer_a].isalnum() and pointer_a+1 < len(t):
                pointer_a += 1
            while not t[pointer_b].isalnum() and pointer_b-1 >= 0:
                pointer_b -= 1
            if t[pointer_a].isalnum() and t[pointer_b].isalnum() and t[pointer_a] != t[pointer_b]:
                return False 
            pointer_a += 1
            pointer_b -= 1
        return True
        