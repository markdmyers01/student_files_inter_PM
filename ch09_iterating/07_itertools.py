from itertools import chain, islice, count
from pathlib import Path


# chain example
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [4, 5, 6]
# list4 = []
# list4.append(list1)
list4 = [list1, list2, list3]
chained_list = chain(*list4)       # chained list is an iterator, not a new list
print(set(chained_list))                       # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# islice example
with Path('../resources/cities15000_info.txt').open(encoding='utf-8') as f:
    for line in islice(f, 7, None):
        print([i for i in line.strip().split(':')][0].strip())


# count(start, step)    is an iterator with no upper bound
# unlike range which requires an upper bound
iterable = count(start=10, step=10)
while (val := next(iterable)) <= 50:
    print(val)
