# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    arr = []
    get_arr(tree, arr)
    target = node.value
    if target in arr:
        index = arr.index(target)
        if index < len(arr) - 1:
            print(f'arr: {arr}\nnode: {node.value}\nres: {arr[index + 1]}')
            return find_node(tree, arr[index + 1])
        else:
            return None
    else:
        return None


def get_arr(tree, arr):
    if tree.left is not None:
        get_arr(tree.left, arr)
    arr.append(tree.value)
    if tree.right is not None:
        get_arr(tree.right, arr)


def find_node(tree, node):
    q = [tree]
    while q is not []:
        cur = q.pop()
        if cur.value == node:
            return cur
        if cur.left is not None: q.append(cur.left)
        if cur.right is not None: q.append(cur.right)


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def first_value(tree):
    if tree.left is not None: return first_value(tree.left)
    return tree


def next_p(node):
    cur = node
    while cur.parent is not None and cur.parent.right == cur:
        cur = cur.parent
    return cur.parent


def findSuccessor(tree, node):
    if node.right is not None:
        return first_value(node.right)
    return next_p(node)


