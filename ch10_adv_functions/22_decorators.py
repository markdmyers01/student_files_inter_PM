"""
    22  _decorators.py
    Decorators that accept arguments (class-based)
"""


class output_formatter:
    """
        supports two arguments: mask - masks the last name,
                                allcaps keyword - displays lastname
    """

    def __init__(self, mask=None, allcaps=False):
        self.mask = mask
        self.allcaps = allcaps

    def my_dec(self, f):
        def wrapper(*args):
            if self.allcaps:
                args = tuple([arg.upper() for arg in args])
            if self.mask:
                args = (args[0], '****') + args[2:]

            # retval = f(*args)
            # return retval
            f(*args)
        return wrapper


@output_formatter(mask=True, allcaps=True).my_dec
def my_func(first, last):
    print(f'{first} {last}')


@output_formatter(False, allcaps=False).my_dec
def my_func2(first, last):
    print(f'{first} {last}')


my_func('Bill', 'Smith')
my_func2('Bill', 'Smith')
