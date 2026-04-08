class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hash_map = {}
        sorted_nums = sorted(nums)
        ans = []

        for i in range(0,len(sorted_nums)):
            hash_map[-sorted_nums[i]] = i

        for i in range(0,len(sorted_nums)):
            for j in range(i+1,len(sorted_nums)):
                a = sorted_nums[i]
                b = sorted_nums[j]
                curr_sum = a + b
                if curr_sum in hash_map and i != hash_map[curr_sum] and j != hash_map[curr_sum]:
                    triplet = sorted([a,b,sorted_nums[hash_map[curr_sum]]])
                    if triplet not in ans: 
                        ans.append(triplet)
        
        return ans
            
            

        
        