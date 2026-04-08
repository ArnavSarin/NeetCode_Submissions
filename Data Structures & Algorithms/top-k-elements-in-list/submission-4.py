class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        for i in range(0,len(nums)):
            if(nums[i] in numsMap):
                numsMap[nums[i]] = numsMap[nums[i]] + 1
            else:
                numsMap[nums[i]] = 1

        print(numsMap)
        print(sorted(numsMap,key=numsMap.get))
        return sorted(numsMap,key=numsMap.get)[len(numsMap)-k:]

        
            
            
