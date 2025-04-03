class Solution:
    def wordBreak(self, s, dictionary):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in dictionary:
                if i >= len(word) and dp[i - len(word)]:
                    if s[i - len(word):i] == word:
                        dp[i] = True
                        break

        return True if dp[n] else False

if __name__ == '__main__':
    s = "ilike"
    dictionary = ["i", "like", "gfg"]
    ob = Solution()
    ans = ob.wordBreak(s, dictionary)
    print(ans)