import time
from libs.timer import stopwatch
from libs.memory_profiler import memory_profiler

@stopwatch
def ex(a, b):
    for i in range(1, 2, 1):
        time.sleep(1)

    return a + b

print(ex(1, 2))

@memory_profiler
def ex1():
    data = [i for i in range(10**6)]
    return sum(data)

ex1()