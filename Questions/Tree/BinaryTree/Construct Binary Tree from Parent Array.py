'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''


class Solution:
    # Function to construct binary tree from parent array.
    def createTree(self, parent):
        # your code here

        n=len(parent)

        ref=[]
        for i in range(n):
            temp=Node(i)
            ref.append(temp)

        for i in range(n):
            if parent[i] == -1:
                root = ref[i]
            else:
                if ref[parent[i]].left is None:
                    ref[parent[i]].left = ref[i]
                else:
                    ref[parent[i]].right = ref[i]

        return root


