class Solution:
    def minOperation(self, mat):
        n = len(mat)
        min_ops = float('inf')

        # Precompute column sums
        col_sums = [sum(mat[i][j] for i in range(n)) for j in range(n)]

        for row in range(n):  # try to make this row contain all beautiful numbers
            total_cost = 0
            valid = True
            for col in range(n):
                col_sum = col_sums[col]
                if col_sum % 2 != 0:
                    valid = False
                    break

                target = col_sum // 2
                current_beauty = mat[row][col]
                current_rest_sum = sum(mat[i][col] for i in range(n) if i != row)
                desired_rest_sum = col_sum - target

                cost = abs(current_beauty - target) + abs(current_rest_sum - desired_rest_sum)
                total_cost += cost

            if valid:
                min_ops = min(min_ops, total_cost)

        return min_ops if min_ops != float('inf') else -1


if  __name__ == "__main__":
    cl = Solution()
    mat = [[2, 0, 3, 7], [1, 4, 1, 3], [3, 2, 1, 0], [6, 2, 1, 4]]
    mat2 = [[2, 4, 6], [1, 2, 3], [1, 2, 3]]
    print(cl.minOperation(mat))  # 4
    print(cl.minOperation(mat2))  # -1
