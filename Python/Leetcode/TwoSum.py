
nums = []
target = 10


x = []
for i, num1 in nums:
    value = target - num1
    if value in nums[i+1:]:
        x.append(i)
        x.append(nums[i+1:].index(value) + (i+1))
        return x
    










