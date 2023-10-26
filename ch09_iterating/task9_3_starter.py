"""

      task9_3_starter.py   -   Using the argparse Module

      This exercise is a refactoring of the task9_2.py solution.  It
      proposes parsing command-line arguments to determine how many results to display.
      The following command line arguments shall be used:

        python task9_3_starter.py -c 5

		    or

        python task9_3_starter.py --count 5

"""
import argparse
from collections import Counter

datafile = '../resources/cities15000.txt'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', default='3', type=int, help='The number of countries to retrieve')

    return parser.parse_args()


def country_generator(filename):
    with open(filename, encoding='utf8') as cities_file:
        for line in cities_file:
            yield line.strip().split('\t')[8]


args = get_args()

most_common = Counter(country_generator(datafile)).most_common(args.count)
print(most_common)
