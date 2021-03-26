def smallestDifference(arrayOne, arrayTwo):
    one_p = arrayOne[0]
    two_p = arrayTwo[0]
    cur_diff = abs(one_p - two_p)
    for i in range(1, len(arrayOne)):
        diff = abs(arrayOne[i] - two_p)
        if diff < cur_diff:
            one_p = arrayOne[i]
            cur_diff = diff

    for i in range(1, len(arrayTwo)):
        diff = abs(one_p - arrayTwo[i])
        if diff < cur_diff:
            two_p = arrayTwo[i]
            cur_diff = diff
    return [one_p, two_p]


def smallestDifference(arrayOne, arrayTwo):
    # 利用已经排序号的数列
    arrayOne.sort()
    arrayTwo.sort()
    p1 = 0
    p2 = 0
    # inf 的设置方法
    diff = float('inf')
    cur_diff = float('inf')
    res_list = []
    # 你追我赶性 2pointer, 不错过每个差值
    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        num1 = arrayOne[p1]
        num2 = arrayTwo[p2]
        if num1 < num2:
            # 先记住diff 然后 incurment, 为下次做准备
            cur_diff = num2 - num1
            p1 += 1
        elif num2 < num1:
            cur_diff = num1 - num2
            p2 += 1
        else:
            # 忘记了 相等的情况
            return [num1, num2]
        # 和目前最小的进行比较
        if diff > cur_diff:
            diff = cur_diff
            res_list = [num1, num2]
    return res_list


