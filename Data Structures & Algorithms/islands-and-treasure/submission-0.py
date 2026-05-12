class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def validate(x,y):
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[x]):
                return True
            return False


        for x in range(0,len(grid)):
            for y in range (0,len(grid[x])):

                if grid[x][y]==0:
                    seen = set()
                    queue = deque([(x,y,0)])

                    while len(queue) > 0:
                        i,j,curr_distance = queue.popleft()

                        if (i,j) not in seen and grid[i][j]!=-1:

                            if curr_distance < grid[i][j]:
                                grid[i][j] = curr_distance

                            if validate(i+1,j) and (i+1,j) not in seen:
                                queue.append((i+1,j,curr_distance+1))

                            if validate(i-1,j) and (i-1,j) not in seen:
                                queue.append((i-1,j,curr_distance+1))

                            if validate(i,j+1) and (i,j+1) not in seen:
                                queue.append((i,j+1,curr_distance+1))

                            if validate(i,j-1) and (i,j-1) not in seen:
                                queue.append((i,j-1,curr_distance+1))

                        seen.add((i,j))
                else:
                    continue
        
        return
            


        

                        





