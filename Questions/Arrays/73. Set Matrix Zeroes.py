from typing import  List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        row_aux=[False]*row
        col_aux=[False]*col

        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    row_aux[i]=True
                    col_aux[j]=True

        print(row_aux)
        print(col_aux)

        for i in range(row):
            for j in range(col):
                if row_aux[i] or col_aux[j]:
                    matrix[i][j]=0

if __name__=="__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution = Solution()
    solution.setZeroes(matrix)
    print(*matrix)