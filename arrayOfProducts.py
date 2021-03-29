def arrayOfProducts(array):
    res = []
    for i in range(len(array)):
        temp = 1
        for j in range(len(array)):
            temp = temp if i == j else temp * array[j]
        res.append(temp)

    return res


def arrayOfProducts(array):
    m = len(array)
    left = [1] * m
    right = [1] * m
    res = [1] * m
    # 没有想到用两个array
    for i in range(1, m):
        left[i] = left[i - 1] * array[i - 1]
        right[m - 1 - i] = right[m - i] * array[m - i]
    # 想到了用 left right 但是没有想到 这么袭击
    # 想到left right 之后  应该把每个的left right 写出来 就很清楚了
    for i in range(m):
        res[i] = left[i] * right[i]
    return res

def arrayOfProducts(array):
    m = len(array)
    left = 1
    right = 1
    res = [1] * m
    for i in range(1,m):
        left *= array[i-1]
        res[i] *= left
    # 一来一回
    for i in range(m-2,-1, -1):
        right *= array[i+1]
        res[i] *= right

    return res
