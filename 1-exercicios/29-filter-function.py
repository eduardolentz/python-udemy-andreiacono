
# FUNÇÂO FILTER
    # https://docs.python.org/pt-br/3/library/functions.html#filter

valores = [10,20,30,40,57]

'''def remover20(x):
    return x > 20

print(list(map(remover20, valores)))
print(list(filter(remover20, valores)))'''

print(list(filter(lambda x: x >20, valores)))