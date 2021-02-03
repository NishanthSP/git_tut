def anagram(str1, str2):
	if len(str1) != len(str2):
		return False

	count = {}

	for i in str1:
		if not count.get(i):
			count[i] = 1
		else:
			count[i] += 1
	for i in str2:
		if not count.get(i):
			return False
		else:
			count[i] -= 1

	for i in count.keys():
		if count[i] != 0:
			return False

	return True

str1 = " abc"
str2 = "bca "
print(anagram(str1, str2))