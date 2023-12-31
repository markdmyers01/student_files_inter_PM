"""

    Using Path() provides additional ways to read from a file

"""
from pathlib import Path
import sys

path = Path('../resources')
filename = 'access_.log'
filepath = path / filename

lines = []
f = None
try:
    f = open(filepath, encoding='utf-8')
    lines = f.readlines()
except IOError as err:
    print(f'Error: {err}', file=sys.stderr)
finally:
    if f:
        f.close()

print(f'{len(lines)} lines read.')


# Using Path() in a 'with' control
lines = []
try:
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()
except IOError as err:
    print(f'Error {err}', file=sys.stderr)

print(f'{len(lines)} lines read.')



# Using the Path() object's open() method in a 'with' control
lines = []
try:
    with filepath.open(encoding='utf-8') as f:
        lines = f.readlines()
except IOError as err:
    print(f'Error: {err}', file=sys.stderr)

print(f'{len(lines)} lines read.')


lines = []
try:
    lines = filepath.read_text(encoding='utf-8').split('\n')
except IOError as err:
    print(f'Error: {err}', file=sys.stderr)
print(f'{len(lines)} lines read.')

print(lines[-5:])