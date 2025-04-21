# User function Template for python3
class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        # Code here
        n = len(mat)
        ans = []
        self.solve(0, 0, mat, "", ans)
        return ans

    def is_valid(self, row, col, mat):
        if row < 0 or row >= len(mat) or col < 0 or col >= len(mat[0]) or mat[row][col] == 0:
            return False
        return True

    def solve(self, row, col, mat, path, ans):
        if row == len(mat) - 1 and col == len(mat[0]) - 1:
            ans.append(path)
            return
        if not self.is_valid(row, col, mat):
            return
        mat[row][col] = 0
        self.solve(row + 1, col, mat, path + "D", ans)
        self.solve(row, col - 1, mat, path + "L", ans)
        self.solve(row, col + 1, mat, path + "R", ans)
        self.solve(row - 1, col, mat, path + "U", ans)
        mat[row][col] = 1


if __name__ == "__main__":
    mat = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    Output= ["DDRDRR", "DRDDRR"]
    obj = Solution()
    print(obj.findPath(mat))
