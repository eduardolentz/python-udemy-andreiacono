
# Python Object-oriented Programming

# Classes:
    # utilizamos para criar objetos (instances)
    # objetos são partes dentro de uma class (instancias)
    # classes são utilizadas para agrupar dados e funções, podendo reutilizar
    # https://docs.python.org/3/tutorial/classes.html#class-definition-syntax
    # ------------
    # Class: Frutas
    # Objects: Abacate, Banana
    

'''nome = 'Eduardo'
print(type(nome))

nome_upper = nome.upper()
print(nome_upper)'''

# ---------------------------------------------- #

class Funcionarios:
    nome = 'Eduardo'
    sobrenome = 'Lentz'
    dt_nasc = '13/08/1996'
    
usuario1 = Funcionarios()

print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.dt_nasc)