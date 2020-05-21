from time import perf_counter


def timer(f):
    def modified_func(*args):
        start = perf_counter()
        f(*args)
        stop = perf_counter()
        print(stop - start)

    return modified_func


@timer
def time_consumer(n):
    for i in range(0, n):
        n = 1 + 1


time_consumer(100000000)
