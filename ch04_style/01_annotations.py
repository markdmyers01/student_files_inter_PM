"""
    01_annotations.py - This code runs without error.  But using improper
                        values in the functions and methods will cause the items
                        to be highlighted in the IDE.
"""
from dataclasses import dataclass
from typing import List, Tuple, Any, Union


def display_info(name: str, age: int, spouse: str, *children: Any,
                 parents: list, **other_family: Union[str, int, list]) -> dict:
    # print(len(spouse))
    # TODO: Need to do something with the args
    return display_info.__annotations__


print(display_info('John', 40, 10, 'Tim', 'Sam', 10,
                   parents=['Martha', 'Frank'], sister='Amy', sister_age=40, sister_list=[1, 2, 3]))

# print(display_info.__annotations__)
# Python 3.6+, variable annotations
my_list: List[int] = [1, 2, 3]
my_list.append('hello')
print(my_list)

# this is a type alias
Group = Tuple[str, str, int, float]


@dataclass
class Members:
    names: Group


c = Members(names=('John', 'Paul', 10, 1.5))
print(c)
c2 = Members(('John',))
print(c2)
