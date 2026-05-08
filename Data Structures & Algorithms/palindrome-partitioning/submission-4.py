class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def backtrack (curr, word):

            if len(word) > 0 and word == word[::-1]:
                ans.append(curr[:] + [word])

            if len(word) == 0:
                ans.append(curr[:])
                return

            for i in range(0,len(word)):
                first_half = word[:i]

                if first_half != "":
                    if first_half == first_half[::-1]:
                        curr.append(first_half)
                        backtrack(curr,word[i:])
                        curr.pop()
            return

        if len(s) == 1:
            return [[s]]

        backtrack([],s)
        return ans




            