from  typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        sum=0
        for i in range(n):
            min_val = arr[i]
            for j in range(i,n):
                min_val = min(min_val, arr[j])
                sum += min_val
        return sum




if __name__ == '__main__':
    arr = [11, 81, 94, 43, 3]
    # Output: 444
    print(Solution().sumSubarrayMins(arr))