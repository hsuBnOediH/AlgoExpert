def inOrderTraverse(tree, array):
    if tree.left != None: inOrderTraverse(tree.left, array)
    array.append(tree.value)
    if tree.right != None: inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    array.append(tree.value)
    # 复制粘贴出问题, 检查复制的东西改完整了没有
    if tree.left != None: preOrderTraverse(tree.left, array)
    if tree.right != None: preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree.left != None: postOrderTraverse(tree.left, array)
    if tree.right != None: postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array

