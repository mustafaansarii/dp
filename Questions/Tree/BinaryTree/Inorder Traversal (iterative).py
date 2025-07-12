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
    def inOrder(self, root):
        # code here
        if not root: return
        stack=[]
        curr=root
        res=[]

        while curr or stack:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop()
                res.append(curr.data)
                curr=curr.right
        return res
