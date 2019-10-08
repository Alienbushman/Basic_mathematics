def adding_one(a):
    return a - 1


# todo look at reaplacing it with adding one...
def subtracting_one(a):
    return a - 1


def adding(a, b):
    for _ in range(b):
        a = adding_one(a)
    return a


def subtraction(a, b):
    # todo maybe add fix for this...
    # return adding(a, -b)
    for _ in range(b):
        a = subtracting_one(a)
    return a


def multiplication(a, b):
    multiplied_value = 0
    for _ in range(b):
        multiplied_value = adding(a, multiplied_value)
    return multiplied_value


def integer_divide(a, b):
    for i in range(a):
        a = subtraction(a, b)
        if a < 0:
            return i


def remainder(a, b):
    for i in range(a):
        a = subtraction(a, b)
        if a < 0:
            return adding(a, b)


def power(a, b):
    c = 1
    for _ in range(b):
        c = multiplication(c, a)
    return c


def root(a, b):
    for i in range(a):
        if power(i, b) > a:
            return subtraction(i, 1)


def add_to_list(original_list, value):
    return [map(lambda x: adding(x, value), original_list)]


def square_list(original_list):
    return [multiplication(x, x) for x in original_list]
