class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def backtrack (curr, word):

            if len(word) > 0 and word == word[::-1]:
                ans.append(curr[:] + [word])

            if len(word) == 0:
                print("GOT HERE")
                ans.append(curr[:])
                return

            for i in range(0,len(word)):
                first_half = word[:i]
                second_half = word[i:]
                print("GOT HERE 2")
                print(first_half)
                print(word[i:])

                # if first_half == "" and second_half == second_half[::-1]:
                #     curr.append(second_half)
                #     backtrack(curr,"")
                #     curr.pop()


                if first_half != "":
                    if first_half == first_half[::-1]:
                        print("GOT HERE 3")
                        curr.append(first_half)
                        backtrack(curr,word[i:])
                        curr.pop()

                    # if  first_half == first_half[::-1] and second_half == second_half[::-1]:
                    #     curr.append(first_half)
                    #     curr.append(second_half)
                    #     backtrack(curr,"")
                    #     curr.pop()
                    #     curr.pop()

            print("GOT HERE 4")
            return

        if len(s) == 1:
            return [[s]]

        backtrack([],s)
        return ans




            