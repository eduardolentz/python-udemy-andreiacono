# SETS --> COM STRINGS
    # Similar a listas
    # Evitaa intens duplicados
    # Não utuliza index
    # https://docs.python.org/3/library/stdtypes.html#set


set1 = {'a','b','c'}
set2 = {'a','d','e'}
set3 = {'c','d','f'}

set4 = set1.union(set2, set3)
set5 = set1.difference(set3)
set6 = set1.intersection(set2) # --> O que aparece em ambos grupos
set7 = set1.symmetric_difference(set3)

print(set4)
print(set5)
print(set6)
print(set7)