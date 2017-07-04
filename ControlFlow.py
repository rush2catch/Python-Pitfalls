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


control_flow_1(1, 1)
control_flow_2(1, 1)