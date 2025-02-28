class Solution:
    def maximumSum(self, nums) -> int:
        seen={}
        max_sum=-1
        for num in nums:
            digit_sum=self.sum_int(num)
            if digit_sum in seen:
                max_sum=max(max_sum,num+seen[digit_sum])
                seen[digit_sum]=max(seen[digit_sum],num)
            else:seen[digit_sum]=num
        return max_sum
    
    def sum_int(self,n):
        sumation=0
        while n:
            sumation +=n%10
            n//=10
        return sumation
    

nums = [18,43,36,13,7]
sol = Solution().maximumSum(nums)
print(sol)