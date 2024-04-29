# https://www.youtube.com/watch?v=q4o_1cXAS-c&t=251s&ab_channel=PythonRussian

def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} started")
        result = func(*args)
        print(f"{func.__name__} finished")
        return result

    return wrapper


@logger
def summ(a, b):  # в этот момент summ == wrapper
    return a + b


print(summ(3, 3))
# print(summ)

if __name__ == '__main__':
    # function = logger(summ)
    # print(function(2, 3))

    # logger(summ)(2, 3)
    #
    # summ = logger(summ)
    # print(summ(2, 3))
    pass
