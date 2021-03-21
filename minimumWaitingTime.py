def minimumWaitingTime(queries):
    queries = sorted(queries)
	wait_time = 0 
	tol_time = 0
	for i in range(1,len(queries)):
		pre_time = queries[i-1]
		wait_time += pre_time
		tol_time += wait_time
    return tol_time



def minimumWaitingTime(queries):
	queries = sorted(queries)
	res = 0
	left_len = len(queries )-1
	# 用乘法横向计算更加省时间
	for i in queries:
		res += left_len * i 
		left_len -=1
    return res
