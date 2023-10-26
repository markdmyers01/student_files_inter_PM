"""

      task9_2_starter.py   -   Using Generators and Dictionary Comprehensions

       Working from your previous solution for task6_1_starter.py, or by using
       the solution below, modify this solution to use a generator.



"""
from collections import Counter

datafile = '../resources/cities15000.txt'
# cities = []


def country_generator(filename):
    with open(filename, encoding='utf8') as cities_file:
        for line in cities_file:
            yield line.strip().split('\t')[8]


most_common = Counter(country_generator(datafile)).most_common(5)
print(most_common)
