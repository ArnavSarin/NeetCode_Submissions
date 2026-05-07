class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(curr, seen, x, y):
            if curr == word:
                return True
            
            check_x, check_x2, check_y, check_y2 = False, False, False, False

            if x + 1 < len(board) and (x+1,y) not in seen:
                seen.append((x+1,y))
                check_x = backtrack(curr + board[x+1][y],seen, x+1,y)
                seen.pop()

            if x - 1 >= 0 and (x-1,y) not in seen:
                seen.append((x-1,y))
                check_x2 = backtrack(curr + board[x-1][y],seen, x-1,y)
                seen.pop()
            
            if y + 1 < len(board[0]) and (x,y+1) not in seen:
                seen.append((x,y+1))
                check_y = backtrack(curr + board[x][y+1],seen, x,y+1)
                seen.pop()

            if y - 1 >= 0 and (x,y-1) not in seen:
                seen.append((x,y-1))
                check_y2 = backtrack(curr + board[x][y-1],seen, x,y-1)
                seen.pop()

            return check_x or check_x2 or check_y or check_y2

        for x in range(0,len(board)):
            for y in range(0,len(board[x])):
                if backtrack(board[x][y],[(x,y)],x,y):
                    return True
        
        return False
