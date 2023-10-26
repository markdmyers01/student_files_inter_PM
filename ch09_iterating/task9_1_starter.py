"""

      task9_1_starter.py   -   Determining the country with the most cities with more than
                               15000 people.  Read cities15000.txt.


"""
from collections import Counter

datafile = '../resources/cities15000.txt'

cities = []
with open(datafile, encoding='utf8') as cities_file:
    for line in cities_file:
        cities.append(line.strip().split('\t')[8])
print(cities[:5])
most_common = Counter(cities).most_common(10)
print(most_common)
