# DICIONARIOS

aluno = {
    'nome':'Eduardo',
    'idade':28,
    'nota': 9.8, 
    'aprovado':True, 
    'materias': ['mat', 'ing','fis']
}

print(aluno)

print(aluno.get('materias'))
print(len(aluno))

print(aluno.keys())
print(aluno.values())
print(aluno.items())

lista = aluno.items()

print(len(lista))
print(type(lista))