import time


def log_time(func, *args):
    """
    Responsible to measure time spent by method `func`
    :param func: method to be monitored
    :param args: expected arguments from method `func`
    :return: tuple with time spent and result from method `func`
    """
    st = time.time()
    result = func(*args)
    return time.time() - st, result
