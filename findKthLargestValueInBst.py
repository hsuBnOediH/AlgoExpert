# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    right_size = tree_size(tree.right)
    if right_size >= k:
        return findKthLargestValueInBst(tree.right, k)
    elif right_size + 1 == k:
        return tree.value
    else:
        return findKthLargestValueInBst(tree.left, k - right_size - 1)


def tree_size(tree):
    size = 0
    if tree != None:
        size += 1
    else:
        return 0
    if tree.left != None:
        size += tree_size(tree.left)
    if tree.right != None:
        size += tree_size(tree.right)
    return size
