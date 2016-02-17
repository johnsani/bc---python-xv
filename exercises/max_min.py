def find_max_min(nums):
    maximum_number = nums[0]
    minimum_number = nums[0]
    for value in nums:
        if maximum_number < value:
          maximum_number = value
        if value < minimum_number:
          minimum_number = value
          if minimum_number == maximum_number:
              return [minimum_number]
    return [minimum_number, maximum_number]
print find_max_min([6,4])
