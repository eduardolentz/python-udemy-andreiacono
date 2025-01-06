
# ARRAYS -->
    # Similar a listas
    # Para melhorar a performance do código --> Acima de mil
    # Módulo
    # https://docs.python.org/pt-br/3.7/library/array.html
    
from array import array    
    
letras = ['a','b','c','d']
num_i = [10,20,30,40]
num_f = [1.5,2.2,3,8]

print(letras)
print(num_i)
print(num_f)

array_letras = array('u',['a','b','c','d'])
array_num_i = array('i', [10,20,30,40])
array_num_f = array('f', [1.5,2.2,3,8])

print(array_letras)
print(array_num_i)
print(array_num_f)

print(type(array_letras))

    