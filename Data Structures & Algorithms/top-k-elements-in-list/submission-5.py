class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = Counter(nums)

        print(hash_map.items())

        return [key for key, _ in sorted(hash_map.items(), key=lambda x: x[1], reverse=True)[:k]]