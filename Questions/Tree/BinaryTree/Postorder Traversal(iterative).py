#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    # Return a list containing the post order traversal of the given tree
    def postOrder(self,root):
        # code here
        stack1=[root]
        stack2=[]
        while stack1:
            current=stack1.pop()
            stack2.append(current.data)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        res=[]
        while stack2:
            res.append(stack2.pop())
        return res
