class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        n1, n2 = len(arr1), len(arr2)
        total_length = n1 + n2
        half = total_length // 2

        low, high = 0, n1

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = half - partition1

            left1 = arr1[partition1 - 1] if partition1 > 0 else float('-inf')
            right1 = arr1[partition1] if partition1 < n1 else float('inf')

            left2 = arr2[partition2 - 1] if partition2 > 0 else float('-inf')
            right2 = arr2[partition2] if partition2 < n2 else float('inf')

            if left1 <= right2 and left2 <= right1:
                # If the total length is even, sum the two middle elements
                if total_length % 2 == 0:
                    return max(left1, left2) + min(right1, right2)
                else:
                    # If the total length is odd, return the middle element
                    return min(right1, right2)
            elif left1 > right2:
                high = partition1 - 1
            else:
                low = partition1 + 1

if __name__ == "__main__":
    # Example usage
    arr1 = [1, 2, 4, 6, 10]
    arr2 = [4, 5, 6, 9, 12]
    print(Solution().sum_of_middle_elements(arr1, arr2))  # Output: 9 (Middle elements are 4 and 5)
