from functools import reduce
def get_factorial(num):
    factorial = reduce(lambda x,y: x * y, range(1, num + 1), 1)
    return factorial


def recursive_factorial(num):
    if num == 0:
        return 1
    return num * recursive_factorial(num -1)

print get_factorial(0)
print recursive_factorial(1)
