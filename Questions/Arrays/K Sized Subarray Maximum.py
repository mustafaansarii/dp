from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        deq = deque()
        res = []

        # Process first k elements
        for i in range(k):
            while deq and arr[deq[-1]] <= arr[i]:
                deq.pop()
            deq.append(i)

        res.append(arr[deq[0]])

        for i in range(k, n):
            while deq and deq[0] <= i - k:
                deq.popleft()

            while deq and arr[deq[-1]] <= arr[i]:
                deq.pop()

            deq.append(i)
            res.append(arr[deq[0]])

        return res


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 3
    # Expected Output: [3, 3, 4, 5, 5, 5, 6]
    ob = Solution()
    res = ob.maxOfSubarrays(arr, k)
    print(res)
