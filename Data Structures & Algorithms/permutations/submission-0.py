class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(curr):
            nonlocal ans

            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for i in range (0,len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()

        backtrack([])
        return ans 
        