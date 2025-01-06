
# FUNÇÂO MAP
    # Muito utilizado com listas
    # Aplicar uma função a um Terable, por item (list, tuple, dict, etc)
    # https://docs.python.org/3/library/functions.html#map
    
lista = [1,2,3,4]

def multi(x):
    return x * 2

lista2 = map(multi, lista)

print(list(lista2))


# Associando MAP com um função lambda

lista = [1,2,3,4]

#def multi(x):
#    return x * 2


print(list(map(lambda x: x * 2, lista)))


