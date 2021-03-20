def nodeDepths(root):
	# 需要一个变量来记住 深度
	return sum_node_deep(root,0)

def sum_node_deep(node, cur):
	# None node 深度为 0 
	res = 0
	if not node == None:
		# 非0 node深度为当前深度
		res = cur
		if not node.left == None:
			# 递归 深度+1
			res += sum_node_deep(node.left, cur +1)
		if not node.right == None:
			res += sum_node_deep(node.right, cur+1)
	return res 
		



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None






def nodeDepths(root):
	return sum_node_deep(root,0)

def sum_node_deep(node, deep):
	# 分析node的left right  要多一层逻辑， 直接分析node 更好
	if node is None: return 0 
	return deep + sum_node_deep(node.left,deep +1) + sum_node_deep(node.right, deep + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def nodeDepths(root):
    res = 0
	unpops = [{'node': root,'deep':0}]
    while len(unpops) > 0:
		single_node= unpops.pop()
		# node= single_node['node']
		# deep= single_node['deep']
		# 利用stack的方式loop tree
		node,deep = single_node['node'],single_node['deep']
		if node is not None:
			res += deep
			unpops.append({'node':node.left,'deep':deep+1})
			unpops.append({'node':node.right,'deep':deep+1})
	return res


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None






