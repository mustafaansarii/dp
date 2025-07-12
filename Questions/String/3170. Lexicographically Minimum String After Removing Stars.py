class Solution:
    def clearStars(self, s: str) -> str:
        if len(s) == 1:
            return ""
        stars = []
        for i in range(len(s)):
            if s[i] == "*":
                stars.append(i)
            elif stars:
                s = s[:i] + "*" + s[i+1:]
                s = s[:stars[-1]] + s[i] + s[stars[-1]+1:]
                stars.pop()
                break
            if i == len(s)-1:
                return self.clearStars(s[:-1])
        return s.replace("*", "")


if __name__=="__main__":
    s = Solution()
    print(s.clearStars("a**b**c"))