class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").lower()
        s = ''.join([char for char in s if char.isalnum()])
        print(s)
        length = len(s)
        midpt = int(length/2)
        if(length%2==0):
            print("GOT HERE")
            print(s[0:midpt])
            print((s[midpt:length])[::-1])
            return s[0:midpt] == (s[midpt:length])[::-1]
        else:
            print("GOT HERE 2")
            print(s[0:midpt-1])
            print((s[midpt+1:length])[::-1])
            return s[0:midpt] == (s[midpt+1:length])[::-1]




        