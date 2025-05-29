class Solution:
    def sumSubstrings(self, s):
        total_sum = 0
        prev = 0
        mod = 10**9 + 7  
        for i in range(len(s)):
            num = int(s[i])
        
            curr = (prev * 10 + num * (i + 1)) % mod
            
            total_sum = (total_sum + curr) % mod
            
            prev = curr
        
        return total_sum
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    s = "1234"
    print(solution.sumSubstrings(s))  # Output: 1670