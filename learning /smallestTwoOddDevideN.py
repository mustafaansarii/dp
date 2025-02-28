
def smallTwoOddDevideN(n):
    if n <= 1:
        return -1
    res=[]
    for i in range(2,n+1):
        if i%2 !=0 and n%i==0:
            res.append(i)
            if len(res)==2:
                break
    return res



if __name__ == "__main__":
    for i in range(5,100,2):
        re=smallTwoOddDevideN(i)
        print(i,re)