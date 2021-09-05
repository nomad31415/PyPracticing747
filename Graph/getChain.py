
from  functools import reduce

xxx = reduce(lambda x,y: min(x,y)  , {'abcd','abc','ghjkkl','zx','ab'})
y = set(filter(lambda x: x[:len(xxx)] == xxx, {'abcd','abc','ab','dfghj'}))
print("Result: {},({})".format(len(y),y ))


