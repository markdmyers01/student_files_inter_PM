"""
      task3_1_starter.py   -   Modularization

      This file represents the driver for our city_search.py module.

      It reads data from resources/cities15000.txt (a tsv file).
      Determines the largest city and highest city.
      Allows for searching by city names to determine a city population.

"""
from pathlib import Path

import ch03_modularization.city_search as cs

working_dir = '../resources'
data_file = 'cities15000.txt'
fullname = Path(working_dir) / data_file

cs.read_data(fullname)

print(cs.largest().name)
print(cs.highest().name, '\n')

results = cs.search('new')

if not results:
    print('No cities found.')
else:
    print(f'Total results: {len(results)}')
    unique_countries = set()
    col_header = [h[0].capitalize() for h in cs.header]
    print('{0:<35}{1:>15}{2:>15}{3:>10}'.format(*col_header))
    print('{0:-<75}'.format(''))
    for city in results:
        unique_countries.add(city.country)
        print('{0:<35}{1:>15,}{2:>15,}{3:>10}'.format(*city))
    print('{0:-<75}'.format(''))
    tot_pop = sum([r.population for r in results])
    print('{0:>35}{1:>15,}{2:>15}{3:>10}'.format('Total Population:', tot_pop, 'Countries:', len(unique_countries)))