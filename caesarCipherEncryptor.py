def caesarCipherEncryptor(string, key):
	# for i in list
	# 对 i 的修改是无效的
	res = []
	# key 这个地方忘记计算 key> 26 或者 key < 0
	key = key % 26
	for i in string:
		# ord chr是转换 int and char 的函数
		res.append(chr(ord(i) + key) if ord(i) + key <= ord('z') else chr(ord(i) + key - 26))

	# string 在pyhton中 imutable, 如果想更改使用 “”.join[list of string or char]
	# 直接转换不可用
	# print(int('a'))
	return "".join(res)