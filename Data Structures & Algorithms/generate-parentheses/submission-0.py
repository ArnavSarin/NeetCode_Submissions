class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(curr, left, right, checker):
            nonlocal ans

            if left == 0 and right == 0:
                print("GOT HERE")
                print(curr)
                ans.append(curr[:])
                return

            print("GOT HERE 0")
            print(curr)
            
            if left - 1 >= 0 and checker > -1:
                print("GOT HERE 1")
                backtrack(curr + "(",left-1,right, checker + 1)

            if right - 1 >= 0:
                print("GOT HERE 2")
                backtrack(curr + ")",left,right-1, checker - 1)
                
            return
        
        backtrack("",n,n,0)
        return ans

