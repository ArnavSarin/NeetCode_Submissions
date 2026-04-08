class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        ans = []

        for i in range(0,len(nums)):
            hash_map[target-nums[i]] = i

        for i in range(0,len(nums)):
            if nums[i] in hash_map and i != hash_map[nums[i]]:
                ans = [i,hash_map[nums[i]]]
                break
        
        return sorted(ans)

        