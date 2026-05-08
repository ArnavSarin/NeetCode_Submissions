class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def validate (x,y):
            if x>=0 and x<len(grid) and y>=0 and y<len(grid[x]):
                return True
            return False

        seen = set()
        max_area = 0

        for x in range(0,len(grid)):
            for y in range(0,len(grid[x])):
                queue = deque()
                 
                if (x,y) not in seen:
                    if grid[x][y] == 0:
                        seen.add((x,y))
                    
                    if grid[x][y] == 1:
                        queue.append((x,y))
                        area = 0

                        while len(queue) > 0:
                            i, j = queue.popleft()

                            if (i,j) not in seen:
                                area += 1
                                seen.add((i,j))

                                if (i-1,j) not in seen and validate(i-1,j) and grid[i-1][j] == 1:
                                    queue.append((i-1,j))

                                if (i+1,j) not in seen and validate(i+1,j) and grid[i+1][j] == 1:
                                    queue.append((i+1,j))

                                if (i,j-1) not in seen and validate(i,j-1) and grid[i][j-1] == 1:
                                    queue.append((i,j-1))

                                if (i,j+1) not in seen and validate(i,j+1) and grid[i][j+1] == 1:
                                    queue.append((i,j+1))

                        max_area = max(max_area, area)


        return max_area

                        


