def fibbonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)

def fibbonacci_series(n):
    if not n: return []
    res=[0,1]
    def fib_ser(n):
        if n==0 or n==1:
            return n
        else:
            res.append(res[-1]+res[-2])
            fib_ser(n-1)
    fib_ser(n)
    return res


def fibbonacci_dp(n):
    if n==0 or n==1:
        return n
    else:
        dp=[0]*(n+1)
        dp[1]=1
        if dp[n]!=0:
            return dp[n]
        else:
            dp[n]=fibbonacci_dp(n-1)+fibbonacci_dp(n-2)
    return dp[n]


if  __name__ == "__main__":
    print(fibbonacci(10))
    print(fibbonacci_series(9))
    print(fibbonacci_series(1))
    print(fibbonacci_dp(10))