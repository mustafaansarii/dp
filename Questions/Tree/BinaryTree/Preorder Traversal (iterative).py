#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return a list containing the inorder traversal of the given tree
class Solution:
    def preOrder(self, root):
        # code here
        if not root: return
        stack=[root]
        res=[]
        while stack:

            curr=stack.pop()
            res.append(curr.data)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res

