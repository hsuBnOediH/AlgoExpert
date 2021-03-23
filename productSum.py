# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
	depth = 1
	res = productSumHelper(array,depth)
	return res
def productSumHelper(array, depth):
	res = 0
	for i in array:
		# if type(i) == type(1):
		if type(i) is int:
			# 分配律每次都乘 depth
			res += i * depth
		else:
			res += productSumHelper(i,depth+1) * depth
	return res
