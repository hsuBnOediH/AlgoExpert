# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return get_tree_info(tree)[0]


def get_tree_info(tree):
    # 先左后右 标准DFS
    if tree != None:
        l_path, l_height = get_tree_info(tree.left)
        r_path, r_height = get_tree_info(tree.right)
        height = max(l_height, r_height) + 1
        # 注意注意 node 和连线 结果到底想要哪一个
        path = max(l_path, r_path, l_height + r_height)
        # 想不出来的主要原因是 没有想着去利用两个return的值
        return (path, height)
    else:
        return (0, 0)


