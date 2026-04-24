class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)

        while l < r:
            print("GOT HERE")
            print(l)
            print(r)
            mid = l + (r-l)//2
            print(mid)

            if nums[mid]==target:
                return mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return -1 
               
    
    
