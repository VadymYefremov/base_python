""" Сalculating factorial by def & lambda  """
import functools
import time


def benchmark(iters):
    """ Decorator for testing speed calculatig factorial
     iters - the number of repetitions of the operation
     used for testing speed """
    def actual_decorator(func):

        def wrapper(*args, **kwargs):
            total = 0
            for _i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] среднее время выполнения: {} секунд.'.format(total / iters))

            return return_value

        return wrapper

    return actual_decorator


@benchmark(5)
def factorial():
    """ Calculating factorial by def """
    res = 1
    for i in range(1, 6):
        res *= i
    return res


factorial()


@benchmark(5)
def factorial_2():
    """ Calculating factorial by lambda"""
    factorial2 = functools.reduce(lambda x, y: x * y, range(1, 6))
    return factorial2


print(factorial_2())
