import time


def time_performance(func, *args, **kwargs):
    t0 = time.time()
    func(*args, **kwargs)
    t1 = time.time()
    return t1 - t0


def time_performance_recursive(func, inputs=[], **kwargs):
    """Returns an array with timestamps."""
    times = []
    for input_ in inputs:
        dt = time_performance(func, *input_)
        times.append(dt)
    return times
