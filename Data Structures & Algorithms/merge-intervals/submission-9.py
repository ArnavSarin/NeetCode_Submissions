class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        if len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x:x[0], reverse=False)
        print(intervals)

        interval = intervals.pop(0)
        second_interval = None
        # inserted = False

        while len(intervals) > 0:
            print("BEGINNING")
            print(interval)
            second_interval = intervals.pop(0)
            print(second_interval)

            if interval[1] < second_interval[0]:
                print("GOT HERE BELOW")
                ans.append(interval)
                interval = second_interval
                # inserted = True 
            elif interval[0] <= second_interval[0] and interval[1] >= second_interval[0] \
                and interval[1] <= second_interval[1]:
                print("GOT HERE 0")
                interval = [interval[0],second_interval[1]]
            elif interval[0] <= second_interval[0] and second_interval[0] <= interval[1] \
                and interval[1] <= second_interval[1] and second_interval[1] <= interval[1]:
                print("GOT HERE INTERVAL CONTAINS")
                continue
            elif second_interval[0] <= interval[0] and interval[0] < second_interval[1] \
                and second_interval[0] <= interval[1] and interval[1] <= second_interval[1]:
                print("GOT HERE INTERVAL IS SUBSET")
                interval = second_interval
            elif second_interval[0] <= interval[0] and interval[0] <= second_interval[1] \
                and second_interval[1] <= interval[1]:
                print("GOT HERE 1")
                interval = [second_interval[0],interval[1]]
            else:
                print("GOT HERE 2")
                continue

        # if inserted:
        # ans.append(second_interval)
        # else:
        #     ans.append(interval)
        ans.append(interval)
        return ans


