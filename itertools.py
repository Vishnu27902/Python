import itertools

from itertools import permutations
# a=["".join(i) for i in permutations("1894762222")]
b=["".join(i) for i in itertools.product("1234",repeat=4)][:]
[print(j) for j in b if len(set(j))==len(j)]