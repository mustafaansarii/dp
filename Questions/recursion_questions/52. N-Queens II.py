class Solution:
    def totalNQueens(self, n: int) -> int:
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
                return 1
            count = 0
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    count += solve(board, row + 1)
                    board[row][col] = '.'
            return count
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        return solve(board, 0)
