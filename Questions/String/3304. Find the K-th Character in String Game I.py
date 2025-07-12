class Solution:
    def kthCharacter(self, k: int) -> str:
        sb = ['a']
        while len(sb) < k:
            size = len(sb)
            for i in range(size):
                next_char = chr(ord('a') + ((ord(sb[i]) - ord('a') + 1) % 26))
                sb.append(next_char)
        return sb[k - 1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.kthCharacter(16))
    # Input: k = 8
    # Output: "e"
    # Explanation:
    # Initially, word = "a"
    # We need to do the operation three times:
    # Generated string is "b", word becomes "ab"
    # Generated string is "bc", word becomes "abbc"
    # Generated string is "bccd", word becomes "abbcbccd"