def two_sum(main_list, target):
	for index, item in enumerate(main_list):
		num = target - item
		if num in main_list:
			if num != item:
				return [index, main_list.index(num)]
two_sum([1, 10, 33, 8, 6, 5, 4], 12)