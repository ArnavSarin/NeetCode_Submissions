class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(0,len(board)):
            seen = set()
            for j in range(0,len(board[i])):
                if(board[i][j].isdigit() and board[i][j] in seen):
                    return False
                else:
                    seen.add(board[i][j])

        for i in range(0,len(board)):
            seen = set()
            for j in range(0,len(board[i])):
                if(board[j][i].isdigit() and board[j][i] in seen):
                    return False
                else:
                    seen.add(board[j][i])

        for i in range(0,len(board)):
            seen = set()
            for j in range(0,len(board[i])):
                row = int((int(i/3)*3) + (j/3))
                col = int((i%3)*3 + (j%3))

                if board[row][col].isdigit() and board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])
        return True


        