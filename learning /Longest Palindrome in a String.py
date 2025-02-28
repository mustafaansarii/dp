class Solution:
    def longestPalindrome(self, s):
        # code here
        # max_len=0
        # max_str=''
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         substr=s[i:j+1]
        #         if substr==substr[::-1]:
        #             if len(substr)>max_len:
        #                 max_len=len(substr)
        #                 max_str=substr
        # return max_str
        pass

class Solution:
    def longestPalindrome(self, s):
        max_str = ''
        n=len(s)
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            odd = expand_around_center(i, i)
            if len(odd) > len(max_str):
                max_str = odd
            even = expand_around_center(i, i + 1)
            if len(even) > len(max_str):
                max_str = even
        return max_str

if __name__=="__main__":
    s="aaaabbaa"
    print(Solution().longestPalindrome(s))