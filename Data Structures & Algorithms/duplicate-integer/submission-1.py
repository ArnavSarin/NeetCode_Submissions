class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in range(0,len(nums)):
            if nums[i] not in seen:
                print(seen)
                seen.add(nums[i])
            else:
                return True
        
        return False
        