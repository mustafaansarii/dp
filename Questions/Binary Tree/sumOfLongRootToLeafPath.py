'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''


class Solution:
    def sumOfLongRootToLeafPath(self, root):
        # code here
        res = []

        def dfs(root, curr):
            if not root:
                return
            curr.append(root.data)
            if not root.left and not root.right:
                res.append(curr[:])
            dfs(root.left, curr)
            dfs(root.right, curr)
            curr.pop()

            return

        dfs(root, [])
        max_len = 0
        max_sum = 0
        for i in res:
            if len(i) > max_len:
                max_len = len(i)
                max_sum = sum(i)
            elif len(i) == max_len:
                max_sum = max(max_sum, sum(i))

        return max_sum