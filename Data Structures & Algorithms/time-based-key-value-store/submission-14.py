class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((value,timestamp))
        print(self.hm)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ''

        actions = self.hm[key]

        l, r = 0, len(actions)-1

        print(actions)
        print(len(actions))

        ans = -1

        while l <= r:
            mid = l + (r-l)//2

            if actions[mid][1] == timestamp:
                return actions[mid][0]
            elif actions[mid][1] < timestamp:
                # l = mid + 1
                ans = mid 
                l = mid + 1
                # r = mid
            else:
                r = mid - 1 
                # l = mid + 1
                # r = mid

        print(l)
            
        if ans == -1:
            return ''
        return actions[ans][0]
        

