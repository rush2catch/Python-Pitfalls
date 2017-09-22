#coding:utf-8

class Solution(object):
	def file_process(self):
		count = 0
		with open('fix.log', 'rb') as f:
			for line in f.readlines():
				arr = line.split()
				if arr[-1] != arr[-2]:
					count += 1
					print(line)
		print(count)

obj = Solution()
obj.file_process()