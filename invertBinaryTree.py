def invertBinaryTree(tree):
    if tree != None:
        # 先后顺序问题 不能直接更改顺序
        # tree.left = invertBinaryTree(tree.left)
        # tree.right = invertBinaryTree(tree.right)
        tree.right, tree.left = invertBinaryTree(tree.left), invertBinaryTree(tree.right)
        # tree.left, tree.right = tree.right, tree.left
        # 不要忘记写 return
        return tree
    else:
        return None


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree):
    # BFS 的精髓 array
    q = [tree]
    while len(q) > 0:
        cur = q.pop()
        if cur != None:
            cur.left, cur.right = cur.right, cur.left
            q.append(cur.left)
            q.append(cur.right)
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
