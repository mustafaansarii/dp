class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr):
        # Sort array first to optimize search
        arr.sort()
        n = len(arr)

        for i in range(n-2):
            # Use two pointer technique
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]

                if curr_sum == 0:
                    return 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return 0

    #return 1 if -sums in seen else 0

if __name__ == "__main__":
    s = Solution()
    print(s.findTriplets([0, -1, 2, -3, 1]))

