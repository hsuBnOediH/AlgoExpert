def moveElementToEnd(array, toMove):
	mover = 0
	replacer = len(array) - 1
	while replacer > mover:
		# 不要忘记 最外层的限制条件 for both
		while array[mover] is not toMove and replacer > mover:
			mover += 1
		while array[replacer] is toMove and replacer > mover:
			replacer -= 1
		array[mover], array[replacer]  = array[replacer], array[mover]
	return array



def moveElementToEnd(array, toMove):
	mover = 0
	replacer = len(array) - 1
	find_slot = False
	find_target = False
	while replacer > mover:
		if array[replacer] is toMove:
			replacer -= 1
		else:
			find_slot = True
		if array[mover] is not toMove:
			mover += 1
		else:
			find_target = True
		if find_slot and find_target:
			array[mover], array[replacer]  = array[replacer], array[mover]
			find_slot = False
			find_target = False
	return array



def moveElementToEnd(array, toMove):
	mover = 0
	replacer = len(array) - 1
	while replacer > mover:
		# 不要忘记 最外层的限制条件 for both
		while array[replacer] is toMove and replacer > mover:
			replacer -= 1
		if array[mover] == toMove:
			array[mover], array[replacer]  = array[replacer], array[mover]
		mover +=1
	return array
# 一个while 配合 一个if的组合, 保证一边静止  把判定写在不确定的这边