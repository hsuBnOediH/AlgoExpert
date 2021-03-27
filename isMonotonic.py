def isMonotonic(array):
    # 用小于等于更好
    if len(array) == 0:
        return True
    elif len(array) == 1:
        return True
    else:
        # relation 惩罚抄写 打字错误 问题很大
        relation = 0
        for i in range(0, len(array) - 1):
            # index 写错 写成了1
            sub_relation = array[i + 1] - array[i]
            if relation != 0:
                # 用乘法更简单
                if sub_relation * relation < 0:
                    return False
            else:
                relation = sub_relation
    return True


def isMonotonic(array):
    # 最简单写法, 只增加一个bool的空间
    is_up = True
    is_down = True

    for i in range(len(array) - 1):
        fir = array[i]
        sec = array[i + 1]
        if sec - fir < 0:
            is_up = False
        if sec - fir > 0:
            is_down = False
        if is_up is False and is_down is False:
            return False
    return True
