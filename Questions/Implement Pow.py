class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        # dp=[-1]*(abs(e)+1)
        # def solve(b,e):
        #     if e==0:
        #         return 1
        #     if e==1:
        #         return b
        #     if dp[e]!=-1:
        #         return dp[e]
        #     if e%2==0:
        #         dp[e]=solve(b,e//2)*solve(b,e//2)
        #     else:
        #         dp[e]=solve(b,e//2)*solve(b,e//2)*b
        #     return dp[e]
        # ans=solve(b, abs(e))
        # if e<0:
        #     return 1/ans
        # return ans
        if e == 0:
            return 1
        if e == 1:
            return b
        if e < 0:
            return 1 / self.power(b, -e)
        val = self.power(b, e // 2)
        if e % 2 == 0:
            return val * val
        else:
            return val * val * b
        return val



if __name__ == "__main__":
    b = 3.000000
    e = 7
    print(Solution().power(b, e))
