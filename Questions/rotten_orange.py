from collections import deque
class Solution:
    def orangesRotting(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        fresh = 0
         
        # Initialize queue with rotten oranges and count fresh ones
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 2:
                    queue.append((i, j))
                elif mat[i][j] == 1:
                    fresh += 1
        
        # If no fresh oranges, no time needed
        if fresh == 0:
            return 0
            
        # Directions for 4-connected neighbors
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        time = -1
        # Perform BFS
        while queue:
            time += 1
            level_size = len(queue)
            
            for _ in range(level_size):
                x, y = queue.popleft()
                
                # Check all 4 directions
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    # If neighbor is fresh, rot it
                    if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] == 1:
                        mat[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
        
        # If no fresh oranges left, return time, else -1
        return time if fresh == 0 else -1


if __name__ == "__main__":
    sol = Solution()
    mat = [[0, 1, 2], 
           [0, 1, 2], 
           [2, 1, 1]]
    print(sol.orangesRotting(mat))  # Output: 1