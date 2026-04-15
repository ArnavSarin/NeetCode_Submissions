class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        hash_map = {}
        for i in range (0,len(position)): 
            hash_map[i] = (position[i],(target - position[i])/speed[i])

        val = [j for i, j in sorted(hash_map.items(),key=lambda x:x[1][0], reverse=True)]
        
        fleets = []
        for pos, time in val:
            fleets.append((pos,time))
            if len(fleets)>=2 and (fleets[-2][0] == fleets[-1][0] or fleets[-2][1] >= fleets[-1][1]):
                fleets.pop()

        return len(fleets)


