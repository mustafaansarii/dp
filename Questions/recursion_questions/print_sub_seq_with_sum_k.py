def print_sub_seq_equall_k(arr,k):
    def sub_seq(idx, arr, n, res, ):
        if sum(res)==k:
            print(res)
            return
        if idx == n:
            return
        res.append(arr[idx])
        sub_seq(idx + 1, arr, n, res)
        res.pop()
        sub_seq(idx + 1, arr, n, res)
    sub_seq(0, arr, len(arr), [] )



if __name__ == "__main__":
    arr = [1, 2, 3]
    k = 3
    print_sub_seq_equall_k(arr, k)
    # Output: [1, 2], [3]

    arr = [4, 5, 6]
    k = 9
    print_sub_seq_equall_k(arr, k)