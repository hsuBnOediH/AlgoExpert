# 想法是对的 但是没有写出来，想到了记录 closest number 和 diff， 但是没有想清楚怎么处理递归的问题
# 先尝试使用 while loop的方式去写 
# 没有想到处理 root就等于num diff == 0 的情况
def findClosestValueInBst(tree, target):
	cloest = tree.value
	diff = abs(tree.value - target)
	pointer = tree
	while not pointer == None:
		if pointer.value == target: return target
		if abs(pointer.value - target) < diff:
			diff = abs(pointer.value - target)
			cloest = pointer.value
		pointer = pointer.left if target < pointer.value else pointer.right
	return cloest
# 本质在于insert remove 之类的函数		
		
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None







def findClosestValueInBst(tree, target):
	cloest = tree.value
	res =  findValueHelper(tree, target, cloest)
	return res

def findValueHelper(tree,target,cloest):
	if tree == None: return cloest
	# 最容易被忘记的case
	if tree.value == target: return target
	# python 的三元写法 必须有else
	cloest = tree.value if abs(cloest - target) > abs(tree.value - target) else cloest
	tree = tree.left if target < tree.value else tree.right
	return findValueHelper(tree, target, cloest)
	


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
