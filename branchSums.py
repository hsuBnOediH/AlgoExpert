# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	res = []
	# 从0 开始计算， 找到加再什么地方， 不要重复的加 第一个
	sum_all_branch(root,0,res)
	return res 

# 全部leaf 只能用递归的解法
def sum_all_branch(tree,pre_sum,res):
	if not tree.left == None:
		sum_all_branch(tree.left, tree.value + pre_sum, res)
	if not tree.right == None:
		sum_all_branch(tree.right, tree.value + pre_sum, res)
	if tree.left == None and tree.right == None:
		res.append(pre_sum + tree.value)
		
	
