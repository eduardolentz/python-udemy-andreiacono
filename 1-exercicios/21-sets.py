
# SETS
    # Similar a listas
    # Evitaa intens duplicados
    # Não utuliza index
    
list1 = [10,20,30,40,50]
list2 = [10,20,60,70]

num1 = set(list1)
num2 = set(list2)

print(num1)

'''
Operadores:
| (Union) --> Junta tirando os valores duplicados
- (Defference) --> Os valores q aparecem no primeiro set q não aprecem no segundo 
^ (Symmetric Difference) --> Retira os repetidos nas duas listas
& (And) --> O que é duplicado em ambas as listas
'''

print(num1 | num2)
print(num1 - num2)
print(num1 ^ num2)
print(num1 & num2)

print(len(num1))
# print(num1[0])  --> error 