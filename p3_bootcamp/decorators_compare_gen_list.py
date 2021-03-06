from time import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing: {fn.__name__}")
        print(f"Time elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_gen_nums():
    return sum(x for x in range(100000000))


@speed_test
def sum_list_nums():
    return sum([x for x in range(100000000)])


print(sum_gen_nums())
print(sum_list_nums())

