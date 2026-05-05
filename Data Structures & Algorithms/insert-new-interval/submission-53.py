class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        inserted = False
        for i in intervals:
            # if newInterval[1] < i[0]:
            #     ans.append(newInterval)
            #     # ans.append(i)
            #     inserted = True
            if inserted or i[1] < newInterval[0]:
                ans.append(i)
            elif i[0] <= newInterval[0] and newInterval[0] <= i[1] \
                and i[0] <= newInterval[1] and newInterval[1] <= i[1]:
                print("GOT HERE INSIDE")
                newInterval = i
            elif newInterval[0] <= i[0] and i[0] <= newInterval[1] \
                and newInterval[0] <= i[1] and i[1] <= newInterval[1]:
                print("GOT HERE CONTAINS")
                continue
            elif i[0] <= newInterval[0] and i[1] >= newInterval[0]:
                print("GOT HERE 1")
                newInterval = [i[0], newInterval[1]]
                print(newInterval)
            elif i[0] <= newInterval[1] and i[1] >= newInterval[1]:
                print("GOT HERE 2")
                newInterval = [newInterval[0],i[1]]
                print(newInterval)
            else:
                ans.append(newInterval)
                ans.append(i)
                inserted = True

        # if inserted:
        #     ans.append(intervals[len(intervals)-1])
        if not inserted:
            ans.append(newInterval)
        return ans
            


