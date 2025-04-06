class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        res=[]
        def dfs(i,sub):
            if i==n:
                res.append(sub)
                return
            dfs(i+1,sub+s[i])
            dfs(i+1,sub)

        return res

if  __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    Solution().isSubsequence(s, t)