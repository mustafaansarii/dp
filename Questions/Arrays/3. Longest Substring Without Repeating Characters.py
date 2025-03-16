class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        n=len(s)
        start=0
        maps={}
        for i in range(n):
            if s[i] in maps and maps[s[i]] >= start:
                start=maps[s[i]]+1
            else:
                max_length=max(max_length,i-start+1)
            maps[s[i]]=i
        return max_length



if __name__=="__main__":
    solution=Solution();
    print(solution.lengthOfLongestSubstring("abcabcbb"));