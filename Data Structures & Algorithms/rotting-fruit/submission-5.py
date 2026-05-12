class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def validate(x,y):
            if x>=0 and y>=0 and x < len(grid) and y < len(grid[x]):
                return True
            return False

        queue = deque()
        seen = set()

        for x in range (0,len(grid)):
            for y in range (0,len(grid[x])):
                if grid[x][y] == 2:
                    queue.append((x,y,0))
                    seen.add((x, y))
                    grid[x][y] = -1
                if grid[x][y] == 1:
                    grid[x][y] = math.inf


        while len(queue) > 0:
            i,j,time = queue.popleft()

            if grid[i][j] != 0:
                if time < grid[i][j]:
                    grid[i][j] = time

                if validate(i+1,j) and (i+1,j) not in seen:
                    queue.append((i+1,j,time+1))

                if validate(i-1,j) and (i-1,j) not in seen:
                    queue.append((i-1,j,time+1))

                if validate(i,j+1) and (i,j+1) not in seen:
                    queue.append((i,j+1,time+1))

                if validate(i,j-1) and (i,j-1) not in seen:
                    queue.append((i,j-1,time+1))

            seen.add((i,j))
        

        max_value = max([max(row) for row in grid])
        if max_value == math.inf:
            return -1
        if max_value == -1:
            return 0

        return max_value

        