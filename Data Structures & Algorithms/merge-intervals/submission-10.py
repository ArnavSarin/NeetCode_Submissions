class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        if len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x:x[0], reverse=False)

        interval = intervals.pop(0)
        second_interval = None

        while len(intervals) > 0:
            second_interval = intervals.pop(0)

            if interval[1] < second_interval[0]:
                ans.append(interval)
                interval = second_interval
            elif interval[0] <= second_interval[0] and interval[1] >= second_interval[0] \
                and interval[1] <= second_interval[1]:
                interval = [interval[0],second_interval[1]]
            elif interval[0] <= second_interval[0] and second_interval[0] <= interval[1] \
                and interval[1] <= second_interval[1] and second_interval[1] <= interval[1]:
                continue
            elif second_interval[0] <= interval[0] and interval[0] < second_interval[1] \
                and second_interval[0] <= interval[1] and interval[1] <= second_interval[1]:
                interval = second_interval
            elif second_interval[0] <= interval[0] and interval[0] <= second_interval[1] \
                and second_interval[1] <= interval[1]:
                interval = [second_interval[0],interval[1]]
            else:
                continue

        ans.append(interval)
        return ans


