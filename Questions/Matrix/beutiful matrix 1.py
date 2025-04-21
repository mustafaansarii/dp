class Solution:
    def isBeauty(self, mat):
        m = len(mat)
        n = len(mat[0])

        for col in range(n):
            total_sum = 0
            for row in range(m):
                total_sum += mat[row][col]

            found_beautiful = False
            for row in range(m):
                if mat[row][col] == total_sum - mat[row][col]:
                    found_beautiful = True
                    break

            if not found_beautiful:
                return False

        return True


if __name__ == "__main__":
    cl = Solution()
    mat = [[2, 0, 3, 7], [1, 4, 1, 3], [3, 2, 1, 0], [6, 2, 1, 4]]
    mat2 = [[2, 0, 0], [1, 1, 3], [1, 2, 3]]
    print(cl.isBeauty(mat2))  # False
    print(cl.isBeauty(mat))  # True
