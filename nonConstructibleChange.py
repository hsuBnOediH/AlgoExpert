# 非暴力算法，但是复杂比较高
def nonConstructibleChange(coins):
	res = 0
	coins.sort(reverse = True)
	print(f'sorted: {coins}')
	
	changes =[0]
	while len(coins) > 0:
		new_coin = coins.pop()
		print(f'new_coin: {new_coin}')
		temp =[]
		for num in changes:
			print(f'num: {num}')
			new_min = num + new_coin
			print(f'new_min: {new_min}')
			if new_min not in changes:
				if new_min  == res +1: 
					res = new_min
					temp.append(new_min)
					print(f'append new min: {temp}')
				else:
					# the first can not 所以加1
					return res + 1
		changes.extend(temp)
		print('next coin---------')
	# the first can not 所以加1
	return res + 1



# 数学题 没有什么意义
def nonConstructibleChange(coins):
    coins.sort()
	res = 0 
	for i in coins:
		if i > res +1:
			return res +1
		res += i
    return res + 1
