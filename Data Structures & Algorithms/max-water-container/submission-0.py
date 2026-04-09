class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights)-1
        max_water = 0

        while left < right:
            area = min(heights[right],heights[left])*(right-left)
            max_water = max(area, max_water)

            if heights[left]<heights[right]:
                left += 1
            else:
                right -= 1

        return max_water




            
        
        return max_water
            

        
        