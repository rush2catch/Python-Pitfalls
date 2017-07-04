def control_flow_1(nums1, nums2):

	while nums1 + nums2 <= 10:
		if  nums1 <= 5:
			print("nums1 = {}".format(nums1))
			nums1 += 1
		if nums2 <= 5:
			print("nums2 = {}".format(nums2))
			nums2 += 1

def control_flow_2(nums1, nums2):
	while nums1 + nums2 <= 10:
		while  nums1 <= 5:
			print("nums1 = {}".format(nums1))
			nums1 += 1
		while nums2 <= 5:
			print("nums2 = {}".format(nums2))
			nums2 += 1

def control_flow_3(num1, num2):
	while num1 + num2 <= 6:
		if num1 == 0:
			print("num1 = 0 ", num1)
		elif num1 == 1:
			print("num1 = 1 ", num1)
		elif num1 == 2:
			print("num1 = 2 ", num1)
		else:
			print("num1 = 3 ", num1)
		num1 += 1

		if num2 == 0:
			print("num2 = 0 ", num2)
		elif num2 == 1:
			print("num2 = 1 ", num2)
		elif num2 == 2:
			print("num2 = 2 ", num2)
		else:
			print("num2 = 3 ", num2)
		num2 += 1



control_flow_1(1, 1)
control_flow_2(1, 1)
control_flow_3(0, 0)