class Solution:
    def findLargest(self, arr):
        arr = [str(num) for num in arr]

        arr.sort(key=lambda x: x * 10, reverse=True)

        result = ''.join(arr)

        if result[0] == '0':
            return '0'

        return result



res=Solution().findLargest([3, 30, 34, 5, 9])
print(res)