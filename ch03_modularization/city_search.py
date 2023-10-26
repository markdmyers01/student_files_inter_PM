"""
      city_search.py   -   Refactored task2_3.py solution,
                           used with task3_1_starter.py

      This module is called by task3_1_starter.py.  It reads data from cities15000.txt,
      collects the name, population, elevation, and country code into a NamedTuple.

      It provides a highest() and largest() function for calculating each of those.
      Finally, it allows for searching cities by name and returning results.
"""
from typing import NamedTuple

_cities = []
header = [('name', str), ('population', int), ('elevation', int), ('country', str)]
City = NamedTuple('City', header)


def read_data(fullname):
    with open(fullname, encoding='utf-8') as f:
        for line in f:
            fields = line.strip().split('\t')
            name = fields[1]
            country = fields[8]
            population = int(fields[14])
            elevation = int(fields[16])
            city = City(name, population, elevation, country)
            _cities.append(city)


def largest():
    return sorted(_cities, key=lambda city: city.population, reverse=True)[0]


def highest():
    return sorted(_cities, key=lambda city: city.elevation, reverse=True)[0]


def search(name):
    results = []
    for item in _cities:
        if name.lower() in item.name.lower():
            results.append(item)
    return results


if __name__ == '__main__':
    filepath = '../resources/cities15000.txt'
    read_data(filepath)
    print(_cities[:5])