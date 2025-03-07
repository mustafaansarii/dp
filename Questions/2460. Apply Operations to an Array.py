from typing import  List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        pass

    def move_zero(self, arr):
        n = len(arr)

        j = 0
        for i in range(n):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        return arr



if __name__=="__main__":
    nums = [1,2,0,0,0,2,1,1,6,5,0,4]
    print(Solution().move_zero(nums))