class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        s = ''.join([char for char in s if char.isalnum()])
        print(s)
        length = len(s)
        midpt = int(length/2)
        if(length%2==0):
            return s[0:midpt] == (s[midpt:length])[::-1]
        else:
            return s[0:midpt] == (s[midpt+1:length])[::-1]




        