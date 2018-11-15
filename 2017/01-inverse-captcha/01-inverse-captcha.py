def inverse_captcha(num_str):
	nums = list(num_str)
	num_sum = 0
	for index in range(len(nums)):
		num = int(nums[index])
		if index == len(nums)-1:
			next_num = int(nums[0])	
		else:
			next_num = int(nums[index+1])
		if num == next_num:
			num_sum += num
	return num_sum
