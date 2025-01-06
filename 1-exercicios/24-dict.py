# Dictionaries  --> dicionarios
    # Utiliza index no formato keys e values
    # Aceita string, integer, float, boolean
    # https://docs.python.org/pt-br/3.13/tutorial/datastructures.html#dictionaries


aluno1 = {'nome':'Ana','idade':13}
aluno2 = {'nome':'Pedro','idade':16}

print(aluno1)
print(aluno2['nome']) # --> Index é a Key

# Alterar dados em dicionarios
aluno1['nome'] = 'Jose'
print(aluno1)

aluno1.update({'nome':'Eduardo', 'idade':28, 'aprovado':True})

del aluno1['idade']
print(aluno1)

print(aluno1.get('indereco', 'Não existe'))


