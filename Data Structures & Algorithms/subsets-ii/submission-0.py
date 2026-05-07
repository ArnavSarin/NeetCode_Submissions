class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)

        def backtrack(curr,counter):
            nonlocal ans

            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            ans.append(curr[:])
            for i in range (counter,len(nums)):

                if i > counter and nums[i] == nums[i-1]:
                    continue

                curr.append(nums[i])
                backtrack(curr,i+1)
                curr.pop()

        backtrack([],0)
        return ans