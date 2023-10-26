"""
    08_decorators.py

    Here it is..(finally!)...the decorator syntax
"""


def shortener(func):
    width = 15

    def wrapper(val):
        print(f'Before value: {val}')
        val = val[:width] + '...'
        ret = func(val)
        print(f'After value: {val}')
        return f'This is whatever the wrapper is going to return - and this is what display returned {ret}'
    return wrapper


@shortener
def display(val):
    # print(val)
    return val


data = 'This is a long string that will be truncated.'
x = display(data)
print(x)
