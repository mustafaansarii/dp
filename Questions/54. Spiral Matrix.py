from typing import  List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range((min(m,n)+1)//2):

            for j in range(i,n-i):
                res.append(matrix[i][j])
            for j in range(i+1,m-i):
                res.append(matrix[j][n-i-1])
            for j in range(n-i-2,i-1,-1):
                if i==m-i-1:
                    break
                res.append(matrix[m-i-1][j])
            for j in range(m-i-2,i,-1):
                if i==n-i-1:
                    break
                res.append(matrix[j][i])

        return  res


if __name__=="__main__":
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    print(Solution().spiralOrder(matrix))
