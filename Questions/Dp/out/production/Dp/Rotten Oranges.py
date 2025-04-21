class Solution:
    def orangesRotting(self, mat):
        m, n = len(mat), len(mat[0])
        queue = []
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 2:
                    queue.append((i, j, 0))
                elif mat[i][j] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_time = 0
        
        while queue and fresh > 0:
            x, y, time = queue.pop(0)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] == 1:
                    mat[nx][ny] = 2
                    fresh -= 1
                    queue.append((nx, ny, time + 1))
                    max_time = max(max_time, time + 1)
        
        return max_time if fresh == 0 else -1

match = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
sol = Solution().orangesRotting(match)
print(sol)