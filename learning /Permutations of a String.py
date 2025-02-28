class Solution:
    def findPermutation(self, s):
        s = list(s)
        res = []
        self.helper(s, 0, res)
        return res

    def helper(self, s, index, res):
        if index == len(s):
            res.append("".join(s))
            return

        for i in range(index, len(s)):
            if i > index and s[i] == s[index]:
                continue
            s[index], s[i] = s[i], s[index]
            self.helper(s, index + 1, res)
            s[index], s[i] = s[i], s[index]


if __name__ == "__main__":
    sol = Solution()
    s = "AAA"
    Output= ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
    print(sol.findPermutation(s))




