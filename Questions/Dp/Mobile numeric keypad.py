class Solution:
    def getCount(self, n):
        # code here
        dp=[1]*10
        for i in range(1,n):
            dp2=[0]*10
            for j in range(10):
                dp2[j]+=dp[j]
                if j ==0:
                    dp2[j]+=dp[8]
                elif j==1:
                    dp2[j]+=dp[4]+dp[2]
                elif j==2:
                    dp2[j]+=dp[5]+dp[1]+dp[3]
                elif j==3:
                    dp2[j]+=dp[6]+dp[2]
                elif j==4:
                    dp2[j]+=dp[1]+dp[7]+dp[5]
                elif j==5:
                    dp2[j]+=dp[2]+dp[4]+dp[6]+dp[8]
                elif j==8:
                    dp2[j]+=dp[0]+dp[7]+dp[9]+dp[5]
                elif j==6:
                    dp2[j]+=dp[3]+dp[5]+dp[9]
                elif j==7:
                    dp2[j]+=dp[4]+dp[8]
                elif j==9:
                    dp2[j]+=dp[6]+dp[8]
            dp=dp2
        return sum(dp)

if __name__ == "__main__":
    n = 2
    output = 36
    sol = Solution()
    print(sol.getCount(n))