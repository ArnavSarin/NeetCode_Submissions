class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def validate(x,y):
            return x>=0 and y>=0 and x<len(heights) and y<len(heights[x])

        pacific_ocean = [(0,0)] + [(x,0) for x in range(1,len(heights))]+[(0,y) for y in range(1,len(heights[0]))]

        atlantic_ocean = [(len(heights)-1,len(heights[0])-1)]+[(x,len(heights[x])-1) for x in range(0,len(heights))] + [(len(heights)-1,y) for y in range(0,len(heights[0]))]

        pacific = [[False for j in i] for i in heights]
        atlantic = [[False for j in i] for i in heights]

        for ocean in range(0,2):
            queue = deque(pacific_ocean)

            if ocean==1:
                queue = deque(atlantic_ocean)

            seen = set()

            while len(queue)>0:
                i,j = queue.popleft()

                if ocean == 0:
                    pacific[i][j] = True
                else:
                    atlantic[i][j] = True

                if validate(i+1,j) and (i+1,j) not in seen and heights[i][j] <= heights[i+1][j]:
                    queue.append((i+1,j))

                if validate(i-1,j) and (i-1,j) not in seen and heights[i][j] <= heights[i-1][j]:
                    queue.append((i-1,j))

                if validate(i,j+1) and (i,j+1) not in seen and heights[i][j] <= heights[i][j+1]:
                    queue.append((i,j+1))

                if validate(i,j-1) and (i,j-1) not in seen and heights[i][j] <= heights[i][j-1]:
                    queue.append((i,j-1))

                seen.add((i,j))

        ans = []
        for i in range(0,len(heights)):
            for j in range(0,len(heights[i])):
                if atlantic[i][j] and pacific[i][j]:
                    ans.append([i,j])

        return ans
        
            

        
