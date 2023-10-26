"""
    task8_1_starter.py

    This task asks us to retrieve JSON data (from a network request to a server to a
    database and back) and store the results in a list of data classes.

    We will then take that list of data classes and persist it to a file in the form of
    JSON data.

    This is a sample of what the retrieved JSON looks like:
{
    "name":"Burns",
    "results":[{ "actor":"Christopher Collins (early season 1), Harry Shearer",
                 "episode_debut":"\"Simpsons Roasting on an Open Fire\"",
                 "name":"Charles Montgomery Burns",
                 "original_air_date":"1989-",
                 "role":"Owner of the Springfield Nuclear Power Plant."},

               ...(additional characters may be returned)...

    ]
}


    Step 1.  BE SURE YOUR SERVER IS RUNNING (right-click wsgi.py in the ch08_network_api/server folder)

    Follow the remaining steps below....
"""
import dataclasses
import datetime
import json

import requests

results = []


@dataclasses.dataclass
class Character:
    name: str
    actor: str
    role: str
    original_air_date: datetime.date



char_name = input('Enter partial Simpsons character name: ')
url = f'http://localhost:8051/simpsons?char_name={char_name}'

data = requests.get(url).json()


# The following will convert the dict from step 3 into a list of data classes...
# be sure to call your dict from step 3 'data' as shown below
for character in data.get('results', []):
    actor = character.get('actor')
    name = character.get('name')
    role = character.get('role')
    date_str = character.get('original_air_date')
    try:
        orig_air_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        orig_air_date = date_str

    results.append(Character(name, actor, role, orig_air_date))


class CharacterEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            result = obj.__dict__
        except (AttributeError, TypeError):
            if isinstance(obj, datetime.date):
                result = obj.strftime('%Y-%b-%d')
            else:
                result = '(unknown type)'
        return result


with open('simpsons_data.json', 'wt') as f:
    json.dump(results, f, cls=CharacterEncoder, indent=4)
    print('Write complete. Open file to view results.')



