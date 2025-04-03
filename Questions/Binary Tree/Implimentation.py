
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if not root: return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

if __name__ == "__main__":
    root=Node(10)
    root.left=Node(12)
    root.right=Node(90)
    root.left.left=Node(12)
    root.left.right = Node(12)
    inorder(root)


