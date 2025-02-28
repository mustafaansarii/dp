class Solution:
    def rotate(self, matrix) -> None:
        
        n=len(matrix)
        new_mat = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                new_mat[i][j] = matrix[n-1-j][i]

        return new_mat

if __name__=="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().rotate(matrix))