def findThreeLargestNumbers(array):
	res = array[:3]
	# print(res)
	cur_min = min(res)
	for num in array[3:]:
		if num > cur_min:
			res.remove(cur_min)
			# print(res)
			res.append(num)
			cur_min = min(res)
	return sorted(res)