class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        inserted = False
        for i in intervals:
            if inserted or i[1] < newInterval[0]:
                ans.append(i)
            elif i[0] <= newInterval[0] and newInterval[0] <= i[1] \
                and i[0] <= newInterval[1] and newInterval[1] <= i[1]:
                newInterval = i
            elif newInterval[0] <= i[0] and i[0] <= newInterval[1] \
                and newInterval[0] <= i[1] and i[1] <= newInterval[1]:
                continue
            elif i[0] <= newInterval[0] and i[1] >= newInterval[0]:
                newInterval = [i[0], newInterval[1]]
            elif i[0] <= newInterval[1] and i[1] >= newInterval[1]:
                newInterval = [newInterval[0],i[1]]
            else:
                ans.append(newInterval)
                ans.append(i)
                inserted = True

        if not inserted:
            ans.append(newInterval)
        return ans
            


