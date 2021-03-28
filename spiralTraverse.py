def spiralTraverse(array):
    width = len(array[0])
    height = len(array)
    bool_dic = {}
    for i in range(width):
        for j in range(height):
            bool_dic[(i, j)] = True
    i = 0
    j = 0
    res = []
    direc = 'right'
    for idx in range(len(bool_dic.keys()) ):
        if bool_dic[(i, j)]:
            res.append(array[j][i])
            bool_dic[(i, j)] = False
            print(res)
        if direc is 'right':
            if (i + 1, j) in bool_dic.keys() and bool_dic[i + 1, j]:
                i += 1
            else:
                direc = 'down'
        if direc is 'down':
            if (i, j + 1) in bool_dic.keys() and bool_dic[i, j + 1]:
                j += 1
            else:
                direc = 'left'
        if direc is 'left':
            if (i - 1, j) in bool_dic.keys() and bool_dic[i - 1, j]:
                i -= 1
            else:
                direc = 'up'
        if direc is 'up':
            if (i, j - 1) in bool_dic.keys() and bool_dic[i, j - 1]:
                j -= 1
            else:
                direc = 'right'
    return res

# 实际上是个 2 * 2 pointer的问题
def spiralTraverse(array):
    sc = 0
    ec = len(array[0]) - 1
    sr = 0
    er = len(array) - 1
    res = []

    while sc <= ec and sr <= er:
        for col in range(sc, ec + 1):
            res.append(array[sr][col])
        for row in range(sr + 1, er + 1):
            res.append(array[row][ec])
        for col in reversed(range(sc, ec)):
            # edge case
            if sr == er: break
            res.append(array[er][col])
        for row in reversed(range(sr + 1, er)):
            if sc == ec: break
            res.append(array[row][sc])
        sc += 1
        ec -= 1
        sr += 1
        er -= 1

    return res

