from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(open, close, curr_res):
            if open == close == n:
                res.append(curr_res)
                return
            if open < n:
                generate(open+1, close, curr_res+"(")
            if close < open:
                generate(open, close+1, curr_res+")")
        generate(0, 0, "")
        return res



if __name__=="__main__":
    n = 3
    print(Solution().generateParenthesis(n))
