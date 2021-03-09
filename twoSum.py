# Array in 的查找不够快
def twoNumberSum(array, targetSum):
    potential = []
    for num in array:
        potential_num = targetSum - num
        if potential_num != num:
            potential.append(potential_num)

    for num in potential:
        if num in array:
            return [num, targetSum - num]
    return []


# dict的设计方式问题 需要两个loop
def twoNumberSum(array, targetSum):
    # 在python中 dict 和 object 是hash
    potential = {}
    for num in array:
        potential[num] = targetSum - num if targetSum != 2 * num else False

    # 调取pair 的方式 dict.items()
    # 更多关于dict
    # https://docs.python.org/zh-cn/3.8/library/stdtypes.html#mapping-types-dict
    for (key, value) in potential.items():
        if value in array:
            return [key, value]
    return []


# 目前最佳
def twoNumberSum(array, targetSum):
    # 在python中 dict 和 object 是hash
    potential = {}
    for num in array:
        # 检查 num in potential.keys()
        if num in potential:
            return [num, potential[num]]
        else:
            potential[targetSum - num if targetSum != 2 * num else False] = num
    return []
