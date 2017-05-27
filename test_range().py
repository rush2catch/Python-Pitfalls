def test_0(nums):
    for i in range(len(nums)):
        if nums[i] == 1:
            nums.pop(i)
        return nums

def test_1(nums):
    for i in range(len(nums)):
        print(i, len(nums))
        # print(nums[i])
        nums.pop()

test_1([1,1,1,11])
print(test_0([0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]))