# 假设 第一个已经排序好了, 从第二个开始前比较 insert
def insertionSort(array):
    for i in range(1, len(array)):
        # range 的用法, range(a,b,c) 包含 a, 不包含b 每个步骤 step c
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            # 如果不大了 抓紧结束
            else:
                break
    return array

