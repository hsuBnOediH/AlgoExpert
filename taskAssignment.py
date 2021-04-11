def taskAssignment(k, tasks):
    num2idx = {}
    # 利用array的方法去存放
    for idx, i in enumerate(tasks):
        if i in num2idx:
            num2idx[i].append(idx)
        else:
            num2idx[i] = [idx]
    tasks.sort()
    res = []
    for i in range(k):
        targets = [tasks[i], tasks[-i - 1]]
        idxs = [num2idx[targets[0]].pop(), num2idx[targets[1]].pop()]
        res.append(idxs)
    return res
