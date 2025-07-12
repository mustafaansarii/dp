class Solution:
    def countConsec(self, n: int) -> int:
        # code here
        total = 1 << n

        tmp1, tmp2 = 1, 2
        # Compute n_th  terms of Fibonacci
        for i in range(2, n+1):
            tmp1, tmp2 = tmp2, tmp1 + tmp2
        return total - tmp2

if __name__=="__main__":
    sol=Solution()
    print(sol.countConsec(23))