class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def validate(x,y):
            if x>=0 and x < len(grid) and y>=0 and y < len(grid[x]):
                return True
            return False

        seen = set()
        num_islands = 0

        for i in range (0, len(grid)):
            for j in range (0, len(grid[i])):
                queue = deque()

                if grid[i][j]=="0":
                    seen.add((i,j))

                if grid[i][j]=="1" and (i,j) not in seen:
                    print("GOT HERE")
                    num_islands += 1
                    queue.append((i,j))

                    while len(queue) > 0:
                        row,col = queue.popleft()
                        seen.add((row,col))
                        
                        if validate(row-1,col) and (row-1,col) not in seen and grid[row-1][col]=="1":
                            queue.append((row-1,col))

                        if validate(row+1,col) and (row+1,col) not in seen and grid[row+1][col]=="1":
                            queue.append((row+1,col))
                        
                        if validate(row,col-1) and (row,col-1) not in seen and grid[row][col-1]=="1":
                            queue.append((row,col-1))

                        if validate(row,col+1) and (row,col+1) not in seen and grid[row][col+1]=="1":
                            queue.append((row,col+1))

        return num_islands               




