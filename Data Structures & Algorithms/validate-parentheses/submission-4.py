class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(0,len(s)):
            if s[i]=='[' or s[i]=='(' or s[i]=='{':
                stack.append(s[i])
            elif len(stack)==0:
                return False
            elif s[i] == ']':
                curr = stack.pop()
                if curr != '[':
                    return False
            elif s[i] == ')':
                curr = stack.pop()
                if curr != '(':
                    return False
            elif s[i] == '}':
                curr = stack.pop()
                if curr != '{':
                    return False
            else:
                return False
        
        return len(stack) == 0

        