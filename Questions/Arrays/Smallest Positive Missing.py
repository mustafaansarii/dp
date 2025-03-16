class Solution:
    def missingNumber(self, arr):
        n = len(arr)

        # Step 1: Mark all non-positive and out of range numbers
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = n + 1

        # Step 2: Mark presence of numbers using index
        for i in range(n):
            num = abs(arr[i])  # Take absolute value to handle already marked numbers
            if num <= n:
                # Mark presence by making the number at index (num-1) negative
                arr[num - 1] = -abs(arr[num - 1])

        # Step 3: Find first positive number
        for i in range(n):
            if arr[i] > 0:
                return i + 1

        return n + 1
