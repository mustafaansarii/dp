class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n = len(arr)
        max1 = max2 = float("-inf")

        for num in arr:
            if num  > max1:
                max2 = max1
                max1 = num
            elif num > max2 and num != max1:
                max2 = num

        return max2


if __name__ == '__main__':
    arr = [10,5,10]
    print(Solution().getSecondLargest(arr))
