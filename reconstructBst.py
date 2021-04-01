# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
	if len(preOrderTraversalValues) == 0: return None
	if len(preOrderTraversalValues) ==1: return BST(preOrderTraversalValues[0])
	else:
		root = preOrderTraversalValues[0]
		pr  = len(preOrderTraversalValues)
		for i in range(1,len(preOrderTraversalValues)):
			if preOrderTraversalValues[i] >= root:
				pr = i
				break

		return BST(root,reconstructBst(preOrderTraversalValues[1:pr]), reconstructBst(preOrderTraversalValues[pr:]))



arr = [10, 4, 2, 1, 5, 17, 19, 18]
reconstructBst(arr)


# 不知道为什么不能用的 解法
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
	bst = None
	for i in preOrderTraversalValues:
		insert(bst,i)
	return bst


def insert(bst,value):
	if bst == None:
		bst = BST(value,None,None)
	elif bst.value > value:
		insert(bst.left)
	else:
		insert(bst.right)