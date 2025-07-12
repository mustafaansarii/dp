'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import  deque
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        # height=0
        # queue=deque()
        # queue.append(root)
        # while queue:
        #     n=len(queue)
        #     for _ in range(n):
        #         curr=queue.popleft()
        #         if curr.left:
        #             queue.append(curr.left)
        #         else:
        #             queue.append(curr.right)
        #     height+=1
        #
        # return height-1


        if not root:
            return -1
        left = self.height(root.left)
        right = self.height(root.right)

        return max(left,right)+1




