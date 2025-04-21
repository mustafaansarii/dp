class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here
        n = len(arr)
        cnt = float("inf")
        for i in range(n):
            sums = 0
            for j in range(i, n):
                sums += arr[j]
                if sums > x:
                    cnt = min(cnt, j - i + 1)
                    break


        return cnt



if __name__ == "__main__":
    x=12829
    arr=[6829, 3917, 171, 3654]
    obj = Solution()
    print(obj.smallestSubWithSum(x, arr))
