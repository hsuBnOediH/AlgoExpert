def threeNumberSum(array, targetSum):
    cur_num = 0
    # sort 之后问题更好解决 nlogn
    array = sorted(array)
    res = []
    # 边界问题
    for i in range(0, len(array) - 2):
        l = i + 1
        r = len(array) - 1
        sub_tar = targetSum - array[i]
        # 内部使用two pointer,  保证里面 loop through 一遍
        # 总复杂度是 n^2
        while l < r:
            tal = array[i] + array[l] + array[r]
            if tal is targetSum:
                res.append((array[i], array[l], array[r]))
                l += 1
                r -= 1
            elif tal < targetSum:
                l += 1
            else:
                r -= 1
    return res
