class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)

        for i in range(0,k):
            ans = heapq.heappop(nums)

        return -ans