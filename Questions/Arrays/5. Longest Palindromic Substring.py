class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start = 0
        max_length = 1
        def expand_around_center(left: int, right: int) -> tuple:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            left, right = expand_around_center(i, i)
            if (right - left + 1) > max_length:
                start = left
                max_length = right - left + 1

            left, right = expand_around_center(i, i + 1)
            if (right - left + 1) > max_length:
                start = left
                max_length = right - left + 1

        return s[start:start + max_length]

if __name__=="__main__":
    s=Solution()
    print(s.longestPalindrome("ac"))