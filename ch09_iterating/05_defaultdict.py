import json
from collections import defaultdict

d1 = defaultdict(float)
d1['greet1'] = 'hello'
print(d1['greet1'])     # works as expected
print(d1['greet2'])     # not valid, invokes the str() constructor as a result
d1['greet3'] = None
print(d1)

print(json.dumps(d1))
