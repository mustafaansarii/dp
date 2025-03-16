from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i=0
        j=0
        k=len(nums)
        while  j<k:
            if nums[j]<pivot:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[j]==pivot:
                j+=1
            else:
                k-=1
                nums[j],nums[k]=nums[k],nums[j]
        return nums

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        middle = []
        right = []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                right.append(num)

        return left + middle + right



if  __name__ == "__main__":
    s = Solution()
    nums=[9,12,5,10,14,3,10]
    print(s.pivotArray(nums,10))
