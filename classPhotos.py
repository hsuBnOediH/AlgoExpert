def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights = sorted(redShirtHeights)
	blueShirtHeights = sorted(blueShirtHeights)
	diff = []
	res =1
	for i in range(len(blueShirtHeights)):
		if blueShirtHeights[0] > redShirtHeights[0]:
			# 优化不使用额外空间
			diff.append(blueShirtHeights[i] - redShirtHeights[i])
		else:
			diff.append(-blueShirtHeights[i] + redShirtHeights[i])
		# 小于0 及时break
	for i in diff:
		res *= i
    return res > 0




def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights = sorted(redShirtHeights)
	blueShirtHeights = sorted(blueShirtHeights)
	res =1
	bule_taller = blueShirtHeights[0] > redShirtHeights[0]
	for i in range(len(blueShirtHeights)):
		if bule_taller:
			res*= (blueShirtHeights[i] - redShirtHeights[i])
		else:
			res*=(-blueShirtHeights[i] + redShirtHeights[i])
		print(res)
		if res <= 0:
			return False
    return True



#### 需要再看下zip 同样长度的array