def minNumberOfCoinsForChange(n, denoms):
    res = 0
    denoms.sort()
    denoms.reverse()
    print(denoms)
    for i in denoms:
        n_coin = n // i
        rest = n % i
        res += n_coin
        n = rest
    if n == 0:
        return res
    else:
        return -1

# 不能解决 【1，3，5】 9 这种问题
def minNumberOfCoinsForChange(n, denoms):
    changes = [float("inf") for i in range(n + 1)]
    print(changes)
    changes[0] = 0
    for d in denoms:
        for i in range(n + 1):
            if d <= i:
                changes[i] = min(changes[i - d] + 1, changes[i])
    if changes[-1] == float("inf"): return -1
    return changes[-1]
