class Solution:
    def maxGold(self, mat):
        n, m = len(mat), len(mat[0])
        if n == 1:
            return sum(mat[0])
        for col in range(1, m):
            mat[0][col] += max(mat[0][col - 1], mat[1][col - 1])
            for row in range(1, n - 1):
                mat[row][col] += max(mat[row - 1][col - 1], mat[row][col - 1], mat[row + 1][col - 1])
            mat[-1][col] += max(mat[-1][col - 1], mat[-2][col - 1])
        return max(mat[row][-1] for row in range(n))

if __name__=="__main__":
    mat = [[1, 3, 1, 5],
           [2, 2, 4, 1],
           [5, 0, 2, 3],
           [0, 6, 1, 2]]
    sol=Solution()
    print(sol.maxGold(mat))
