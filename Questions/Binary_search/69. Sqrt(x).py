class Solution:
    def mySqrt(self, num: int) -> int:
        if num == 0:
            return 0

        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return mid
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return right


if __name__ == "__main__":
    print(Solution().mySqrt(8))
    output = 2  # round of 2.82842...
    print(Solution().mySqrt(4))