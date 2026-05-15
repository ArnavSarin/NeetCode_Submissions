class Solution:

    #Validate its not on the edge basically should not contain the length or the 0 
    def solve(self, board: List[List[str]]) -> None:

        def validate(x,y):
            return x>=0 and y>=0 and x < len(board) and y < len(board[x])

        queue = deque()
        seen = set()

        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == 'O' and \
                    (i==0 or j==0 or i==len(board)-1 or j==len(board[i])-1):
                    queue.append((i,j))
                    board[i][j] = 'S'

        while len(queue)>0:
            x,y = queue.popleft()

            if validate(x+1,y) and (x+1,y) not in seen and board[x+1][y]=='O':
                queue.append((x+1,y))
                board[x+1][y] = 'S'

            if validate(x-1,y) and (x-1,y) not in seen and board[x-1][y]=='O':
                queue.append((x-1,y))
                board[x-1][y] = 'S'

            if validate(x,y+1) and (x,y+1) not in seen and board[x][y+1]=='O':
                queue.append((x,y+1))
                board[x][y+1] = 'S'

            if validate(x,y-1) and (x,y-1) not in seen and board[x][y-1]=='O':
                queue.append((x,y-1))
                board[x][y-1] = 'S'

            seen.add((x,y))

        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

        






        

