class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(math.sqrt((0-i[0])**2 + (0-i[1])**2),i) for i in points]
        heapq.heapify(points)
        ans = []
        i = 0
        while i < k:
            value = heapq.heappop(points)
            i+=1
            ans.append(value[1])


        return ans