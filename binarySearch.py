def binarySearch(array, target):
	length = len(array)
	if length == 0 or length == 1 and array[0] is not target:
		return -1
	elif array[0] is target:
		return 0
	else:
		mid_idx = int(length / 2) if length % 2 == 0 else int((length - 1) / 2)
	if array[mid_idx] == target:
		return mid_idx
	elif array[mid_idx] > target:
		sub_res =  binarySearch(array[:mid_idx], target)
		res = sub_res if sub_res is not -1 else -1
		return res
	else:
		sub_res =binarySearch(array[mid_idx:], target)
		res = mid_idx + binarySearch(array[mid_idx:], target) if sub_res is not -1 else -1
		return res





def binarySearch(array, target):
	l_pointer = 0
	r_pointer = len(array) - 1
	while l_pointer < r_pointer:
		m_pointer = (l_pointer + r_pointer) // 2
		if array[m_pointer] > target:
			r_pointer = m_pointer -1
		elif array[m_pointer] < target:
			l_pointer = m_pointer + 1
		else:
			return m_pointer
	if array[l_pointer] == target:
		return l_pointer
	else:
		return -1
