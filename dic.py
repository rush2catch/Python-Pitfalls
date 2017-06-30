def dic_analysis(dic):

	for i in range(1,10,1):
		dic[i] = i+10
	print(dic)

	maxNum = 0
	maj = 0
	for k in dic:
		if dic[k] > maxNum:
			maxNum = dic[k]
			maj = k
		print(maxNum, maj)


	for key, value in dic.items():
		print(key, value)


testDic = {}
dic_analysis(testDic)