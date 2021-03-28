def longestPeak(array):
	p_idxs=[]
	#没想到 掐头去尾
	for i in range(1,len(array) -1):
		if array[i]> array[i-1] and array[i] > array[i+1]:
			p_idxs.append(i)
	cur_p = 0
	#实际上还是一个冲中间到两边的pointer
	# 只是多了一个找inti value
	for peak in p_idxs:
		l = peak
		r = peak
		while  l > 0 and array[l-1] < array[l]:
			l-=1
		while r < len(array) -1 and array[r] > array[r+1]:
			r+=1
		if cur_p < (r-l) + 1:
			cur_p = r-l +1
	return cur_p