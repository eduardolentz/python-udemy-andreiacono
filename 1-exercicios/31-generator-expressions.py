
# GENERATOR EXPRESSIONS 
    # uma forma mais rapida para listas, dicionarios e etc
    # menos memoria alocada
    # valores em bytes

from sys import getsizeof

numeros1 = [x * 10 for x in range(100)]
print(type(numeros1))
print(numeros1)
print(getsizeof(numeros1))

print('-----------------')

numeros2 = (x * 10 for x in range(100))
print(type(numeros2))
print(numeros2)
print(list(numeros2))
print(getsizeof(numeros2))
