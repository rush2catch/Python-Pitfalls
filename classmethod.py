class A(object):
	def m1(self, n):
		print("self:", self)

	@classmethod
	def m2(cls, n):
		print("cls:", cls)

	@staticmethod
	def m3(n):
		print("n:", n)


a = A()
A.m1(a, 1)
a.m1(1)
A.m2(1)
a.m2(1)
A.m3(1)
a.m3(1)