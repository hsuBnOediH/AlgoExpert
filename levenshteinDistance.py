def levenshteinDistance(str1, str2):
    # 初始化2d array
    steps = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
    steps[0] = [i for i in range(len(str2) + 1)]
    for i in range(len(str1) + 1):
        steps[i][0] = i
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            min_p = min(steps[j][i - 1], steps[j - 1][i], steps[j - 1][i - 1])
            if str1[j - 1] == str2[i - 1]:
                # bug 所在 需要 对角线的base case
                steps[j][i] = steps[j - 1][i - 1]
            else:
                steps[j][i] = min_p + 1

    print(steps)
    return steps[-1][-1]
