class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        print(seen)

        for i in nums:
            if i in seen:
                return i
            seen.add(i)

        return -1
        

