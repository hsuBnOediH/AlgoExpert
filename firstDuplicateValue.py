def firstDuplicateValue(array):
    s = set()
    for i in array:
        if i in s:
            return i
        else:
            s.add(i)
    return -1

# 1 to n 题目要求不是废话
# 相当于有个等长度的array 记录 TF， 可以利用正负 ，原文为正
def firstDuplicateValue(array):
    for i in range(len(array)):
        num = abs(array[i])
        if array[num - 1] > 0:
            array[num - 1] = - array[num - 1]
        else:
            return num
    return -1
