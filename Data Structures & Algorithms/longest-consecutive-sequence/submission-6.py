class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sorted_nums = sorted(set(nums))

        if len(sorted_nums)==0:
            return 0

        if len(sorted_nums)==1:
            return len(sorted_nums)

        left = right = 0
        max_value = 1

        while(right<len(sorted_nums)-1):
            if sorted_nums[right]+1 == sorted_nums[right+1]:
                max_value = max(max_value,right+2-left)
            else:
                left = right+1
            right += 1

        return max_value



            



            
