from collections import deque
class Solution:
    def longestSubarray(self, arr):
        n = len(arr)
        low = 0
        high = n
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if mid == 0:
                ans = max(ans, 0)
                low = mid + 1
                continue

            dq = deque()
            found = False
            for i in range(n):
                while dq and dq[0] < i - mid + 1:
                    dq.popleft()

                while dq and arr[i] >= arr[dq[-1]]:
                    dq.pop()

                dq.append(i)

                if i >= mid - 1:
                    current_max = arr[dq[0]]
                    if current_max <= mid:
                        found = True
                        break

            if found:
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1

        return ans