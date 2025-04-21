from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
    
        def is_safe(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                    if board[i][j] == 'Q':
                        return False
                for i, j in zip(range(row, -1, -1), range(col, n)):
                    if board[i][j] == 'Q':
                        return False
            return True
        
        def solve(board, row):
            if row == n:
                res.append([''.join(row) for row in board])
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    solve(board, row + 1)
                    board[row][col] = '.'


        res = []
        solve(board, 0)
        return res

if __name__ == '__main__':
    print(Solution().solveNQueens(4))