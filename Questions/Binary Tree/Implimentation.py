
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    if not root: return []
    return [root.data]+preOrder(root.left)+preOrder(root.right)

def inorder(root):
    if not root: return []
    return inorder(root.left)+[root.data]+inorder(root.right)

def postOrder(root):
    if not root: return []
    return postOrder(root.left)+postOrder(root.right)+[root.data]

def preOrder_iter(root):
    if not root: return
    res=[]
    stack=[root]
    while stack:
        curr=stack.pop()
        res.append(curr.data)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res

def inorder_iter(root):
    if not root: return
    stack=[]
    current=root
    res=[]
    while stack or current:
        if current:
            stack.append(current)
            current=current.left
        elif stack:
            current=stack.pop()
            res.append(current.data)
            current=current.right
    return res

def postOrder_iter(root):
    if not root: return
    res=[]
    stack1=[root]
    stack2=[]
    current=root
    while stack1:
        current=stack1.pop()
        stack2.append(current.data)
        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)
        
    while stack2:
        res.append(stack2.pop())
    
    return res

def Level_Order(root):
    if not root:
        return
    q=[root]
    res=[]
    while q:
        current=q.pop(0)
        res.append(current.data)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    return res

if __name__ == "__main__":
    root=Node(1)
    root.left=Node(1)
    root.right=Node(2)
    root.left.left=Node(3)
    root.left.right = Node(4)
    print("inorder: ", inorder(root))
    print("inorder_iter: ",inorder_iter(root))
    print("preOrder: ", preOrder(root))
    print("preOrder_iter: ",preOrder_iter(root))
    print("postOrder: ", postOrder(root))
    print("posttOrder_iter: ",postOrder_iter(root))
    print("Level_Order: ",Level_Order(root))