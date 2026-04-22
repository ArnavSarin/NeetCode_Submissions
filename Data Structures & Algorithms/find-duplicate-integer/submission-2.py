class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(0,len(nums)):
            idx = abs(nums[i])-1
            if nums[idx] < 0:
                return abs(nums[i])
            nums[idx] = -nums[idx]
        return -1
        

