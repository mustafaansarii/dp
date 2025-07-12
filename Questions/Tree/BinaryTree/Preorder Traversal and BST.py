#User function Template for python3

class Solution:
    def canRepresentBST(self, arr, N):
        # code here
        # in preOrder always left child is smaller than parent and right child is greater than parent

        stack = []
        last_node = float('-inf')
        for node in arr:
            if node < last_node:
                return 0
            while stack and stack[-1] < node:
                last_node = stack.pop()
            stack.append(node)
        return 1
