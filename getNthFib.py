def getNthFib(n):
	if n == 2: return 1
	if n == 1: return 0
	return getNthFib(n -1) + getNthFib(n-2)


def getNthFib(n):
    # 用array 更好,省下index的空间
    dic_fib = {1: 0, 2: 1}
    return calNthFib(n, dic_fib)


def calNthFib(n, dict_fib):
    if n in dict_fib:
        return dict_fib[n]
    else:
        fib_num = calNthFib(n - 1, dict_fib) + calNthFib(n - 2, dict_fib)
        dict_fib[n] = fib_num
        return fib_num


def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    pre_two = [0, 1]
    for idx in range(3, n):
        pre_two.append(pre_two[0] + pre_two[1])
        pre_two.pop(0)

    return pre_two[0] + pre_two[1]
