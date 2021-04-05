# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    return tree_info(tree)[1]


def tree_info(tree):
	if tree is not None:
		l_h, l_balance= tree_info(tree.left)
		# 又是复制 left right 问题
		r_h, r_balance= tree_info(tree.right)
		height = max(l_h, r_h) +1
		if abs(l_h - r_h) <= 1 and l_balance and r_balance:
			return height,True
		else:
			return height,False
	else:
		return 0, True