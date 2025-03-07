
def digit_comb():
    comb=0
    for i in range(1,10,2):
        for j in range(2,10,2):
            if j>4:
                continue
            for k in range(1,10):
                if k==i:
                    continue
                if k==j:
                    continue
                if abs(k-i)!=1:
                    continue
                print(i,j,k,sep="")
                comb+=1


if __name__=="__main__":
    #question
    #fist digit should be odd
    #2nd digit should even>4
    # 3rd and fourth should have difference of 1
    digit_comb()