def cal_intersection(nums1, nums2):

	# method 1
	result_1 = [val for val in nums1 if val in nums2]
	print(result_1)

	# method 2
	result_2 = list(set(nums1).intersection(set(nums2)))
	print(result_2)


def cal_union(nums1, nums2):
	result = list(set(nums1).union(set(nums2)))
	print(result)

def cal_diff(nums1, nums2):
	result = list(set(nums1).difference(set(nums2))) # get items in nums1 but not in nums2
	print(result)


test_case1 = [1, 3, 5, 7, 11, 13, 17, 20]
test_case2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
cal_intersection(test_case1, test_case2)
cal_union(test_case1, test_case2)
cal_diff(test_case1, test_case2)