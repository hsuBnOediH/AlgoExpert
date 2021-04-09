def removeIslands(matrix):
    h = len(matrix)
    w = len(matrix[0])

    is_on_b_m = [[False for x in range(w)] for y in range(h)]
    board_arr = get_board_arr(h, w)
    board_lan_arr = []
    for (y, x) in board_arr:
        if matrix[y][x] == 1:
            is_on_b_m[y][x] = True
            board_lan_arr.append((y, x))
    while len(board_lan_arr) > 0:
        y, x = board_lan_arr.pop(0)
        sur_arr = get_sur(x, y, h, w)
        for y_temp, x_temp in sur_arr:
            if is_on_b_m[y_temp][x_temp] != True and matrix[y_temp][x_temp] == 1:
                is_on_b_m[y_temp][x_temp] = True
                board_lan_arr.append((y_temp, x_temp))
    for y in range(h):
        for x in range(w):
            if not is_on_b_m[y][x] and matrix[y][x] == 1:
                matrix[y][x] = 0
    return matrix


def get_sur(x, y, h, w):
    res = []
    if y - 1 >= 0:
        res.append((y - 1, x))
    if y + 1 < h:
        res.append((y + 1, x))
    if x - 1 >= 0:
        res.append((y, x - 1))
    if x + 1 < w:
        res.append((y, x + 1))
    return res


def get_board_arr(h, w):
    arr = [(0, x) for x in range(w)]
    temp = [(h - 1, x) for x in range(w)]
    arr.extend(temp)
    temp = [(y, 0) for y in range(h)]
    arr.extend(temp)
    temp = [(y, w - 1) for y in range(h)]
    arr.extend(temp)
    return list(set(arr))
