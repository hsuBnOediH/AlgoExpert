# DP 第一题
# 题目有点小问题 array 需要按顺序
# 找到最小的问题 base case 有点像 induction deduction
def numberOfWaysToMakeChange(n, denoms):
    # 非常重要: 0 的组成方法有且只有一种
    ways = [1]
    ways.extend([0] * n)
    for denom in denoms:
        for i in range(1, n + 1):
            if i >= denom:
                # i -denom 是核心
                ways[i] += ways[i - denom]
    return ways[-1]
