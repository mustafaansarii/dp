from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        pref = [0] * n
        suff = [0] * n
        pref[0] = nums[0]
        suff[n-1] = nums[n-1]
        for i in range(1, n):
            pref[i] = max(pref[i-1], nums[i])
        
        for i in range(n-2, -1, -1):
            suff[i] = max(suff[i+1], nums[i])
        
        for i in range(1, n-1):
            ans = max(ans, (pref[i-1] - nums[i]) * suff[i+1])
        
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maximumTripletValue([12,6,1,2,7]))