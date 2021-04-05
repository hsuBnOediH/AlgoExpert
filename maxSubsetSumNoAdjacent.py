# 处理两个base case 单独拿出来 考虑清楚
# len = 0, return 0
# len = 1, reutn arr[0]
# =2, sum_2 也要取max(前两个value)


# 基础理论  两个pointer  互相依赖的pointer
# 基础思想 拆分, 拆分最小步骤去思考 只考虑当前的小小步骤 有点点点类似recursion的思维方式
def maxSubsetSumNoAdjacent(array):
    max_arr = []
    for i in range(len(array)):
        if i == 0 or i == 1:
            max_arr.append(array[i])
        else:
            print(i)
            max_arr.append(max(max_arr[i - 1], max_arr[i - 2] + array[i]))
    return 0 if len(max_arr) == 0 else max_arr[-1]


def maxSubsetSumNoAdjacent(array):
    # 单独处理 base case
    if len(array) == 1: return array[0]
    sum_1 = 0
    sum_2 = 0
    for i in range(len(array)):
        if i == 0:
            sum_1 = array[i]
        elif i == 1:
            # sum_2 = array[i]
            # 这一步忘记取前两个最大值, 有点像 最考试学计算的 max 方法, loop 一遍, 这里要看两个值, 记录两个潜在最大
            sum_2 = max(array[0], array[1])
        else:
            # 这里 旧的 sum1是不要的, 不要这样sawp
            temp = max(sum_2, sum_1 + array[i])
            temp, sum_2 = sum_2, temp
            temp, sum_1 = sum_1, temp
    return sum_2


def maxSubsetSumNoAdjacent(array):
    l = len(array)
    if not l: return 0
    if l == 1: return array[0]
    i_2 = array[0]
    i_1 = max(array[0],array[1])
    for i in range(2,l):
        temp = max(i_2 + array[i], i_1)
        i_2 = i_1
        i_1 = temp
    return i_1
