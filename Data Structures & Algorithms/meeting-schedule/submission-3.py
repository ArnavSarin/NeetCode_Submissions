"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) <= 1:
            return True

        intervals = sorted(intervals, key=lambda x:x.start, reverse=False)

        print([(i.start,i.end) for i in intervals])

        prev_interval = intervals.pop(0)
        prev_start, prev_end = prev_interval.start, prev_interval.end


        while len(intervals) > 0:
            interval = intervals.pop(0)
            start, end = interval.start, interval.end

            if prev_start > start and prev_start < end \
                or prev_end > start and prev_end < end:
                return False
            if start > prev_start and start < prev_end \
                or end > prev_start and end < prev_end:
                return False
            if start == prev_start and end == prev_end:
                return False
            
            prev_start, prev_end = start, end

        return True 

