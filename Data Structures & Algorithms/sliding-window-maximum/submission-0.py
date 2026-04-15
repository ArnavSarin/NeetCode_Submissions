class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans = []

        for i in range(0,len(nums)-k+1):
            max_value = max(nums[i:i+k])
            ans.append(max_value)

        return ans
        
