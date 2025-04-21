class Solution:
    def getThreeLargest(self, arr):
        # code here
        seen = set()
        n = len(arr)
        max1 = max2 = max3 = float('-inf')
        for num in arr:
            if num > max1 and num not in seen:
                max3 = max2
                max2 = max1
                max1 = num
                seen.add(num)
            elif num > max2 and num not in seen:
                max3 = max2
                max2 = num
                seen.add(num)
            elif num > max3 and num not in seen:
                max3 = num
                seen.add(num)

        result = set()
        result.add(max3)
        result.add(max2)
        result.add(max1)
        return result


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,9,9, 10]
    print(Solution().getThreeLargest(arr))