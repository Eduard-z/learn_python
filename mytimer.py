import time
reps = 1000
repslist = range(reps)


def timer(func, *pargs, **kargs):
    start = time.perf_counter()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.perf_counter() - start
    return (elapsed, ret)
