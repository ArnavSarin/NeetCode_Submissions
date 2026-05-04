class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if len(stones) == 0:
            return 0

        if len(stones) == 1:
            return stones[0]

        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_stone = -heapq.heappop(stones)
            second_stone = -heapq.heappop(stones)

            if first_stone != second_stone:
                heapq.heappush(stones,-(first_stone - second_stone))

        if len(stones) == 0:
            return 0

        return -stones[0]
