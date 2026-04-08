class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}

        for i in range (0,len(nums)):
            if(nums[i] in hashMap):
                return True
            else:
                hashMap[nums[i]] = 1
        return False
         