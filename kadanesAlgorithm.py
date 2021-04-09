def kadanesAlgorithm(array):
    t = []
	s = 0
	cur_max = - float('inf')
	for i in array:
		s+= i
		t.append(s)
		if cur_max < s:
			cur_max = s
	for i in range(len(array)):
		for j in range(i+1,len(t)):
			s = t[j] - array[i]
			t[j] = s
			if s > cur_max:
				cur_max = s
	return cur_max




def kadanesAlgorithm(array):
	res = [array[0]]
	cur_m = res[-1]
	for i in range(1,len(array)):
		# 区分节点： 当前最大，是否抛弃之前的sum
		res.append(max(res[-1] + array[i], array[i]))
		if res[-1]>cur_m:
			cur_m = res[-1]
	return  cur_m
