# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        if not root: return True
        def helper(node):
            # Bug 1: Need to handle None case in helper function
            if not node: return 0

            left,right=0,0
            if node.left:
                left=helper(node.left)
            if node.right:
                # Bug 2: Assigning to left instead of right variable
                right=helper(node.right)
            # Bug 3: Need to return height (1 + max of left,right) not just difference
            return 1 + max(left,right)

        # Bug 4: Need to check if any subtree is unbalanced, not just root
        def isBalancedHelper(node):
            if not node: return True
            left = helper(node.left) if node.left else 0
            right = helper(node.right) if node.right else 0
            return abs(left-right) <= 1 and isBalancedHelper(node.left) and isBalancedHelper(node.right)

        return isBalancedHelper(root)