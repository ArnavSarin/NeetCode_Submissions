class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)

        def backtrack (curr, total, counter):
            nonlocal ans

            if total == target:
                ans.append(curr[:])
                return
            
            for i in range(counter,len(candidates)):
                
                if candidates[i] == candidates[i-1] and i > counter:
                    continue

                new_total = total + candidates[i]
                if new_total <= target:
                    curr.append(candidates[i])
                    backtrack(curr[:],new_total,i+1)
                    curr.pop()
            return
        
        backtrack([],0,0)
        return ans

