# https://www.algoexpert.io/questions/River%20Sizes
def riverSizes(matrix):
    # 直接改成visited 之后把原来的 1 改成0 导致一些地方断掉， 需要另外一个arr 存放 is visited
    # extra array只用用visited 更好
    visited = get_visited_array(matrix)
    res_array = []
    row = len(matrix)
    col = len(matrix[0])
    for row_idx in range(row):
        for col_idx in range(col):
            if not visited[row_idx][col_idx]:
                # 之前看过的 同时满足 not visited 和 是river 就扔了
                node_size = visite_node(matrix, visited, row_idx, col_idx)
                if node_size:
                    res_array.append(node_size)
    return res_array


# 每个func 只做一个事情, 尽量控制修改visited 的地方只有一个
def visite_node(matrix, visited, row, col):
    counter = 0
    # 需要一个队列然后对队列之一while(len()) loop, DFS 思想
    unchecked = [[row, col]]
    while len(unchecked):
        node = unchecked.pop()
        if visited[node[0]][node[1]]:
            continue
        # 只在这一个地方改
        visited[node[0]][node[1]] = True
        if matrix[node[0]][node[1]] != 0:
            counter += 1
            unchecked.extend(check_surround(matrix, visited, node[0], node[1]))
    return counter


def get_visited_array(matrix):
    # 可以利用 [] * n  这一个特点 制造arary
    res = [[False] * len(matrix[0]) for row in matrix]
    return res


def check_surround(matrix, visited, row, col):
    sur_arr = []
    # 边界问题, 小的这一边用 =, len() 那一边 不用 =
    # !!!! 今日最佳bug, not visited!!!!!!!!!!!!! not 忘了加 看了半小时没看出来
    if row - 1 >= 0 and not visited[row - 1][col]:
        sur_arr.append([row - 1, col])
    if row + 1 < len(matrix) and not visited[row + 1][col]:
        sur_arr.append([row + 1, col])
    if col + 1 < len(matrix[0]) and not visited[row][col + 1]:
        sur_arr.append([row, col + 1])
    if col - 1 >= 0 and not visited[row][col - 1]:
        sur_arr.append([row, col - 1])
    return sur_arr
