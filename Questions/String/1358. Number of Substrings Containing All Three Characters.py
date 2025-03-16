class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Using sliding window approach for O(n) complexity
        # Track last seen positions of a,b,c
        last_a = last_b = last_c = -1
        count = 0
        n = len(s)

        # For each character, update last seen position
        for i in range(n):
            if s[i] == 'a':
                last_a = i
            elif s[i] == 'b':
                last_b = i
            else:
                last_c = i

            # If we have seen all characters, add count of valid substrings
            if min(last_a, last_b, last_c) >= 0:
                count += min(last_a, last_b, last_c) + 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSubstrings("abcabc"))