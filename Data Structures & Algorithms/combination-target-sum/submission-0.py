class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(curr,total,counter):
            nonlocal ans

            if total == target:
                ans.append(curr[:])
                return
            
            for i in range(counter,len(nums)): 
                new_total = total + nums[i]
                if new_total <= target:
                    print("GOT HERE")
                    print(nums[i])
                    print(total)
                    curr.append(nums[i])
                    backtrack(curr[:],new_total,i)
                    curr.pop()
            return

        backtrack([],0,0)
        return ans



                
        