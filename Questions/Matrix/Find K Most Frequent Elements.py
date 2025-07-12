def  K_Most_Frequent(arr,k):
    freq=dict()
    for num in arr:
        freq[num]=freq.get(num,0)+1

    for key,value in freq.items():
        if value==k:
            return key

    return -1


if __name__=="__main__":
    arr=[1,1,1,2,2,2,4,5,6]
    sol=K_Most_Frequent(arr,3)
    print(sol)