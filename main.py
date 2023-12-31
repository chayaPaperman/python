from functools import wraps
import datetime
import time
from datetime import *


def timeRunning(func):
    def wrapper(*args):
        first = datetime.now().minute
        func()
        print(datetime.now().minute - first)

    return wrapper


@cashe_func
@timeRunning
def func1():
    i = 0
    for _ in range(10000000000):
        i += 1

dict1 = {}


def cache_func(func):

    def inner():
        f = dict1.get(func.__name__)
        if f is None:
            dict1.update([(func.__name__, func())])
            f = dict1.get(func.__name__)
        return f
    return inner()

@timeRunning
@cache_func
def check_func():
    y = 0
    for i in range(1000):
        y += 1
    return y


print(check_func)
print(check_func)
print(check_func)
print(check_func)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Everyone')
    print(print_hi.__name__)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
