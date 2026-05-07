"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals = sorted(intervals, key=lambda x:x.start, reverse=False)

        time = []

        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end,-1))

        time = sorted(time, key=lambda x: (x[0],x[1]), reverse=False)
        
        max_rooms, rooms = 0, 0

        print(time)

        for t in time:
            rooms += t[1]
            max_rooms = max(rooms, max_rooms)
    
        return max_rooms

