class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(0,len(numbers)):
            hash_map[target-numbers[i]] = i

        for i in range(0,len(numbers)):
            if numbers[i] in hash_map and hash_map[numbers[i]] != i:
                return sorted([i+1,hash_map[numbers[i]]+1])
        
        return []



