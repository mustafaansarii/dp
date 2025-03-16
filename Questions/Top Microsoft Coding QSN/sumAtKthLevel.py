from os import *
from sys import *
from collections import *
from math import *

def sumAtKthLevel(root, k):
    # Write your Code here.
    if not root:
        return 0

    queue = deque([root, None])
    sum_at_k = 0

    while queue and k > 0:
        node = queue.popleft()

        if node is None:
            if not queue:
                break
            k -= 1
            queue.append(None)
        else:
            if k == 1:
                sum_at_k += node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return sum_at_k