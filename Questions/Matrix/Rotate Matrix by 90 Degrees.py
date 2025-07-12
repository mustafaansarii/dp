def rotate_90(mat):
    m=len(mat)
    n = len(mat[0])

    for i in range(m):
        for j in range(n):
            mat[j][i]=mat[i][j]


    for i in range(m):
        mat[i].reverse()


if __name__=="__main__":
    mat=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    rotate_90(mat)
    print(mat)