def isPalindrome(string):
	length = len(string)
	for i in range(length // 2):
		if string[i] is not string[length - 1- i]:
			return False
	return True