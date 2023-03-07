import copy

def cpy(ls):
    # ls=copy.deepcopy(ls)
    ls[1]=2
l=[1,1,1]
print(l)
print(cpy(l))
print(l)