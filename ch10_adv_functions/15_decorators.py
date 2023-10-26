"""
    15_decorators.py

    A decorator to measure time-to-execute.
"""
from itertools import islice
from pathlib import Path
import time


def profile(orig_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = orig_func(*args, **kwargs)
        finish = time.time()
        print(f'{orig_func.__name__} took {(finish - start):.2f}sec')
        return ret
    return wrapper


@profile
def func1(filepath):
    with Path(filepath).open(encoding='utf-8') as f:
        # for count, line in enumerate(islice(f, None, None)):
        # line_count = len(f.readlines())
        # for count, line in enumerate(f, start=1):
        #     # print(line.strip()[::-1])
        #     line_count = count
        return len(f.readlines())


print(f'{func1("../resources/access_.log")} lines read.')
