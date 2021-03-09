# 暴力
def sortedSquaredArray(array):
    # 第一次 没有考虑到负数的平方大小问题
    return sorted([x ** 2 for x in array])


# Tow pointer
# import math
# python abs() 直接可用
def sortedSquaredArray(array):
    sm_idx = 0
    bg_idx = len(array) - 1
    res_idx = len(array) - 1
    # init list with fixed size 的方式
    # res = [0 for x in range(len(array))]
    res = [0] * len(array)
    while sm_idx != bg_idx:
        if abs(array[sm_idx]) > abs(array[bg_idx]):
            res[res_idx] = array[sm_idx] ** 2
            sm_idx += 1
        else:
            res[res_idx] = array[bg_idx] ** 2
            bg_idx -= 1
        res_idx -= 1
    # 没有分析最后相等会发生的什么, 这时候 两边的都没有写
    res[0] = array[bg_idx] ** 2
    return res

# 改变成for， 少考虑一种情况
# import math
# python abs() 直接可用
def sortedSquaredArray(array):
	sm_idx = 0
	bg_idx = len(array) - 1
	res = [0]* len(array)
	# 不要迷信 while
	# reversed 的用法
	for i in reversed(range(len(array))):
		if abs(array[sm_idx]) > abs(array[bg_idx]):
			res[i] = array[sm_idx] ** 2
			sm_idx += 1
		else:
			res[i] = array[bg_idx] ** 2
			bg_idx -= 1
	# 不用考虑相等的时候 进入else
	return res
