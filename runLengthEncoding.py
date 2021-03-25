def runLengthEncoding(string):
    res = []
    cur_char = ''
    counter = 0
    for i in string:
        if i is cur_char and counter < 9:
            counter += 1
        else:
            # python 中 int 需要格式转换后才能join
            res.append(str(counter))
            res.append(cur_char)
            cur_char = i
            counter = 1
    # 最后两个 不要忘记处理
    res.append(str(counter))
    res.append(cur_char)
    return "".join(res[2:])
