def one_n(n):
    if not n:
        return
    one_n(n-1)
    print(n)

one_n(100)