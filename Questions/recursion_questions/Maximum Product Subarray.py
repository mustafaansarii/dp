class Solution:

    # Function to find maximum
    # product subarray
    # def maxProduct(self, arr):
    #     # code here
    #     n = len(arr)
    #     res = float('-inf')
    #     def sub_arr(idx, arr, n, curr_res, prod):
    #         nonlocal res
    #         if idx == n:
    #             return
    #         prod = prod * arr[idx]
    #         res = max(res, prod)
    #         sub_arr(idx + 1, arr, n, curr_res, prod)
    #         sub_arr(idx + 1, arr, n, curr_res, 1)
    #     sub_arr(0, arr, n, res, 1)
    #     return max(res, max(arr))
    def maxProduct(self, arr):
        n = len(arr)
        res = arr[0]
        prefix= suffix = 1
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix = prefix * arr[i]
            suffix = suffix * arr[n-i-1]
            res = max(res, prefix, suffix)
        return res

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(Solution().maxProduct(arr))