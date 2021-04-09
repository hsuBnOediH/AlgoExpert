def hasSingleCycle(array):
    l = len(array)
    idxs = [0]
    for i in range(l):
        temp = array[idxs[-1]] + idxs[-1]
        temp = temp % l
        temp = temp if temp >= 0 else temp + l
        idxs.append(temp)
    # 注意检查和最后是不是落在了0
    return l == len(set(idxs)) and idxs[-1] == 0


def hasSingleCycle(array):
    l = len(array)
    index = 0
    # 可以一直观察index 因为
    # 1. 从0 开始
    # 2. 走n步 就停
    # 3. 走完之前不能有 0 
    # 4. 走n之后必须为0 ,  如果有sub loop 就永远回不来了 这点没考虑到
    for i in range(l):
        index += array[index]
        index = index % l
        index = index if index >= 0 else index + l
        print(index)
        if index == 0 and i < l - 1:
            return False
    return index == 0
