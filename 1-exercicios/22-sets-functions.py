# SETS
    # Similar a listas
    # Evitaa intens duplicados
    # Não utuliza index
    # https://docs.python.org/3/library/stdtypes.html#set
    
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [10,20,60,70]

num1 = set(list1)

set = {}   # --> Declara um dicionario vazio
print(type(set))

set1 = {8,9,7,4,4,5,2,1}
set2 = set1.copy()
set1.add(24)
set1.update([8,10,12,47])
set1.remove(10)
set1.discard(90) # --> Não gera erro se o numero não estiver no set



print(type(num1))
print(type(list2))
print(type(set1))


print(set1)
print(set2)

print(type(set))
