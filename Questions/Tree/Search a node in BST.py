class BST:

    # Function to search a node in BST.
    def search(self, node, x):
        # code here
        if node is None:
            return False
        if node.data == x:
            return True
        elif node.data > x:
            return self.search(node.left, x)
        else:
            return self.search(node.right, x)