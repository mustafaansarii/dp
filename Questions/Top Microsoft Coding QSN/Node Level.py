from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure

	class   TreeNode :
    	def __init__(self, val) :
        	self.val = val
        	self.left = None
        	self.right = None

'''

def nodeLevel(root, searchedValue):
    # Write your code here.
    def findLevel(root, searchedValue, level):
        if not root:
            return -1
        if root.val == searchedValue:
            return level

        leftLevel = findLevel(root.left, searchedValue, level + 1)
        if leftLevel != -1:
            return leftLevel

        rightLevel = findLevel(root.right, searchedValue, level + 1)
        return rightLevel

    level=findLevel(root, searchedValue, 1)
    if level !=-1:
        return level
    else:
        return 0



