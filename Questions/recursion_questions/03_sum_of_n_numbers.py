def sum_n(n,res):

    if not n:
        return res
    return sum_n(n-1, res+n)


print(sum_n(10,0))
