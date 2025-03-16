def fact_recur(n):
    if n == 0:
        return 1
    return n * fact_recur(n-1)

def fact_dp_memo(n):
    dp=[-1]*(n+1)
    def fact(n):
        if n == 0:
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = n * fact(n-1)
        return dp[n]
    return fact(n)

def fact_tab(n):
    table=[-1]*(n+1)
    for i in range(n+1):
        if i == 0:
            table[i] = 1
        else:
            table[i] = i * table[i-1]
    return table[n]

def fact_loop(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

if __name__ == "__main__":
    n = 1500
    # print(fact_recur(n))
    # print(fact_dp_memo(n))
    # print(fact_tab(n))
    print(fact_loop(n))
