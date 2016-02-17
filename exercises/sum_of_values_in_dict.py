my_dict = {"a": [2,3,4,5], "b": [2,4,6,7,8], "c":[30, 50, 60]}

def largest_value(dictn):
    largest_value = 0
    for key in dictn:
        largest = len(dictn[key])
        if largest_value < largest:
            largest_value = largest
            value_key = key
    return value_key
def sum_of_values(dictn):
    sum_of_values = 0
    for key in dictn:
        sum_of_values += sum(dictn[key])
    return sum_of_values


print largest_value(my_dict)
print sum_of_values(my_dict)
