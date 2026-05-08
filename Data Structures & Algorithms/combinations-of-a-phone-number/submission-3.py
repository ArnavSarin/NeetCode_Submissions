class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []

        hm = {
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z']
        }

        def backtrack(word,counter):

            if len(word) == len(digits) and len(word) > 0:
                ans.append(word)
                return

            if counter < len(digits):
                for j in hm[digits[counter]]:
                    word += j
                    backtrack(word,counter+1)
                    word = word[:-1]

            return

        backtrack("",0)
        return ans
